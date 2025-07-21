from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QMessageBox
)

from PyQt5.QtCore import Qt
from installer import install_mod

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NewVegux Mod Manager")
        self.setMinimumSize(500, 200)

        self.label = QLabel("Select an archive to install")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.install_button = QPushButton("Install Mod")
        self.install_button.clicked.connect(self.select_install)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.install_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def select_install(self):
        file_path, _ = QFileDialog.getOpenFileName(self,"Choose mod archive", "", "Zip files (.zip)")
        try:
            install_mod(file_path)
            QMessageBox.information(self, "Success", f"Installed mod from archive: \n{file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))