# -*- mode: python -*-

block_cipher = None


a = Analysis(['CattwalkV3C.py'],
             pathex=['C:\\Users\\josha\\Desktop\\[PROGRAM]\\[PYTHON]\\Cattwalk\\CATTWALKv3'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='CattwalkV3C',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='CattwalkV3C')
