# CitationVault

**CitationVault** is a Windows desktop application for managing and organizing your citations, references, and research sources — all in one place.

---

## Download

Head to the [**Releases**](../../releases) page and grab the latest `CitationVault.exe`.

No installation required — just download and run.

---

## Getting Started

1. Download `CitationVault.exe` from the [Releases](../../releases) page
2. Double-click to launch
3. Start adding and organizing your citations

---

## Features

- Store and search citations quickly
- Organize references by project or category
- Lightweight single-file Windows executable — no install needed

---

## Splash Screen Launcher *(optional)*

The `splash/` folder contains a branded launcher that displays a **Maridizzle** splash screen before opening CitationVault. To build it on a Windows machine:

**Requirements**
- Python 3.9+ for Windows
- `pip install pyinstaller`

**Build**
```
cd splash
pyinstaller CitationVaultLauncher.spec
```

Place the output `CitationVaultLauncher.exe` next to `CitationVault.exe`. Run the launcher instead of the main exe to get the splash experience.

---

## Credits

Made by **Maridizzle**

---

## License

All rights reserved © Maridizzle
