# PyInstaller spec for CitationVaultLauncher
# Run on Windows:  pyinstaller CitationVaultLauncher.spec
#
# Place CitationVault.exe in the same output folder as the compiled launcher,
# or adjust the `binaries` list below to bundle it inside the single file.

block_cipher = None

a = Analysis(
    ['CitationVaultLauncher.py'],
    pathex=['.'],
    binaries=[],          # add ('CitationVault.exe', '.') to bundle the main exe
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zfiles, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CitationVaultLauncher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,          # windowed — no console window
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
