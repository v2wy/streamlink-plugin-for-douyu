# streamlink-plugin-for-douyu

### 依赖
因为需要执行js加密，所以依赖于`jsengine`
```
pip install jsengine quickjs
```

### 使用方法
https://streamlink.github.io/cli/plugin-sideloading.html

下载`douyu.py`之后放入指定文件夹，使用`streamlink`的时候会自动加载，或者可以加入参数手动指定`--plugin-dir DIRECTORY`。

### 效果

```json
streamlink -j https://www.douyu.com/8682569 

{
  "plugin": "douyu",
  "metadata": {
    "id": "8682569",
    "author": "\u51b7\u5c11icon",
    "category": "\u82f1\u96c4\u8054\u76df",
    "title": "\u97e9\u670d\u51b22000\u5206\u8bd5\u8bad"
  },
  "streams": {
    "tct_h5_900": {
      "type": "http",
      "method": "GET",
      "url": "https://tc-tct.douyucdn2.cn/dyliveflv3/8682569rIwPgnTge_900.flv?wsAuth=9a7d65f4484fd530b0ec8c9a8c93e182&token=web-h5-0-8682569-628e4e6046773bf3fdff1c614c4110c5bdbc4798d6b5b5d7&logo=0&expire=0&did=9bbe7210796245248da88b42eb716b8f&pt=2&st=0&sid=394266675&mcid2=0&origin=tct&mix=0&isp=",
      "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Origin": "https://www.douyu.com/8682569",
        "Referer": "https://www.douyu.com/8682569"
      },
      "body": null
    },
    "hw_h5_900": {
      "type": "http",
      "method": "GET",
      "url": "https://hw3.douyucdn2.cn/live/8682569rIwPgnTge_900.flv?wsAuth=d52a48cbe2a9a05bd5698e77d78f01f1&token=web-h5-0-8682569-628e4e6046773bf3e40abbded8536382e1ba40d6a22847b3&logo=0&expire=0&did=9bbe7210796245248da88b42eb716b8f&pt=2&st=0&sid=394266675&mcid2=0&origin=tct&mix=0&isp=",
      "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Origin": "https://www.douyu.com/8682569",
        "Referer": "https://www.douyu.com/8682569"
      },
      "body": null
    },
    "tct_h5_2000": {
      "type": "http",
      "method": "GET",
      "url": "https://tc-tct.douyucdn2.cn/dyliveflv3/8682569rIwPgnTge_2000.flv?wsAuth=ae12654d2b3daf1f2f7297f9e131db54&token=web-h5-0-8682569-628e4e6046773bf36e04c590a5e27c805c4b2c90cc77ac17&logo=0&expire=0&did=9bbe7210796245248da88b42eb716b8f&pt=2&st=0&sid=394266675&mcid2=0&origin=tct&mix=0&isp=",
      "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Origin": "https://www.douyu.com/8682569",
        "Referer": "https://www.douyu.com/8682569"
      },
      "body": null
    },
    "hw_h5_2000": {
      "type": "http",
      "method": "GET",
      "url": "https://hw3.douyucdn2.cn/live/8682569rIwPgnTge_2000.flv?wsAuth=a3c6dbb09fa094adc97b10090662b44b&token=web-h5-0-8682569-628e4e6046773bf310637ab42cc3d7c2cf537093ee51b411&logo=0&expire=0&did=9bbe7210796245248da88b42eb716b8f&pt=2&st=0&sid=394266675&mcid2=0&origin=tct&mix=0&isp=",
      "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Origin": "https://www.douyu.com/8682569",
        "Referer": "https://www.douyu.com/8682569"
      },
      "body": null
    },
    "tct_h5_4000": {
      "type": "http",
      "method": "GET",
      "url": "https://tc-tct.douyucdn2.cn/dyliveflv3/8682569rIwPgnTge_4000.flv?wsAuth=1ad6386ba4abf0682b0165644360e15a&token=web-h5-0-8682569-628e4e6046773bf35bab75587d793702181d44022c9ef291&logo=0&expire=0&did=9bbe7210796245248da88b42eb716b8f&pt=2&st=0&sid=394266675&mcid2=0&origin=tct&mix=0&isp=",
      "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Origin": "https://www.douyu.com/8682569",
        "Referer": "https://www.douyu.com/8682569"
      },
      "body": null
    },
    "hw_h5_4000": {
      "type": "http",
      "method": "GET",
      "url": "https://hw3.douyucdn2.cn/live/8682569rIwPgnTge_4000.flv?wsAuth=41c6e9b9c86819a2b254a58acc24b313&token=web-h5-0-8682569-628e4e6046773bf3464932df31b51c8e22946fb0efdacd12&logo=0&expire=0&did=9bbe7210796245248da88b42eb716b8f&pt=2&st=0&sid=394266675&mcid2=0&origin=tct&mix=0&isp=",
      "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Origin": "https://www.douyu.com/8682569",
        "Referer": "https://www.douyu.com/8682569"
      },
      "body": null
    },
    "tct_h5_8113": {
      "type": "http",
      "method": "GET",
      "url": "https://tc-tct.douyucdn2.cn/dyliveflv3/8682569rIwPgnTge.flv?wsAuth=f2ee51dec43e63ea74eafc96cad05bf8&token=web-h5-0-8682569-628e4e6046773bf3da265bebf858968c6732c669161e63ad&logo=0&expire=0&did=9bbe7210796245248da88b42eb716b8f&pt=2&st=0&sid=394266675&mcid2=0&origin=tct&mix=0&isp=",
      "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Origin": "https://www.douyu.com/8682569",
        "Referer": "https://www.douyu.com/8682569"
      },
      "body": null
    },
    "hw_h5_8113": {
      "type": "http",
      "method": "GET",
      "url": "https://hw3.douyucdn2.cn/live/8682569rIwPgnTge.flv?wsAuth=0c3bc5e43bf3434eda21be1f31230d10&token=web-h5-0-8682569-628e4e6046773bf337882208585b8b951217c5e80aa9be72&logo=0&expire=0&did=9bbe7210796245248da88b42eb716b8f&pt=2&st=0&sid=394266675&mcid2=0&origin=tct&mix=0&isp=",
      "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Origin": "https://www.douyu.com/8682569",
        "Referer": "https://www.douyu.com/8682569"
      },
      "body": null
    },
    "worst": {
      "type": "http",
      "method": "GET",
      "url": "https://tc-tct.douyucdn2.cn/dyliveflv3/8682569rIwPgnTge_900.flv?wsAuth=9a7d65f4484fd530b0ec8c9a8c93e182&token=web-h5-0-8682569-628e4e6046773bf3fdff1c614c4110c5bdbc4798d6b5b5d7&logo=0&expire=0&did=9bbe7210796245248da88b42eb716b8f&pt=2&st=0&sid=394266675&mcid2=0&origin=tct&mix=0&isp=",
      "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Origin": "https://www.douyu.com/8682569",
        "Referer": "https://www.douyu.com/8682569"
      },
      "body": null
    },
    "best": {
      "type": "http",
      "method": "GET",
      "url": "https://hw3.douyucdn2.cn/live/8682569rIwPgnTge.flv?wsAuth=0c3bc5e43bf3434eda21be1f31230d10&token=web-h5-0-8682569-628e4e6046773bf337882208585b8b951217c5e80aa9be72&logo=0&expire=0&did=9bbe7210796245248da88b42eb716b8f&pt=2&st=0&sid=394266675&mcid2=0&origin=tct&mix=0&isp=",
      "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Origin": "https://www.douyu.com/8682569",
        "Referer": "https://www.douyu.com/8682569"
      },
      "body": null
    }
  }
}
```