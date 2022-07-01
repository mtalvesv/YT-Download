from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.princial = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.princial.sizePolicy().hasHeightForWidth())

        self.princial.setSizePolicy(sizePolicy)
        self.princial.setMinimumSize(QtCore.QSize(400, 400))
        self.princial.setMaximumSize(QtCore.QSize(500, 500))
        self.princial.setObjectName("princial")

        self.label = QtWidgets.QLabel(self.princial)
        self.label.setGeometry(QtCore.QRect(30, 160, 55, 18))
        self.label.setObjectName("label")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.princial)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 150, 291, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.btn_sair = QtWidgets.QPushButton(self.princial)
        self.btn_sair.setGeometry(QtCore.QRect(160, 280, 84, 34))
        self.btn_sair.setObjectName("btn_sair")
        self.btn_mp4 = QtWidgets.QPushButton(self.princial)
        self.btn_mp4.setGeometry(QtCore.QRect(70, 280, 84, 34))
        self.btn_mp4.setObjectName("btn_mp4")

        self.btn_mp3 = QtWidgets.QPushButton(self.princial)
        self.btn_mp3.setGeometry(QtCore.QRect(250, 280, 84, 34))
        self.btn_mp3.setObjectName("btn_mp3")

        self.check_apagarMp4 = QtWidgets.QCheckBox(self.princial)
        self.check_apagarMp4.setEnabled(True)
        self.check_apagarMp4.setGeometry(QtCore.QRect(140, 220, 101, 22))
        self.check_apagarMp4.setObjectName("check_apagarMp4")

        MainWindow.setCentralWidget(self.princial)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yt Download"))
        self.label.setText(_translate("MainWindow", "URL"))
        self.btn_sair.setText(_translate("MainWindow", "Sair"))
        self.btn_mp4.setText(_translate("MainWindow", "MP4"))
        self.btn_mp3.setText(_translate("MainWindow", "MP3"))
        self.check_apagarMp4.setText(_translate("MainWindow", "Apagar MP4"))

