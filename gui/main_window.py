from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QMessageBox, QListWidget
)

from PyQt5.QtCore import Qt

from installer import install_mod
from plugin_manager import read_plugins

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NewVegux Mod Manager")
        self.setMinimumSize(500, 200)


    self.label = QLabel("Select an archive to install")
    self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.install_button = QPushButton("Install Mod")
    self.install_button.clicked.connect(self.select_install)

    self.mods_list = QListWidget()
    self.mods_list.setMinimumHeight(100)
    self.mods_list.setSelectionMode(QListWidget.NoSelection)
    self.mods_list.setFocusPolicy(Qt.NoFocus)
    self.mods_list.setAlternatingRowColors(True)
    self.mods_list.setSortingEnabled(True)

    layout = QVBoxLayout()
    layout.addWidget(self.label)
    layout.addWidget(self.install_button)
    layout.addWidget(QLabel("Active Mods:"))
    layout.addWidget(self.mods_list)

    container = QWidget()
    container.setLayout(layout)
    self.setCentralWidget(container)

    self.refresh_mods_list()


    def select_install(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose mod archive", "", "Zip files (.zip)")
        try:
            install_mod(file_path)
            QMessageBox.information(self, "Success", f"Installed mod from archive: \n{file_path}")
            self.refresh_mods_list()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def refresh_mods_list(self):
        self.mods_list.clear()
        mods = read_plugins()
        if mods:
            self.mods_list.addItems(mods)
        else:
            self.mods_list.addItem("No active mods found.")