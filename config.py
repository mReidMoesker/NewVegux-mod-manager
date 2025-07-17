from pathlib import Path

STEAM_COMPAT_ID = "22380"

#Directories (game, plugins)
FNV_DIR = Path.home() / "./steam/steam/steamapps/common/Fallout New Vegas"
DATA_DIR = FNV_DIR / "Data"

#Wine prefix
PLUGINS_TXT = Path.home() / f".steam/steam/steamapps/compatdata/{STEAM_COMPAT_ID}/pfx/drive_c/users/steamuser/Local Settings/Application Data/FalloutNV/plugins.txt"