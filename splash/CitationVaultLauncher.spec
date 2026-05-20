# PyInstaller 6.x spec for CitationVaultLauncher
# Run on Windows:  pyinstaller CitationVaultLauncher.spec
#
# Place CitationVault.exe in the same output folder as the compiled launcher,
# or adjust the `binaries` list below to bundle it inside the single file.

a = Analysis(
    ['CitationVaultLauncher.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='CitationVaultLauncher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
