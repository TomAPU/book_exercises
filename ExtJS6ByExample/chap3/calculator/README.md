# Extjs by example : calculator

This "Calculator" is one of the sample projects detailed in the book "[ExtJS by Example](https://www.packtpub.com/web-development/ext-js-example)". This sample application uses ExtJS 6. 

由于通过 `requires` 使用了动态依赖，依赖文件会通过 XMLHttpRequest 方式下载，因此不能直接 index.html（XMLHttpRequest 不能从本地文件系统加载文件）。

需要开启一个 Web Server，一般格式为 `sencha fs web -p 80 start -map /path/to/webroot/`，如：

```bash
$ sencha fs web -p 8080 start -map ./
```

然后在浏览器中打开。


Note, this example uses cloudflare CDN for ExtJS 6. If the CDN doesn't work, you may need to update ExtJS lib urls in index.html and point to the local ExtJS library path.


# Folder structure

```
-app
  -view
    -main
      Main.js
      MainController.js
      MainModel.js
app.js
index.html
-lib
  -ext
    ext-all.js
    -theme
      -crisp
        ext-theme-crisp-all_01.css
        ext-theme-crisp-all_02.css
        ext-theme-crisp-all.css
        ext-theme-crisp.css
-resources
  -css
    app.css
```
