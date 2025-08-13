from pathlib import Path

def find_fallout_nv_path() -> Path | None:
    base = Path.home() / ".steam/steam/steamapps/compatdata"
    fallback_name = "Fallout New Vegas"

    # known App ID first
    nv_path = base / "22380/pfx/drive_c/Program Files (x86)/Steam/steamapps/common/Fallout New Vegas"
    if nv_path.exists():
        return nv_path

    # if the App ID is wrong scan compatdata folders (shouldn't need to be used unless user did something odd)
    for compat in base.glob("*/pfx/drive_c/Program Files (x86)/Steam/steamapps/common/*"):
        if compat.name.lower() == fallback_name.lower():
            return compat

    return None