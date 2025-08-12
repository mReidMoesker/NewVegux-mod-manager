import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
from locate_install_path import find_fallout_nv_path


if __name__ == "__main__":
	nv_path = find_fallout_nv_path()
	if nv_path:
		print(f"[INFO] Fallout New Vegas install path detected: {nv_path}")
	else:
		print("[WARN] Fallout New Vegas install path not found.")

	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())