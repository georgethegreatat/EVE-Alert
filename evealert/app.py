"""Application entry point for EVE Alert."""

import customtkinter

from evealert import __version__
from evealert.menu.main import MainMenu


def run() -> None:
    """Start the EVE Alert desktop application."""
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    print(f"Geuthur - EVE Alert v{__version__}")

    app = MainMenu()
    app.mainloop()
