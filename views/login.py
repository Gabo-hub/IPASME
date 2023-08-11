# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from views.resources_rc import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.NonModal)
        Dialog.resize(340, 318)
        icon = QIcon()
        icon.addFile(u":/logo_ipasme/icons/IPASME-logo-DABC2AE9B1-seeklogo.com.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.ql_Login_usuariotext = QLabel(Dialog)
        self.ql_Login_usuariotext.setObjectName(u"ql_Login_usuariotext")
        self.ql_Login_usuariotext.setGeometry(QRect(60, 100, 51, 16))
        font = QFont()
        font.setFamily(u"Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ql_Login_usuariotext.setFont(font)
        self.ql_Login_usuarioinfo = QLineEdit(Dialog)
        self.ql_Login_usuarioinfo.setObjectName(u"ql_Login_usuarioinfo")
        self.ql_Login_usuarioinfo.setGeometry(QRect(60, 120, 231, 31))
        self.ql_Login_usuarioinfo.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid  rgb(122, 122, 122);\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding-left: 25px;\n"
"	padding-right: 20px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(41,50,62);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85,170,255);	\n"
"}")
        self.ql_Login_contrasenainfo = QLineEdit(Dialog)
        self.ql_Login_contrasenainfo.setObjectName(u"ql_Login_contrasenainfo")
        self.ql_Login_contrasenainfo.setGeometry(QRect(60, 190, 231, 31))
        self.ql_Login_contrasenainfo.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ql_Login_contrasenainfo.setLayoutDirection(Qt.LeftToRight)
        self.ql_Login_contrasenainfo.setAutoFillBackground(False)
        self.ql_Login_contrasenainfo.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid  rgb(122, 122, 122);\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding-left: 25px;\n"
"	padding-right: 20px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(41,50,62);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85,170,255);	\n"
"}")
        self.ql_Login_contrasenainfo.setMaxLength(20)
        self.ql_Login_contrasenainfo.setEchoMode(QLineEdit.Password)
        self.ql_Login_contrasenainfo.setCursorPosition(0)
        self.ql_Login_contrasenainfo.setDragEnabled(False)
        self.ql_Login_contrasenainfo.setReadOnly(False)
        self.ql_Login_contrasenainfo.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.ql_Login_contrasenainfo.setClearButtonEnabled(False)
        self.ql_Login_contrasenatext = QLabel(Dialog)
        self.ql_Login_contrasenatext.setObjectName(u"ql_Login_contrasenatext")
        self.ql_Login_contrasenatext.setGeometry(QRect(60, 160, 81, 20))
        self.ql_Login_contrasenatext.setFont(font)


        self.bttn_Login_Ingresar = QPushButton(Dialog)
        self.bttn_Login_Ingresar.setObjectName(u"bttn_Login_Ingresar")
        self.bttn_Login_Ingresar.setGeometry(QRect(60, 240, 101, 31))
        self.bttn_Login_Ingresar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Login_Ingresar.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.bttn_Login_cerrar = QPushButton(Dialog)
        self.bttn_Login_cerrar.setObjectName(u"bttn_Login_cerrar")
        self.bttn_Login_cerrar.setGeometry(QRect(190, 240, 101, 31))
        self.bttn_Login_cerrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Login_cerrar.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -1, 401, 81))
        self.frame.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(53, 131, 173);")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.ql_Login_titulo = QLabel(self.frame)
        self.ql_Login_titulo.setObjectName(u"ql_Login_titulo")
        self.ql_Login_titulo.setGeometry(QRect(100, 10, 181, 41))
        font1 = QFont()
        font1.setFamily(u"Poppins")
        font1.setPointSize(36)
        font1.setBold(True)
        font1.setWeight(75)
        self.ql_Login_titulo.setFont(font1)
        self.ql_Login_titulo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ql_Login_titulo.setScaledContents(True)
        self.ql_Login_titulo.setWordWrap(True)
        self.ql_Login_titulo.setOpenExternalLinks(True)
        self.ql_Login_logotitulo = QLabel(self.frame)
        self.ql_Login_logotitulo.setObjectName(u"ql_Login_logotitulo")
        self.ql_Login_logotitulo.setGeometry(QRect(20, 10, 61, 61))
        self.ql_Login_logotitulo.setPixmap(QPixmap(u":/logo_ipasme/icons/IPASME-logo-DABC2AE9B1-seeklogo.com.png"))
        self.ql_Login_logotitulo.setScaledContents(True)
        self.ql_Login_subtitulo = QLabel(self.frame)
        self.ql_Login_subtitulo.setObjectName(u"ql_Login_subtitulo")
        self.ql_Login_subtitulo.setGeometry(QRect(110, 50, 171, 21))
        font2 = QFont()
        font2.setFamily(u"Poppins")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.ql_Login_subtitulo.setFont(font2)
        self.ql_Login_subtitulo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.bttn_Login_close = QPushButton(self.frame)
        self.bttn_Login_close.setObjectName(u"bttn_Login_close")
        self.bttn_Login_close.setGeometry(QRect(306, 11, 24, 24))
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/cerrar-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bttn_Login_close.setIcon(icon1)
        self.bttn_Login_close.setIconSize(QSize(32, 32))
        self.bttn_Login_close.setFlat(True)
        self.bttn_Login_MostrarContra = QPushButton(Dialog)
        self.bttn_Login_MostrarContra.setObjectName(u"bttn_Login_MostrarContra")
        self.bttn_Login_MostrarContra.setGeometry(QRect(66, 194, 21, 23))
        self.bttn_Login_MostrarContra.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Login_MostrarContra.setStyleSheet(u"")
        self.bttn_Login_MostrarContra.setInputMethodHints(Qt.ImhNone)
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/descarga.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bttn_Login_MostrarContra.setIcon(icon2)
        self.bttn_Login_MostrarContra.setIconSize(QSize(25, 25))
        self.bttn_Login_MostrarContra.setCheckable(True)
        self.bttn_Login_MostrarContra.setChecked(False)
        self.bttn_Login_MostrarContra.setAutoRepeat(False)
        self.bttn_Login_MostrarContra.setFlat(True)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QRect(66, 125, 20, 21))
        self.pushButton.setStyleSheet(u"")
        self.pushButton.setInputMethodHints(Qt.ImhNone)
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/person.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(25, 25))
        self.pushButton.setFlat(True)
        QWidget.setTabOrder(self.ql_Login_usuarioinfo, self.ql_Login_contrasenainfo)
        QWidget.setTabOrder(self.ql_Login_contrasenainfo, self.bttn_Login_Ingresar)
        QWidget.setTabOrder(self.bttn_Login_Ingresar, self.bttn_Login_cerrar)

        self.retranslateUi(Dialog)
        self.bttn_Login_cerrar.clicked.connect(Dialog.close)
        self.bttn_Login_close.clicked.connect(Dialog.close)

        self.bttn_Login_MostrarContra.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.ql_Login_usuariotext.setText(QCoreApplication.translate("Dialog", u"Usuario", None))


        self.ql_Login_usuarioinfo.setText("Admin")
        self.ql_Login_contrasenainfo.setText("superadmin")



        self.ql_Login_contrasenatext.setText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a", None))
        self.bttn_Login_Ingresar.setText(QCoreApplication.translate("Dialog", u"Ingresar", None))
        self.bttn_Login_cerrar.setText(QCoreApplication.translate("Dialog", u"Cerrar", None))
        self.ql_Login_titulo.setText(QCoreApplication.translate("Dialog", u"IPASME", None))
        self.ql_Login_logotitulo.setText("")
        self.ql_Login_subtitulo.setText(QCoreApplication.translate("Dialog", u"Ventana de ingreso", None))
        self.bttn_Login_close.setText("")
        self.bttn_Login_MostrarContra.setText("")
        self.pushButton.setText("")
    # retranslateUi

