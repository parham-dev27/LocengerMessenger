#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
import threading, socket

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 630)
        MainWindow.setMinimumSize(QtCore.QSize(450, 630))
        MainWindow.setMaximumSize(QtCore.QSize(450, 630))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -21, 451, 651))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.page)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 421, 91))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.ServerL_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.ServerL_2.setFont(font)
        self.ServerL_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ServerL_2.setObjectName("ServerL_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ServerL_2)
        self.PortL_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.PortL_2.setFont(font)
        self.PortL_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PortL_2.setObjectName("PortL_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.PortL_2)
        self.ServerE_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.ServerE_2.setFont(font)
        self.ServerE_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ServerE_2.setObjectName("ServerE_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ServerE_2)
        self.PortE_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.PortE_3.setFont(font)
        self.PortE_3.setAlignment(QtCore.Qt.AlignCenter)
        self.PortE_3.setObjectName("PortE_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.PortE_3)
        self.ChangelogL = QtWidgets.QLabel(self.page)
        self.ChangelogL.setGeometry(QtCore.QRect(10, 100, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.ChangelogL.setFont(font)
        self.ChangelogL.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ChangelogL.setObjectName("ChangelogL")
        self.listWidget = QtWidgets.QListWidget(self.page)
        self.listWidget.setGeometry(QtCore.QRect(10, 150, 431, 401))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("border: 2 solid black")
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setObjectName("listWidget")
        self.CloseB = QtWidgets.QPushButton(self.page)
        self.CloseB.setGeometry(QtCore.QRect(10, 560, 431, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(38)
        self.CloseB.setFont(font)
        self.CloseB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseB.setStyleSheet("background-color: rgb(211, 213, 213);")
        self.CloseB.setObjectName("CloseB")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(20, 30, 421, 121))
        font = QtGui.QFont()
        font.setFamily("Tamil MN")
        font.setPointSize(33)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(19, 159, 421, 96))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.ServerL = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.ServerL.setFont(font)
        self.ServerL.setAlignment(QtCore.Qt.AlignCenter)
        self.ServerL.setObjectName("ServerL")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ServerL)
        self.ServerE = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.ServerE.setFont(font)
        self.ServerE.setAlignment(QtCore.Qt.AlignCenter)
        self.ServerE.setObjectName("ServerE")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ServerE)
        self.PortL = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.PortL.setFont(font)
        self.PortL.setAlignment(QtCore.Qt.AlignCenter)
        self.PortL.setObjectName("PortL")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.PortL)
        self.ServerE_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.ServerE_3.setFont(font)
        self.ServerE_3.setAlignment(QtCore.Qt.AlignCenter)
        self.ServerE_3.setObjectName("ServerE_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ServerE_3)
        self.RunB = QtWidgets.QPushButton(self.page_2)
        self.RunB.setGeometry(QtCore.QRect(42, 470, 371, 121))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(38)
        self.RunB.setFont(font)
        self.RunB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RunB.setStyleSheet("background-color: rgb(211, 213, 213);")
        self.RunB.setObjectName("RunB")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.RunB.clicked.connect(self.runServerB)
        self.ServerE.setText(str(self.returnServerIpv4()))
        self.SERVER = self.returnServerIpv4()
        self.PORT = 5050
        self.CLIENTS = []
        self.NICKNAMES = []
        self.CloseB.clicked.connect(self.closeSERVER)

    def closeSERVER(self):
        raise ValueError
            
    

    def broadcast(self, msg):
        for client in self.CLIENTS:
            client.send(msg)


    def returnServerIpv4(self):
        return socket.gethostbyname(socket.gethostname())

    def handle_cleint(self, client):
        connected = True
        while connected:
            try:
                msg = client.recv(2048)
                self.broadcast(msg)
            except:
                index = self.CLIENTS.index(client)
                self.CLIENTS.remove(client)
                client.close
                nickname = self.NICKNAMES[index]
                self.listWidget.addItem(f'[CLIENT] {nickname} left')
                self.broadcast(f"{nickname} left the chat".encode('ascii'))
                self.NICKNAMES.remove(nickname)
                break

    def runServerF(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.SERVER, self.PORT))
        self.server.listen()
        self.listWidget.addItem(f"[SERVER] Server listening...")
        while True:
            client, addr = self.server.accept()
            client.send("@NICK".encode('ascii'))
            nickname = client.recv(2048).decode('ascii')
            self.listWidget.addItem(f'[NEW CLIENT] Address: {addr} | Name: {nickname}')
            self.NICKNAMES.append(nickname)
            self.CLIENTS.append(client)
            self.broadcast(f"{nickname} joined the chat".encode('ascii'))
            thread = threading.Thread(target=self.handle_cleint, args=(client,))
            thread.start()

    def runServerB(self):
        thread2 = threading.Thread(target=self.runServerF)
        thread2.start()
        self.PortE_3.setText(str(self.PORT))
        self.ServerE_2.setText(str(self.SERVER))
        self.stackedWidget.setCurrentIndex(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Locenger Server Hosting"))
        self.ServerL_2.setText(_translate("MainWindow", "Server:"))
        self.PortL_2.setText(_translate("MainWindow", "Port:"))
        self.ServerE_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Server Ip Address</p></body></html>"))
        self.ServerE_2.setText(_translate("MainWindow", "127.0.0.1"))
        self.PortE_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Port Address</p></body></html>"))
        self.PortE_3.setText(_translate("MainWindow", "127.0.0.1"))
        self.ChangelogL.setText(_translate("MainWindow", "Changelog:"))
        self.CloseB.setToolTip(_translate("MainWindow", "<html><head/><body><p>Close The Current Running Server</p></body></html>"))
        self.CloseB.setText(_translate("MainWindow", "Close Server"))
        self.label.setText(_translate("MainWindow", "Lokenger Server Hosting"))
        self.ServerL.setText(_translate("MainWindow", "Server:"))
        self.ServerE.setToolTip(_translate("MainWindow", "<html><head/><body><p>Server Ip Address</p></body></html>"))
        self.ServerE.setText(_translate("MainWindow", "127.0.0.1"))
        self.PortL.setText(_translate("MainWindow", "Port:"))
        self.ServerE_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Server Ip Address</p></body></html>"))
        self.ServerE_3.setText(_translate("MainWindow", "5050"))
        self.RunB.setToolTip(_translate("MainWindow", "<html><head/><body><p>Run Lokenger Server</p></body></html>"))
        self.RunB.setText(_translate("MainWindow", "Run Server"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())