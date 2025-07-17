import sys
from plugin_manager import read_plugins
from installer import install_mod

def print_usage():
    print("NewVegux Mod Manager")
    print("Usage:")
    print("  python nvmm.py list                ") #List plugins enabled
    print("  python nvmm.py install <mod.zip>   ") #Install mod archive

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    cmd = sys.argv[1]

    if cmd == "list":
        plugins = read_plugins()
        print("Enabled plugins:")
        for plugin in plugins:
            print("  -", plugin)

    elif cmd == "install" and len(sys.argv) == 3:
        zip_file = sys.argv[2]
        install_mod(zip_file)

    else:
        print_usage()

if __name__ == "__main__":
    main()
