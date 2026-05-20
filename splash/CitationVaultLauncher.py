"""
CitationVault splash screen launcher.
Shows a branded splash for ~2.5 s then launches CitationVault.exe
from the same directory.

Build (on Windows, with PyInstaller installed):
    pyinstaller CitationVaultLauncher.spec
"""

import os
import sys
import subprocess
import threading
import tkinter as tk


SPLASH_DURATION_MS = 2500
EXE_NAME = "CitationVault.exe"

BG_COLOR = "#0d1117"
ACCENT_COLOR = "#58a6ff"
TEXT_COLOR = "#e6edf3"
SUB_COLOR = "#8b949e"


def get_exe_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def launch_app():
    exe_path = os.path.join(get_exe_dir(), EXE_NAME)
    subprocess.Popen([exe_path], creationflags=subprocess.DETACHED_PROCESS)


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

    # Outer border frame
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

    # Thin accent bar at the bottom
    bar = tk.Frame(inner, bg=ACCENT_COLOR, height=3)
    bar.pack(side=tk.BOTTOM, fill=tk.X)


def main():
    root = tk.Tk()
    build_splash(root)

    # Launch the real app after the splash has been visible
    def close_and_launch():
        root.after(SPLASH_DURATION_MS, lambda: (launch_app(), root.destroy()))

    threading.Thread(target=close_and_launch, daemon=True).start()
    root.mainloop()


if __name__ == "__main__":
    main()
