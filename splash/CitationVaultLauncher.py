"""
CitationVault — splash screen + bundled app launcher.

When compiled with --add-binary, CitationVault.exe is embedded inside this
executable. On first run it copies the real app to LOCALAPPDATA so it
survives the PyInstaller temp-folder cleanup, then launches it detached.
"""

import os
import sys
import shutil
import subprocess
import threading
import tkinter as tk


SPLASH_DURATION_MS = 2500
REAL_EXE_NAME = "CitationVault_real.exe"
APP_DIR_NAME = "CitationVault"

BG_COLOR = "#0d1117"
ACCENT_COLOR = "#58a6ff"
TEXT_COLOR = "#e6edf3"
SUB_COLOR = "#8b949e"


def get_stable_app_path():
    """Copy the embedded exe to LOCALAPPDATA on first run; return its path."""
    local = os.environ.get("LOCALAPPDATA", os.path.expanduser("~"))
    target_dir = os.path.join(local, APP_DIR_NAME)
    target = os.path.join(target_dir, REAL_EXE_NAME)

    if getattr(sys, "frozen", False):
        source = os.path.join(sys._MEIPASS, REAL_EXE_NAME)
        os.makedirs(target_dir, exist_ok=True)
        if not os.path.exists(target) or os.path.getsize(target) != os.path.getsize(source):
            shutil.copy2(source, target)

    return target


def launch_app():
    app_path = get_stable_app_path()
    subprocess.Popen([app_path], creationflags=subprocess.DETACHED_PROCESS)


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

    def close_and_launch():
        root.after(SPLASH_DURATION_MS, lambda: (launch_app(), root.destroy()))

    threading.Thread(target=close_and_launch, daemon=True).start()
    root.mainloop()


if __name__ == "__main__":
    main()
