# PyQt4
项目使用pyinstaller进行打包，最终得到一个exe的执行文件。
首先执行：
    pyinstaller -F -w demo1.py
此时会在dist下生成一个exe执行文件，此时的执行文件不包含静态文件，比如图片。和代码同一级目录会生成一个demo1.spec文件，这个是进行打包配置的文件。
修改此文件，修改前：
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          [],
          name='demo2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
修改后：
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [('\\resources\\test.png','D:\\code\\pyexe\\resources\\test.png','DATA')],
          name='demo2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )

最后执行：
    pyinstaller -F -w demo1.spec 

如果想打包32位exe，需要python和PyQt4都是32位，再按照上述流程打包即可。