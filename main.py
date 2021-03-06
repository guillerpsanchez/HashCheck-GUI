from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QFormLayout, QWidget, QApplication
from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from pass_lib import passme_password
import sys
import ctypes
import resources

ID = u'dev.guillerpsanchez.HashCheck-GUI'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(ID)


class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(500, 130)
        self.setWindowTitle("HasCheck-GUI")

        self.response = QLabel(self)
        self.response.setText("")

        self.send_pass = QPushButton(self)
        self.send_pass.setText("Send")
        self.send_pass.clicked.connect(self.check_password)

        self.inputBox = QLineEdit(self)

        layout = QFormLayout()
        layout.addWidget(self.response)
        layout.addWidget(self.inputBox)
        layout.addWidget(self.send_pass)

        self.setLayout(layout)
        self.show()

    def check_password(self):
        password = self.inputBox.text()
        if passme_password(password) == "F":
            self.response.setText("Your password has been filtered.")
        else:
            self.response.setText("Your password has not been filtered yet.")


def main():
    app = QApplication(sys.argv)
    a = App()
    app.setWindowIcon(QtGui.QIcon(':/icons/icon.png'))
    a.show()
    sys.exit(app.exec())


if __name__ == "__main__":
        main()
