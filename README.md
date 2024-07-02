# streamlink-plugin-for-douyu

### 依赖
因为需要执行js加密，所以依赖于`jsengine`
```
pip install jsengine quickjs
```

### 使用方法
https://streamlink.github.io/cli/plugin-sideloading.html

下载`douyu.py`之后放入指定文件夹，使用`streamlink`的时候会自动加载，或者可以加入参数手动指定`--plugin-dir DIRECTORY`。
