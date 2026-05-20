"""
CitationVault splash screen launcher.
Shows a branded Maridizzle splash for ~2.5 s then launches the bundled
CitationVault.exe. Designed to be compiled with PyInstaller --add-binary
to embed the real app inside this single exe.

On first run, the embedded app is copied to %LOCALAPPDATA%\\CitationVault\\
so it survives PyInstaller's temp-folder cleanup when the launcher exits.
"""

import os
import sys
import shutil
import subprocess
import tempfile
import threading
import tkinter as tk


SPLASH_DURATION_MS = 2500
EXE_NAME = "CitationVault.exe"

BG_COLOR = "#0d1117"
ACCENT_COLOR = "#58a6ff"
TEXT_COLOR = "#e6edf3"
SUB_COLOR = "#8b949e"


def resolve_app_path():
    if getattr(sys, "frozen", False):
        bundled = os.path.join(sys._MEIPASS, EXE_NAME)
        target_dir = os.path.join(
            os.environ.get("LOCALAPPDATA", tempfile.gettempdir()),
            "CitationVault",
        )
        os.makedirs(target_dir, exist_ok=True)
        target = os.path.join(target_dir, EXE_NAME)

        needs_copy = (
            not os.path.exists(target)
            or os.path.getsize(target) != os.path.getsize(bundled)
        )
        if needs_copy:
            shutil.copy2(bundled, target)
        return target

    return os.path.join(os.path.dirname(os.path.abspath(__file__)), EXE_NAME)


def launch_app():
    app_path = resolve_app_path()
    flags = 0
    if hasattr(subprocess, "DETACHED_PROCESS"):
        flags = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
    subprocess.Popen([app_path], creationflags=flags, close_fds=True)


def build_splash(root):
    root.overrideredirect(True)
    root.configure(bg=BG_COLOR)
    root.attributes("-topmost", True)

    width, height = 480, 260
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - width) // 2
    y = (sh - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")

    border = tk.Frame(root, bg=ACCENT_COLOR, bd=0)
    border.place(x=0, y=0, width=width, height=height)

    inner = tk.Frame(border, bg=BG_COLOR)
    inner.place(x=2, y=2, width=width - 4, height=height - 4)

    tk.Label(
        inner,
        text="CitationVault",
        font=("Segoe UI", 32, "bold"),
        fg=TEXT_COLOR,
        bg=BG_COLOR,
    ).pack(pady=(48, 4))

    tk.Label(
        inner,
        text="by  Maridizzle",
        font=("Segoe UI", 13),
        fg=ACCENT_COLOR,
        bg=BG_COLOR,
    ).pack()

    tk.Label(
        inner,
        text="Loading…",
        font=("Segoe UI", 9),
        fg=SUB_COLOR,
        bg=BG_COLOR,
    ).pack(pady=(32, 0))

    bar = tk.Frame(inner, bg=ACCENT_COLOR, height=3)
    bar.pack(side=tk.BOTTOM, fill=tk.X)


def main():
    root = tk.Tk()
    build_splash(root)

    def finish():
        try:
            launch_app()
        finally:
            root.destroy()

    root.after(SPLASH_DURATION_MS, finish)
    root.mainloop()


if __name__ == "__main__":
    main()
