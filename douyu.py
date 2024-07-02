"""
$description Chinese live-streaming platform for live video game broadcasts and individual live streams.
$url huya.com
$type live
$metadata id
$metadata author
$metadata title
"""
import logging
import re
import time
import traceback
import uuid
from typing import Dict
from urllib.parse import parse_qs

import jsengine

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.http import HTTPStream

log = logging.getLogger(__name__)


@pluginmatcher(re.compile(
    r"https?://(?:www\.)?douyu\.com/(?P<channel>[^/?]+)",
))
class Douyu(Plugin):
    QUALITY_WEIGHTS: Dict[str, int] = {}

    @classmethod
    def stream_weight(cls, key):
        weight = cls.QUALITY_WEIGHTS.get(key)
        if weight:
            return weight, key

        return super().stream_weight(key)

    def _get_streams(self):
        channel = self.match.group("channel")
        roomIdKey = f"douyu:room_id:{channel}"
        room_id = self.cache.get(roomIdKey)
        if not room_id:
            room_id = self.session.http.get(
                self.url,
                timeout=5,
                schema=validate.Schema(
                    validate.any(
                        validate.regex(re.compile(r'\$ROOM\.room_id\s*=\s*(\d+)')),
                        validate.regex(re.compile(r'apm_room_id\s*=\s*(\d+)')),
                    ),
                    validate.get(1)
                ))
            self.cache.set(roomIdKey, room_id)
        if not room_id:
            logging.debug(self.url + " 未获取到房间号")
            return
        self.id = room_id
        show_status, video_loop, self.title, self.category, self.author = self.session.http.get(
            f"https://www.douyu.com/betard/{room_id}",
            timeout=5,
            schema=validate.Schema(
                validate.parse_json(),
                validate.get('room'),
                validate.union_get(
                    'show_status', 'videoLoop', 'room_name', 'second_lvl_name', 'nickname'
                )
            ))
        if show_status != 1:
            logging.debug(self.url + " 未开播")
            return
        if video_loop != 0:
            logging.debug(self.url + " 正在放录播")
            return

        did = uuid.uuid4().hex
        tt = str(int(time.time()))

        params = {
            'cdn': 'tct-h5',
            'did': did,
            'tt': tt,
            'rate': 0
        }

        origin_stram_info = self.get_streams(room_id, params)

        for cdn_info in origin_stram_info['data']['cdnsWithName']:
            for quantity_info in origin_stram_info['data']['multirates']:
                if cdn_info['cdn'] == 'tct-h5' and quantity_info['rate'] == 0:
                    stram_info = origin_stram_info
                else:
                    params = {
                        'cdn': cdn_info['cdn'],
                        'did': did,
                        'tt': tt,
                        'rate': quantity_info['rate']
                    }
                    stram_info = self.get_streams(room_id, params)

                self.session.http.headers.update({
                    "Origin": self.url,
                    "Referer": self.url,
                })
                name = f"{cdn_info['cdn']}_{quantity_info['bit']}".replace("-", "_")
                vbitrate = quantity_info['bit']

                self.QUALITY_WEIGHTS[name] = vbitrate

                url = f"{stram_info['data']['rtmp_url']}/{stram_info['data']['rtmp_live']}"

                yield name, HTTPStream(self.session, url)

        log.debug(f"QUALITY_WEIGHTS: {self.QUALITY_WEIGHTS!r}")

    def get_streams(self, room_id, params):
        js = self.get_js(room_id)
        try_times = 3
        while try_times:
            try:
                query = js.call('ub98484234', room_id, params['did'], params['tt'])
                break
            except Exception as e:
                traceback.print_stack()
                logging.error(format(e))
                try_times = try_times - 1
        params.update({k: v[0] for k, v in parse_qs(query).items()})
        return (self.session.http.post(
            url=f'https://www.douyu.com/lapi/live/getH5Play/{room_id}',
            params=params,
            timeout=5,
            schema=validate.Schema(
                validate.parse_json(),
                {
                    'error': int,
                    'msg': str,
                    'data': {
                        'rtmp_url': validate.url(),
                        'rtmp_live': str,
                        'multirates': [
                            {
                                'name': str,
                                'bit': int,
                                'rate': int
                            }
                        ],
                        'cdnsWithName': [
                            {
                                'name': str,
                                'cdn': str,
                            }
                        ]
                    }
                }
            )
        ))

    def get_js(self, channel):
        key1 = f'douyu:homeH5Enc:{channel}'
        if self.cache.get(key1):
            js_enc = self.cache.get(key1)
        else:
            response = (self.session.http.post(
                url=f'https://www.douyu.com/swf_api/homeH5Enc?rids={channel}',
                timeout=5
            )).json()
            js_enc = response['data'][f'room{channel}']
            self.cache.set(key1, js_enc)

        key2 = f'douyu:cryptojs'

        if self.cache.get(key2):
            crypto_js = self.cache.get(key2)
        else:
            crypto_js = (self.session.http.get(
                url='https://cdn.staticfile.org/crypto-js/4.1.1/crypto-js.min.js',
                timeout=5
            )).text
            self.cache.set(key2, crypto_js)
        return jsengine.JSEngine(js_enc + crypto_js)


__plugin__ = Douyu