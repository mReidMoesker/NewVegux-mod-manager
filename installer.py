import zipfile
from pathlib import Path
from config import DATA_DIR
from plugin_manager import add_plugin
from bsa_extract import FalloutNVBSA

#Import bsa files
def extrac_bsa(bsa_path: Path, output_dir: Path):
    try: 
        extractor = FalloutNVBSA(str(bsa_path))
        extractor.extract_all(output_dir)
        print(f"[OK] Extracted BSA: {bsa_path.name}")
    except Exception as e:
        print(f"[ERROR] BSA Extraction failed at {bsa_path.name}: {e}")

#mod installation
def install_mod(zip_path):
    zip_path = Path(zip_path)
    if not zip_path.exists():
        print(f"[ERROR] Mod archive not found: {zip_path}")
        return

    with zipfile.ZipFile(zip_path, 'r') as archive:
        bsa_files = []
        esp_files = []

        for file in archive.namelist():
            lower = file.lower()
            if file.lower().endswith(('.esp', '.esm')):
                esp_files.append(Path(file).name)
            elif lower.endswith('.bsa'):
                bsa_files.append(Path(file).name)

        archive.extractall(DATA_DIR)
        print(f"[OK] Extracted '{zip_path.name}' to Data folder.")

        for esp in esp_files:
            add_plugin(esp)

        for bsa in bsa_files:
            base = bsa[:-4].lower()
            if not any(esp.lower().startswith(base) for esp in esp_files): #checks for matching esp files for bsa files installed
                print(f"[WARNING] BSA '{bsa}' has no matching plugin. This could prevent the mod from loading in-game.")
            else:
                print(f"[OK] BSA '{bsa}' sucessfully paired with matching plugin.")
            
            #bsa extraction to bsa mod folder
            bsa_path = DATA_DIR / bsa
            output_dir = DATA_DIR / (bsa_path.stem + "_extracted")

            if bsa_path.exists():
                extrac_bsa(bsa_path, output_dir)
            else:
                print(f"[ERROR] BSA file missing after extraction at {bsa_path}")