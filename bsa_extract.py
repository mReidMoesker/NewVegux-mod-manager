import os
import struct
from pathlib import Path

class FalloutNVBSA:
    def __init__(self, filepath):
        self.filepath = filepath
        self.folders = []
        self.files = []

    def read_header(self, f):
        f.seek(0)
        magic = f.read(4)
        if magic != b'BSA\x00':
            raise Exception("Not a valid BSA file (bad magic)")
        (self.version,) = struct.unpack('<I', f.read(4))
        if self.version != 103:
            raise Exception(f"Unsupported BSA version {self.version}, expected 103")
        # Skip unknown ints we don't need right now
        f.read(12)  # header size, folder count, file count
        self.folder_count, self.file_count = struct.unpack('<III', f.read(12))

    def read_folders(self, f):
        self.folders = []
        for _ in range(self.folder_count):
            folder_name_len = struct.unpack('<I', f.read(4))[0]
            folder_name = f.read(folder_name_len).decode('utf-8').rstrip('\x00')
            file_count = struct.unpack('<I', f.read(4))[0]
            folder_files = []
            for _ in range(file_count):
                file_name_len = struct.unpack('<I', f.read(4))[0]
                file_name = f.read(file_name_len).decode('utf-8').rstrip('\x00')
                file_size = struct.unpack('<I', f.read(4))[0]
                file_offset = struct.unpack('<I', f.read(4))[0]
                folder_files.append({
                    'name': file_name,
                    'size': file_size,
                    'offset': file_offset
                })
            self.folders.append({
                'name': folder_name,
                'files': folder_files
            })

    def extract_all(self, output_dir):
        output_dir = Path(output_dir)
        with open(self.filepath, 'rb') as f:
            self.read_header(f)
            self.read_folders(f)

            for folder in self.folders:
                folder_path = output_dir / folder['name']
                folder_path.mkdir(parents=True, exist_ok=True)

                for file in folder['files']:
                    f.seek(file['offset'])
                    data = f.read(file['size'])

                    out_file = folder_path / file['name']
                    with open(out_file, 'wb') as out_f:
                        out_f.write(data)

                    print(f"Extracted: {out_file}")