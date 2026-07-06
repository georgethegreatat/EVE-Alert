"""Helper utilities for EVE Alert application."""

import os
import platform
import sys
import tempfile
from pathlib import Path

# Application metadata
APP_NAME = "EVE Alert"

# Path to application icon
ICON = "img/eve.ico"

# Absolute path to the evealert package root
PACKAGE_ROOT = Path(__file__).resolve().parent.parent

# Directory containing the running executable/script (writable location)
EXEC_ROOT = Path(sys.argv[0]).resolve().parent


def get_app_data_path() -> Path:
    """Return the per-user writable application data directory."""
    override_path = os.getenv("EVE_ALERT_CONFIG_DIR")
    if override_path:
        app_data_path = Path(override_path).expanduser()
        app_data_path.mkdir(parents=True, exist_ok=True)
        return app_data_path

    system = platform.system()

    if system == "Darwin":
        base_path = Path.home() / "Library" / "Application Support"
    elif system == "Windows":
        base_path = Path(os.getenv("APPDATA", Path.home() / "AppData" / "Roaming"))
    else:
        base_path = Path(os.getenv("XDG_CONFIG_HOME", Path.home() / ".config"))

    candidates = [
        base_path / APP_NAME,
        EXEC_ROOT / APP_NAME,
        Path(tempfile.gettempdir()) / APP_NAME,
    ]

    for app_data_path in candidates:
        try:
            app_data_path.mkdir(parents=True, exist_ok=True)
            write_check_path = app_data_path / ".write-test"
            write_check_path.touch(exist_ok=True)
            write_check_path.unlink(missing_ok=True)
            return app_data_path
        except OSError:
            continue

    raise OSError("Unable to create an application data directory")


def get_settings_path() -> Path:
    """Return the writable settings file path."""
    return get_app_data_path() / "settings.json"


def get_log_path() -> Path:
    """Return the writable log directory path."""
    log_path = get_app_data_path() / "logs"
    log_path.mkdir(parents=True, exist_ok=True)
    return log_path


def get_resource_path(relative_path: str) -> str:
    """Get the absolute path to a resource file.

    Reads bundled resources from PyInstaller's temporary/bundle directory when
    frozen, and from the package directory during development.

    Args:
        relative_path: Path like "sound/alarm.wav" or "img/icon.png"

    Returns:
        Absolute path to the resource file

    Example:
        >>> get_resource_path("sound/alarm.wav")
        '/path/to/evealert/sound/alarm.wav'
    """
    if not relative_path:
        raise ValueError("relative_path must be provided")

    relative = Path(relative_path)

    if relative.is_absolute():
        return str(relative)

    # PyInstaller one-file and one-folder builds expose bundled data here.
    if getattr(sys, "frozen", False):
        candidates = []
        if hasattr(sys, "_MEIPASS"):
            candidates.append(Path(sys._MEIPASS))  # pylint: disable=protected-access

        executable_dir = Path(sys.executable).resolve().parent
        candidates.extend(
            [
                executable_dir,
                executable_dir / "evealert",
                executable_dir.parent / "Resources",
                executable_dir.parent / "Resources" / "evealert",
            ]
        )

        for base_path in candidates:
            resource_path = (base_path / relative).resolve()
            if resource_path.exists():
                return str(resource_path)

        return str((candidates[0] / relative).resolve())

    # Development mode: strip 'evealert/' prefix and use PACKAGE_ROOT
    relative_stripped = relative
    if relative.parts and relative.parts[0].lower() == "evealert":
        relative_stripped = Path(*relative.parts[1:])

    resource_path = (PACKAGE_ROOT / relative_stripped).resolve()

    # Fallback to EXEC_ROOT if not found in PACKAGE_ROOT
    if not resource_path.exists():
        resource_path = (EXEC_ROOT / relative_stripped).resolve()

    return str(resource_path)
