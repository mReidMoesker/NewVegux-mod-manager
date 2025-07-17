from config import PLUGINS_TXT

def read_plugins():
    if not PLUGINS_TXT.exists():
        return []

    with PLUGINS_TXT.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

def add_plugin(plugin_name):
    plugins = read_plugins()

    if plugin_name.lower() in [p.lower() for p in plugins]:
        print(f"[INFO] Plugin '{plugin_name}' already in load order.")
        return

    with PLUGINS_TXT.open("a", encoding="utf-8") as f:
        f.write(f"{plugin_name}\n")
        print(f"[OK] Plugin '{plugin_name}' added to load order.")