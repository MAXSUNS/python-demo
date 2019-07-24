# PyQt4
项目使用pyinstaller进行打包，最终得到一个exe的执行文件。
首先执行：
    pyinstaller -F -w demo1.py
此时会在dist下生成一个exe执行文件，此时的执行文件不包含静态文件，比如图片。和代码同一级目录会生成一个demo1.spec文件，这个是进行打包配置的文件。
修改此文件，修改前：

          修改后：
最后执行：
    pyinstaller -F -w demo1.spec 
