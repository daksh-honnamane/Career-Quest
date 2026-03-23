import os
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = PROJECT_ROOT / "source"
APP_NAME = "Career Quest"


def _bundle_root():
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return PROJECT_ROOT


def source_path(*parts):
    return _bundle_root() / "source" / Path(*parts)


def asset_path(*parts):
    return source_path("assets", *parts)


def save_file_path():
    if getattr(sys, "frozen", False):
        appdata_root = Path(os.getenv("APPDATA", Path.home() / "AppData" / "Roaming"))
        return appdata_root / APP_NAME / "save_data.json"
    return SOURCE_ROOT / "save_data.json"