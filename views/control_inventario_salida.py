# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'control_inventario_salida.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from views.resources_rc import *

class Ui_ContrlSalida(object):
    def setupUi(self, ContrlSalida):
        if not ContrlSalida.objectName():
            ContrlSalida.setObjectName(u"ContrlSalida")
        ContrlSalida.setWindowModality(Qt.WindowModal)
        ContrlSalida.resize(634, 535)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ContrlSalida.sizePolicy().hasHeightForWidth())
        ContrlSalida.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/logo_ipasme/icons/IPASME-logo-DABC2AE9B1-seeklogo.com.png", QSize(), QIcon.Normal, QIcon.Off)
        ContrlSalida.setWindowIcon(icon)
        ContrlSalida.setStyleSheet(u"background-color: rgb(177, 214, 166);")
        self.verticalLayout = QVBoxLayout(ContrlSalida)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ql_CtrlSalida_Titulo = QLabel(ContrlSalida)
        self.ql_CtrlSalida_Titulo.setObjectName(u"ql_CtrlSalida_Titulo")

        self.verticalLayout.addWidget(self.ql_CtrlSalida_Titulo)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ql_CtrlSalida_numeroactivo = QLabel(ContrlSalida)
        self.ql_CtrlSalida_numeroactivo.setObjectName(u"ql_CtrlSalida_numeroactivo")

        self.gridLayout_2.addWidget(self.ql_CtrlSalida_numeroactivo, 0, 4, 1, 1)

        self.bttn_CtrlSalida_numeroactivo = QPushButton(ContrlSalida)
        self.bttn_CtrlSalida_numeroactivo.setObjectName(u"bttn_CtrlSalida_numeroactivo")
        self.bttn_CtrlSalida_numeroactivo.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_CtrlSalida_numeroactivo.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	\n"
"	background-color: rgb(195, 221, 248);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"	   	background-color: rgb(165, 188, 211);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/botones_ipasme/icons/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bttn_CtrlSalida_numeroactivo.setIcon(icon1)
        self.bttn_CtrlSalida_numeroactivo.setIconSize(QSize(16, 16))
        self.bttn_CtrlSalida_numeroactivo.setFlat(True)

        self.gridLayout_2.addWidget(self.bttn_CtrlSalida_numeroactivo, 0, 2, 1, 1)

        self.bttn_CtrlSalida_nombreactivo = QPushButton(ContrlSalida)
        self.bttn_CtrlSalida_nombreactivo.setObjectName(u"bttn_CtrlSalida_nombreactivo")
        self.bttn_CtrlSalida_nombreactivo.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_CtrlSalida_nombreactivo.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	\n"
"	background-color: rgb(195, 221, 248);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"	   	background-color: rgb(165, 188, 211);\n"
"}\n"
"")
        self.bttn_CtrlSalida_nombreactivo.setIcon(icon1)
        self.bttn_CtrlSalida_nombreactivo.setIconSize(QSize(16, 16))
        self.bttn_CtrlSalida_nombreactivo.setFlat(True)

        self.gridLayout_2.addWidget(self.bttn_CtrlSalida_nombreactivo, 0, 5, 1, 1)

        self.ql_CtrlSalida_nombreactivo = QLabel(ContrlSalida)
        self.ql_CtrlSalida_nombreactivo.setObjectName(u"ql_CtrlSalida_nombreactivo")

        self.gridLayout_2.addWidget(self.ql_CtrlSalida_nombreactivo, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 6, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.line_2 = QFrame(ContrlSalida)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(149, 170, 190);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.BodyFrame = QFrame(ContrlSalida)
        self.BodyFrame.setObjectName(u"BodyFrame")
        self.BodyFrame.setEnabled(False)
        self.BodyFrame.setFrameShape(QFrame.StyledPanel)
        self.BodyFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.BodyFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.ql_CtrlSalida_tipo = QLabel(self.BodyFrame)
        self.ql_CtrlSalida_tipo.setObjectName(u"ql_CtrlSalida_tipo")
        self.ql_CtrlSalida_tipo.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.ql_CtrlSalida_tipo, 1, 0, 1, 1)

        self.cbox_CtrlSalida_tipo = QComboBox(self.BodyFrame)
        self.cbox_CtrlSalida_tipo.setObjectName(u"cbox_CtrlSalida_tipo")
        self.cbox_CtrlSalida_tipo.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlSalida_tipo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cbox_CtrlSalida_tipo, 1, 1, 1, 1)

        self.qlinee_CtrlSalida_cantidad = QLineEdit(self.BodyFrame)
        self.qlinee_CtrlSalida_cantidad.setObjectName(u"qlinee_CtrlSalida_cantidad")
        self.qlinee_CtrlSalida_cantidad.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.qlinee_CtrlSalida_cantidad, 3, 3, 1, 1)

        self.ql_CtrlSalida_cantidad = QLabel(self.BodyFrame)
        self.ql_CtrlSalida_cantidad.setObjectName(u"ql_CtrlSalida_cantidad")
        self.ql_CtrlSalida_cantidad.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_cantidad.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlSalida_cantidad, 3, 2, 1, 1)

        self.qlinee_CtrlSalida_fechaingreso = QLineEdit(self.BodyFrame)
        self.qlinee_CtrlSalida_fechaingreso.setObjectName(u"qlinee_CtrlSalida_fechaingreso")
        self.qlinee_CtrlSalida_fechaingreso.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.qlinee_CtrlSalida_fechaingreso, 2, 1, 1, 1)

        self.cbox_CtrlSalida_condicion = QComboBox(self.BodyFrame)
        self.cbox_CtrlSalida_condicion.setObjectName(u"cbox_CtrlSalida_condicion")
        self.cbox_CtrlSalida_condicion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlSalida_condicion.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cbox_CtrlSalida_condicion, 4, 1, 1, 1)

        self.qlinee_CtrlSalida_totalunidad = QLineEdit(self.BodyFrame)
        self.qlinee_CtrlSalida_totalunidad.setObjectName(u"qlinee_CtrlSalida_totalunidad")
        self.qlinee_CtrlSalida_totalunidad.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.qlinee_CtrlSalida_totalunidad, 3, 1, 1, 1)

        self.cbox_CtrlSalida_sede = QComboBox(self.BodyFrame)
        self.cbox_CtrlSalida_sede.setObjectName(u"cbox_CtrlSalida_sede")
        self.cbox_CtrlSalida_sede.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlSalida_sede.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cbox_CtrlSalida_sede, 1, 3, 1, 1)

        self.ql_CtrlSalida_unidadmedida = QLabel(self.BodyFrame)
        self.ql_CtrlSalida_unidadmedida.setObjectName(u"ql_CtrlSalida_unidadmedida")
        self.ql_CtrlSalida_unidadmedida.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_unidadmedida.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlSalida_unidadmedida, 5, 0, 1, 1)

        self.cbox_CtrlSalida_unidadmedida = QComboBox(self.BodyFrame)
        self.cbox_CtrlSalida_unidadmedida.setObjectName(u"cbox_CtrlSalida_unidadmedida")
        self.cbox_CtrlSalida_unidadmedida.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlSalida_unidadmedida.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cbox_CtrlSalida_unidadmedida, 5, 1, 1, 1)

        self.cbox_CtrlSalida_recibidocalidad = QComboBox(self.BodyFrame)
        self.cbox_CtrlSalida_recibidocalidad.setObjectName(u"cbox_CtrlSalida_recibidocalidad")
        self.cbox_CtrlSalida_recibidocalidad.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlSalida_recibidocalidad.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cbox_CtrlSalida_recibidocalidad, 4, 3, 1, 1)

        self.ql_CtrlSalida_fechaingreso = QLabel(self.BodyFrame)
        self.ql_CtrlSalida_fechaingreso.setObjectName(u"ql_CtrlSalida_fechaingreso")
        self.ql_CtrlSalida_fechaingreso.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_fechaingreso.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlSalida_fechaingreso, 2, 0, 1, 1)

        self.ql_CtrlSalida_sede = QLabel(self.BodyFrame)
        self.ql_CtrlSalida_sede.setObjectName(u"ql_CtrlSalida_sede")
        self.ql_CtrlSalida_sede.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_sede.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlSalida_sede, 1, 2, 1, 1)

        self.ql_CtrlSalida_totalunidad = QLabel(self.BodyFrame)
        self.ql_CtrlSalida_totalunidad.setObjectName(u"ql_CtrlSalida_totalunidad")
        self.ql_CtrlSalida_totalunidad.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_totalunidad.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlSalida_totalunidad, 3, 0, 1, 1)

        self.frame_3 = QFrame(self.BodyFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.ql_CtrlSalida_condicion = QLabel(self.BodyFrame)
        self.ql_CtrlSalida_condicion.setObjectName(u"ql_CtrlSalida_condicion")
        self.ql_CtrlSalida_condicion.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_condicion.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlSalida_condicion, 4, 0, 1, 1)

        self.ql_CtrlSalida_recibidocalidad = QLabel(self.BodyFrame)
        self.ql_CtrlSalida_recibidocalidad.setObjectName(u"ql_CtrlSalida_recibidocalidad")
        self.ql_CtrlSalida_recibidocalidad.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_recibidocalidad.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlSalida_recibidocalidad, 4, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.ql_CtrlSalida_ubicacion_2 = QLabel(self.BodyFrame)
        self.ql_CtrlSalida_ubicacion_2.setObjectName(u"ql_CtrlSalida_ubicacion_2")
        self.ql_CtrlSalida_ubicacion_2.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_ubicacion_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.ql_CtrlSalida_ubicacion_2, 8, 0, 1, 1)

        self.qlinee_CtrlSalida_recibe = QLineEdit(self.BodyFrame)
        self.qlinee_CtrlSalida_recibe.setObjectName(u"qlinee_CtrlSalida_recibe")
        self.qlinee_CtrlSalida_recibe.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.qlinee_CtrlSalida_recibe, 9, 3, 1, 1)

        self.ql_CtrlSalida_numguia = QLabel(self.BodyFrame)
        self.ql_CtrlSalida_numguia.setObjectName(u"ql_CtrlSalida_numguia")
        self.ql_CtrlSalida_numguia.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_numguia.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.ql_CtrlSalida_numguia, 9, 0, 1, 1)

        self.ql_CtrlSalida_recibe = QLabel(self.BodyFrame)
        self.ql_CtrlSalida_recibe.setObjectName(u"ql_CtrlSalida_recibe")
        self.ql_CtrlSalida_recibe.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_recibe.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.ql_CtrlSalida_recibe, 9, 2, 1, 1)

        self.ql_CtrlSalida_existencia = QLabel(self.BodyFrame)
        self.ql_CtrlSalida_existencia.setObjectName(u"ql_CtrlSalida_existencia")
        self.ql_CtrlSalida_existencia.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_existencia.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.ql_CtrlSalida_existencia, 8, 2, 1, 1)

        self.qlinee_CtrlSalida_existencia = QLineEdit(self.BodyFrame)
        self.qlinee_CtrlSalida_existencia.setObjectName(u"qlinee_CtrlSalida_existencia")
        self.qlinee_CtrlSalida_existencia.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.qlinee_CtrlSalida_existencia, 8, 3, 1, 1)

        self.qlinee_CtrlSalida_nguia = QLineEdit(self.BodyFrame)
        self.qlinee_CtrlSalida_nguia.setObjectName(u"qlinee_CtrlSalida_nguia")
        self.qlinee_CtrlSalida_nguia.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.qlinee_CtrlSalida_nguia, 9, 1, 1, 1)

        self.ql_CtrlSalida_observacion = QLabel(self.BodyFrame)
        self.ql_CtrlSalida_observacion.setObjectName(u"ql_CtrlSalida_observacion")
        self.ql_CtrlSalida_observacion.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_observacion.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.ql_CtrlSalida_observacion, 10, 0, 1, 1)

        self.cbox_CtrlSalida_ubicacion = QComboBox(self.BodyFrame)
        self.cbox_CtrlSalida_ubicacion.setObjectName(u"cbox_CtrlSalida_ubicacion")
        self.cbox_CtrlSalida_ubicacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlSalida_ubicacion.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.cbox_CtrlSalida_ubicacion, 8, 1, 1, 1)

        self.ql_CtrlSalida_detalles = QLabel(self.BodyFrame)
        self.ql_CtrlSalida_detalles.setObjectName(u"ql_CtrlSalida_detalles")
        self.ql_CtrlSalida_detalles.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_detalles.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.ql_CtrlSalida_detalles, 7, 0, 1, 1)

        self.lineEdit = QLineEdit(self.BodyFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.lineEdit, 7, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.BodyFrame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.lineEdit_2, 10, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_5)


        self.verticalLayout.addWidget(self.BodyFrame)

        self.line = QFrame(ContrlSalida)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(149, 170, 190);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.FooterFrame = QFrame(ContrlSalida)
        self.FooterFrame.setObjectName(u"FooterFrame")
        self.FooterFrame.setEnabled(False)
        self.FooterFrame.setFrameShape(QFrame.StyledPanel)
        self.FooterFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.FooterFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cbox_CtrlSalida_firma = QComboBox(self.FooterFrame)
        self.cbox_CtrlSalida_firma.setObjectName(u"cbox_CtrlSalida_firma")
        self.cbox_CtrlSalida_firma.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlSalida_firma.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.cbox_CtrlSalida_firma, 4, 3, 1, 1)

        self.ql_CtrlSalida_motivo = QLabel(self.FooterFrame)
        self.ql_CtrlSalida_motivo.setObjectName(u"ql_CtrlSalida_motivo")
        self.ql_CtrlSalida_motivo.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_motivo.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.ql_CtrlSalida_motivo, 1, 0, 1, 1)

        self.cbox_CtrlSalida_motivo = QComboBox(self.FooterFrame)
        self.cbox_CtrlSalida_motivo.setObjectName(u"cbox_CtrlSalida_motivo")
        self.cbox_CtrlSalida_motivo.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlSalida_motivo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.cbox_CtrlSalida_motivo, 1, 1, 1, 1)

        self.qlinee_CtrlSalida_fechaegreso = QLineEdit(self.FooterFrame)
        self.qlinee_CtrlSalida_fechaegreso.setObjectName(u"qlinee_CtrlSalida_fechaegreso")
        self.qlinee_CtrlSalida_fechaegreso.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.qlinee_CtrlSalida_fechaegreso, 2, 1, 1, 1)

        self.ql_CtrlSalida_fechaegreso = QLabel(self.FooterFrame)
        self.ql_CtrlSalida_fechaegreso.setObjectName(u"ql_CtrlSalida_fechaegreso")
        self.ql_CtrlSalida_fechaegreso.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_fechaegreso.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.ql_CtrlSalida_fechaegreso, 2, 0, 1, 1)

        self.ql_CtrlSalida_firmar = QLabel(self.FooterFrame)
        self.ql_CtrlSalida_firmar.setObjectName(u"ql_CtrlSalida_firmar")
        self.ql_CtrlSalida_firmar.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_firmar.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.ql_CtrlSalida_firmar, 4, 2, 1, 1)

        self.ql_CtrlSalida_actualizadopor = QLabel(self.FooterFrame)
        self.ql_CtrlSalida_actualizadopor.setObjectName(u"ql_CtrlSalida_actualizadopor")
        self.ql_CtrlSalida_actualizadopor.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_actualizadopor.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.ql_CtrlSalida_actualizadopor, 4, 0, 1, 1)

        self.ql_CtrlSalida_egreso = QLabel(self.FooterFrame)
        self.ql_CtrlSalida_egreso.setObjectName(u"ql_CtrlSalida_egreso")
        self.ql_CtrlSalida_egreso.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_egreso.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.ql_CtrlSalida_egreso, 0, 0, 1, 1)

        self.qlinee_CtrlSalida_salidacantidad = QLineEdit(self.FooterFrame)
        self.qlinee_CtrlSalida_salidacantidad.setObjectName(u"qlinee_CtrlSalida_salidacantidad")
        self.qlinee_CtrlSalida_salidacantidad.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.qlinee_CtrlSalida_salidacantidad, 3, 1, 1, 1)

        self.ql_CtrlSalida_salidacantidad = QLabel(self.FooterFrame)
        self.ql_CtrlSalida_salidacantidad.setObjectName(u"ql_CtrlSalida_salidacantidad")
        self.ql_CtrlSalida_salidacantidad.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlSalida_salidacantidad.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.ql_CtrlSalida_salidacantidad, 3, 0, 1, 1)

        self.cbox_CtrlSalida_actualizadopor = QComboBox(self.FooterFrame)
        self.cbox_CtrlSalida_actualizadopor.setObjectName(u"cbox_CtrlSalida_actualizadopor")
        self.cbox_CtrlSalida_actualizadopor.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlSalida_actualizadopor.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.cbox_CtrlSalida_actualizadopor, 4, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_3)


        self.verticalLayout.addWidget(self.FooterFrame)

        self.ButtonFrame = QFrame(ContrlSalida)
        self.ButtonFrame.setObjectName(u"ButtonFrame")
        self.ButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.ButtonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.ButtonFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.ButtonFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	background-color: rgb(71, 93, 144);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: rgb(89, 118, 181);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"	background-color: rgb(62, 82, 125);\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.ButtonFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	background-color: rgb(71, 93, 144);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: rgb(89, 118, 181);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"	background-color: rgb(62, 82, 125);\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.ButtonFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	background-color: rgb(71, 93, 144);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: rgb(89, 118, 181);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"	background-color: rgb(62, 82, 125);\n"
"}")
        self.pushButton_3.setFlat(False)

        self.horizontalLayout_4.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.ButtonFrame)

        QWidget.setTabOrder(self.bttn_CtrlSalida_numeroactivo, self.bttn_CtrlSalida_nombreactivo)
        QWidget.setTabOrder(self.bttn_CtrlSalida_nombreactivo, self.cbox_CtrlSalida_tipo)
        QWidget.setTabOrder(self.cbox_CtrlSalida_tipo, self.cbox_CtrlSalida_sede)
        QWidget.setTabOrder(self.cbox_CtrlSalida_sede, self.qlinee_CtrlSalida_fechaingreso)
        QWidget.setTabOrder(self.qlinee_CtrlSalida_fechaingreso, self.qlinee_CtrlSalida_totalunidad)
        QWidget.setTabOrder(self.qlinee_CtrlSalida_totalunidad, self.qlinee_CtrlSalida_cantidad)
        QWidget.setTabOrder(self.qlinee_CtrlSalida_cantidad, self.cbox_CtrlSalida_condicion)
        QWidget.setTabOrder(self.cbox_CtrlSalida_condicion, self.cbox_CtrlSalida_recibidocalidad)
        QWidget.setTabOrder(self.cbox_CtrlSalida_recibidocalidad, self.cbox_CtrlSalida_unidadmedida)
        QWidget.setTabOrder(self.cbox_CtrlSalida_unidadmedida, self.cbox_CtrlSalida_ubicacion)
        QWidget.setTabOrder(self.cbox_CtrlSalida_ubicacion, self.qlinee_CtrlSalida_existencia)
        QWidget.setTabOrder(self.qlinee_CtrlSalida_existencia, self.qlinee_CtrlSalida_nguia)
        QWidget.setTabOrder(self.qlinee_CtrlSalida_nguia, self.qlinee_CtrlSalida_recibe)
        QWidget.setTabOrder(self.qlinee_CtrlSalida_recibe, self.cbox_CtrlSalida_motivo)
        QWidget.setTabOrder(self.cbox_CtrlSalida_motivo, self.qlinee_CtrlSalida_fechaegreso)
        QWidget.setTabOrder(self.qlinee_CtrlSalida_fechaegreso, self.qlinee_CtrlSalida_salidacantidad)
        QWidget.setTabOrder(self.qlinee_CtrlSalida_salidacantidad, self.cbox_CtrlSalida_actualizadopor)
        QWidget.setTabOrder(self.cbox_CtrlSalida_actualizadopor, self.cbox_CtrlSalida_firma)
        QWidget.setTabOrder(self.cbox_CtrlSalida_firma, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)

        self.retranslateUi(ContrlSalida)
        self.pushButton_3.clicked.connect(ContrlSalida.close)

        QMetaObject.connectSlotsByName(ContrlSalida)
    # setupUi

    def retranslateUi(self, ContrlSalida):
        ContrlSalida.setWindowTitle(QCoreApplication.translate("ContrlSalida", u"Control de Inventario (Salida)", None))
        self.ql_CtrlSalida_Titulo.setText(QCoreApplication.translate("ContrlSalida", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">GENERAR/MODIFICAR ORDEN DE SALIDA DE INVENTARIO</span></p></body></html>", None))
        self.ql_CtrlSalida_numeroactivo.setText(QCoreApplication.translate("ContrlSalida", u"<html><head/><body><p align=\"center\">Nombre Del Activo</p></body></html>", None))
        self.bttn_CtrlSalida_numeroactivo.setText("")
        self.bttn_CtrlSalida_nombreactivo.setText("")
        self.ql_CtrlSalida_nombreactivo.setText(QCoreApplication.translate("ContrlSalida", u"<html><head/><body><p align=\"center\">N\u00b0 Del Activo</p></body></html>", None))
        self.ql_CtrlSalida_tipo.setText(QCoreApplication.translate("ContrlSalida", u"<html><head/><body><p align=\"center\">Tipo:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.cbox_CtrlSalida_tipo.setToolTip(QCoreApplication.translate("ContrlSalida", u"Seleccione el tipo de Activo", None))
#endif // QT_CONFIG(tooltip)
        self.cbox_CtrlSalida_tipo.setCurrentText("")
        self.cbox_CtrlSalida_tipo.setPlaceholderText("")
        self.ql_CtrlSalida_cantidad.setText(QCoreApplication.translate("ContrlSalida", u"Cantidad", None))
        self.ql_CtrlSalida_unidadmedida.setText(QCoreApplication.translate("ContrlSalida", u" Unidad de Medida: ", None))
        self.ql_CtrlSalida_fechaingreso.setText(QCoreApplication.translate("ContrlSalida", u"Fecha Ingreso:", None))
        self.ql_CtrlSalida_sede.setText(QCoreApplication.translate("ContrlSalida", u"Sede:", None))
        self.ql_CtrlSalida_totalunidad.setText(QCoreApplication.translate("ContrlSalida", u"Total por Unidad:", None))
        self.ql_CtrlSalida_condicion.setText(QCoreApplication.translate("ContrlSalida", u"Condicion:", None))
        self.ql_CtrlSalida_recibidocalidad.setText(QCoreApplication.translate("ContrlSalida", u" Recibido en Calidad: ", None))
        self.ql_CtrlSalida_ubicacion_2.setText(QCoreApplication.translate("ContrlSalida", u"Ubicacion", None))
        self.ql_CtrlSalida_numguia.setText(QCoreApplication.translate("ContrlSalida", u" N\u00b0 De Gu\u00eda ", None))
        self.ql_CtrlSalida_recibe.setText(QCoreApplication.translate("ContrlSalida", u"Recibe", None))
        self.ql_CtrlSalida_existencia.setText(QCoreApplication.translate("ContrlSalida", u" Existencia ", None))
        self.ql_CtrlSalida_observacion.setText(QCoreApplication.translate("ContrlSalida", u"  Observacion  ", None))
        self.ql_CtrlSalida_detalles.setText(QCoreApplication.translate("ContrlSalida", u"  Detalles  ", None))
        self.ql_CtrlSalida_motivo.setText(QCoreApplication.translate("ContrlSalida", u"Motivo", None))
        self.ql_CtrlSalida_fechaegreso.setText(QCoreApplication.translate("ContrlSalida", u" Fecha de Engreso ", None))
        self.ql_CtrlSalida_firmar.setText(QCoreApplication.translate("ContrlSalida", u"  Firmar: ", None))
        self.ql_CtrlSalida_actualizadopor.setText(QCoreApplication.translate("ContrlSalida", u"Actualizado por:", None))
        self.ql_CtrlSalida_egreso.setText(QCoreApplication.translate("ContrlSalida", u"Egreso:", None))
        self.ql_CtrlSalida_salidacantidad.setText(QCoreApplication.translate("ContrlSalida", u"Salida Cantidad", None))
        self.pushButton.setText(QCoreApplication.translate("ContrlSalida", u"Egresar", None))
        self.pushButton_2.setText(QCoreApplication.translate("ContrlSalida", u"Modificar/Grabar", None))
        self.pushButton_3.setText(QCoreApplication.translate("ContrlSalida", u"Salir", None))
    # retranslateUi

