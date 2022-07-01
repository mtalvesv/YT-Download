from PyQt5 import QtWidgets
import sys

import download
from interface import Ui_MainWindow
from download import *


if __name__ == '__main__':
    d = download.Download()
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Principal)
    Principal.show()
    ui.btn_mp4.clicked.connect(lambda: d.playlist(ui.plainTextEdit.toPlainText()))
    ui.btn_mp3.clicked.connect(lambda: d.playlist(ui.plainTextEdit.toPlainText(), True, ui.check_apagarMp4.isChecked()))
    sys.exit(app.exec_())
