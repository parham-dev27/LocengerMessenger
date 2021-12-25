#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
import threading, socket
from random import randint as randomNumber


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(479, 680)
        MainWindow.setMinimumSize(QtCore.QSize(479, 680))
        MainWindow.setMaximumSize(QtCore.QSize(479, 680))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(479, 680))
        self.centralwidget.setMaximumSize(QtCore.QSize(479, 680))
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-11, -21, 501, 711))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(20, 30, 471, 121))
        font = QtGui.QFont()
        font.setFamily("Tamil MN")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.nameL = QtWidgets.QLabel(self.page)
        self.nameL.setGeometry(QtCore.QRect(20, 190, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.nameL.setFont(font)
        self.nameL.setToolTip("")
        self.nameL.setAlignment(QtCore.Qt.AlignCenter)
        self.nameL.setObjectName("nameL")
        self.nameE = QtWidgets.QLineEdit(self.page)
        self.nameE.setGeometry(QtCore.QRect(50, 270, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(25)
        self.nameE.setFont(font)
        self.nameE.setStyleSheet("border: 2px dashed black;")
        self.nameE.setText("")
        self.nameE.setMaxLength(15)
        self.nameE.setClearButtonEnabled(False)
        self.nameE.setObjectName("nameE")
        self.StartB = QtWidgets.QPushButton(self.page)
        self.StartB.setGeometry(QtCore.QRect(70, 480, 371, 121))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(38)
        self.StartB.setFont(font)
        self.StartB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartB.setStyleSheet("background-color: rgb(211, 213, 213);")
        self.StartB.setObjectName("StartB")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.ipL = QtWidgets.QLabel(self.page_2)
        self.ipL.setGeometry(QtCore.QRect(20, 170, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.ipL.setFont(font)
        self.ipL.setAlignment(QtCore.Qt.AlignCenter)
        self.ipL.setObjectName("ipL")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 471, 121))
        font = QtGui.QFont()
        font.setFamily("Tamil MN")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ipE = QtWidgets.QLineEdit(self.page_2)
        self.ipE.setGeometry(QtCore.QRect(50, 230, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(25)
        self.ipE.setFont(font)
        self.ipE.setStyleSheet("border: 2px dashed black;")
        self.ipE.setText("")
        self.ipE.setMaxLength(15)
        self.ipE.setObjectName("ipE")
        self.joinB = QtWidgets.QPushButton(self.page_2)
        self.joinB.setGeometry(QtCore.QRect(70, 490, 371, 121))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(38)
        self.joinB.setFont(font)
        self.joinB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.joinB.setStyleSheet("background-color: rgb(211, 213, 213);")
        self.joinB.setObjectName("joinB")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 471, 101))
        font = QtGui.QFont()
        font.setFamily("Tamil MN")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.listWidget = QtWidgets.QListWidget(self.page_3)
        self.listWidget.setGeometry(QtCore.QRect(30, 120, 451, 371))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(19)
        self.listWidget.setFont(font)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet("border: 2px solid black;")
        self.listWidget.setAutoScroll(True)
        self.listWidget.setAutoScrollMargin(16)
        self.listWidget.setTabKeyNavigation(False)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setDragDropOverwriteMode(False)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        self.textE = QtWidgets.QLineEdit(self.page_3)
        self.textE.setGeometry(QtCore.QRect(40, 510, 431, 81))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        self.textE.setFont(font)
        self.textE.setStyleSheet("border: 2px dashed black;")
        self.textE.setFrame(True)
        self.textE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.textE.setDragEnabled(False)
        self.textE.setClearButtonEnabled(True)
        self.textE.setObjectName("textE")
        self.sendB = QtWidgets.QPushButton(self.page_3)
        self.sendB.setGeometry(QtCore.QRect(110, 600, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(38)
        self.sendB.setFont(font)
        self.sendB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendB.setStyleSheet("background-color: rgb(211, 213, 213);")
        self.sendB.setObjectName("sendB")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 471, 101))
        font = QtGui.QFont()
        font.setFamily("Tamil MN")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.errorL = QtWidgets.QLabel(self.page_4)
        self.errorL.setGeometry(QtCore.QRect(10, 190, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.errorL.setFont(font)
        self.errorL.setAlignment(QtCore.Qt.AlignCenter)
        self.errorL.setObjectName("errorL")
        self.errorL2 = QtWidgets.QLabel(self.page_4)
        self.errorL2.setGeometry(QtCore.QRect(20, 280, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.errorL2.setFont(font)
        self.errorL2.setAlignment(QtCore.Qt.AlignCenter)
        self.errorL2.setObjectName("errorL2")
        self.gobackB = QtWidgets.QPushButton(self.page_4)
        self.gobackB.setGeometry(QtCore.QRect(70, 460, 371, 121))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(38)
        self.gobackB.setFont(font)
        self.gobackB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gobackB.setStyleSheet("background-color: rgb(211, 213, 213);")
        self.gobackB.setObjectName("gobackB")
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.textE.setMaxLength(2048)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.StartB.clicked.connect(self.getNickname)
        self.joinB.clicked.connect(self.getServerIPv4)
        self.sendB.clicked.connect(self.write)
        self.gobackB.clicked.connect(self.goBackF)

        self.NICKNAME = ""
        self.SERVER = ""
        self.PORT = 5050

    def goBackF(self):
        self.stackedWidget.setCurrentIndex(1)

    def receive(self):
        while True:
            try:
                msg = self.client.recv(2048).decode('ascii')
                if msg == "@NICK":
                    self.client.send(self.NICKNAME.encode('ascii'))
                else:
                    self.listWidget.addItem(f"{msg}")
            except:
                self.stackedWidget.setCurrentIndex(3)
                self.client.close()
                break            

    def write(self):
        msg = self.textE.text()
        if msg == "":
            pass
        else:
            try:
                msg = f'{self.NICKNAME}: {msg}'
                self.client.send(msg.encode('ascii'))
                self.textE.setText("")
            except:
                self.stackedWidget.setCurrentIndex(3)


    def makeConnection(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.SERVER, self.PORT))
            rec_thread = threading.Thread(target=self.receive, daemon=True)
            rec_thread.start()
        except:
            self.stackedWidget.setCurrentIndex(3)

    def getNickname(self):
        name = str(self.nameE.text())
        try:
            if " " in name:
                name = name.replace(" ", "")
                if name == "":
                    raise ValueError
                else:
                    self.NICKNAME = name
            elif name == "":
                raise ValueError
            else:
                self.NICKNAME = name 
        except:
            self.NICKNAME = "NoName" + str(randomNumber(0, 9)) + str(randomNumber(0, 9)) + str(randomNumber(0, 9)) + str(randomNumber(0, 9)) + str(randomNumber(0, 9))
        self.stackedWidget.setCurrentIndex(1)


    def getServerIPv4(self):
        IPv4 = self.ipE.text()
        try:
            if " " in IPv4:
                IPv4 = IPv4.replace(" ", "")
                if IPv4 == "":
                    raise ValueError
                else:
                    self.SERVER = IPv4
            elif IPv4 == "":
                raise ValueError
            else:
                self.SERVER = IPv4
            self.stackedWidget.setCurrentIndex(2)
            try:
                conThread = threading.Thread(target=self.makeConnection, daemon=True)
                conThread.start()
                self.stackedWidget.setCurrentIndex(2)
            except:
                self.stackedWidget.setCurrentIndex(3)
        except:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Locenger"))
        self.label.setText(_translate("MainWindow", "Lokenger"))
        self.nameL.setText(_translate("MainWindow", "Enter Your Name:"))
        self.nameE.setToolTip(_translate("MainWindow", "<html><head/><body><p>Nickname</p></body></html>"))
        self.nameE.setPlaceholderText(_translate("MainWindow", "NAME"))
        self.StartB.setToolTip(_translate("MainWindow", "<html><head/><body><p>Start</p></body></html>"))
        self.StartB.setText(_translate("MainWindow", "Start"))
        self.ipL.setText(_translate("MainWindow", "Server IP:"))
        self.label_2.setText(_translate("MainWindow", "Lokenger"))
        self.ipE.setToolTip(_translate("MainWindow", "<html><head/><body><p>Server IPv4</p></body></html>"))
        self.ipE.setPlaceholderText(_translate("MainWindow", "127.0.0.1"))
        self.joinB.setToolTip(_translate("MainWindow", "<html><head/><body><p>Join Chat</p></body></html>"))
        self.joinB.setText(_translate("MainWindow", "Join Chat"))
        self.label_3.setText(_translate("MainWindow", "Lokenger"))
        self.listWidget.setSortingEnabled(False)
        self.textE.setToolTip(_translate("MainWindow", "<html><head/><body><p>Message Box</p></body></html>"))
        self.textE.setText(_translate("MainWindow", ""))
        self.textE.setPlaceholderText(_translate("MainWindow", "Text"))
        self.sendB.setToolTip(_translate("MainWindow", "<html><head/><body><p>Send Message</p></body></html>"))
        self.sendB.setText(_translate("MainWindow", "Send"))
        self.label_4.setText(_translate("MainWindow", "Lokenger"))
        self.errorL.setText(_translate("MainWindow", "Error"))
        self.errorL2.setText(_translate("MainWindow", "Could Not Connect To The Server"))
        self.gobackB.setToolTip(_translate("MainWindow", "<html><head/><body><p>Run Lokenger Server</p></body></html>"))
        self.gobackB.setText(_translate("MainWindow", "Go Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
