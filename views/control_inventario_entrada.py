# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'control_inventario_entrada.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from views.resources_rc import *



class Ui_ContrlEntrada(object):
    def setupUi(self, ContrlEntrada):
        if not ContrlEntrada.objectName():
            ContrlEntrada.setObjectName(u"ContrlEntrada")
        ContrlEntrada.setWindowModality(Qt.WindowModal)
        ContrlEntrada.resize(808, 444)
        icon = QIcon()
        icon.addFile(u":/logo_ipasme/icons/IPASME-logo-DABC2AE9B1-seeklogo.com.png", QSize(), QIcon.Normal, QIcon.Off)
        ContrlEntrada.setWindowIcon(icon)
        ContrlEntrada.setStyleSheet(u"background-color: rgb(177, 214, 166);")
        self.gridLayout_3 = QGridLayout(ContrlEntrada)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ql_CtrlEntrada_tipo = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_tipo.setObjectName(u"ql_CtrlEntrada_tipo")
        self.ql_CtrlEntrada_tipo.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_tipo.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_tipo, 0, 0, 1, 1)

        self.ql_CtrlEntrada_sede = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_sede.setObjectName(u"ql_CtrlEntrada_sede")
        self.ql_CtrlEntrada_sede.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_sede.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_sede, 0, 2, 1, 1)

        self.qlinee_CtrlEntrada_cantidad = QLineEdit(ContrlEntrada)
        self.qlinee_CtrlEntrada_cantidad.setObjectName(u"qlinee_CtrlEntrada_cantidad")
        self.qlinee_CtrlEntrada_cantidad.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.qlinee_CtrlEntrada_cantidad, 4, 3, 1, 1)

        self.ql_CtrlEntrada_fechaingreso = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_fechaingreso.setObjectName(u"ql_CtrlEntrada_fechaingreso")
        self.ql_CtrlEntrada_fechaingreso.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_fechaingreso.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_fechaingreso, 3, 0, 1, 1)

        self.qlinee_CtrlEntrada_fechaingreso = QLineEdit(ContrlEntrada)
        self.qlinee_CtrlEntrada_fechaingreso.setObjectName(u"qlinee_CtrlEntrada_fechaingreso")
        self.qlinee_CtrlEntrada_fechaingreso.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.qlinee_CtrlEntrada_fechaingreso, 3, 1, 1, 1)

        self.cbox_CtrlEntrada_tipo = QComboBox(ContrlEntrada)
        self.cbox_CtrlEntrada_tipo.addItem("")
        self.cbox_CtrlEntrada_tipo.addItem("")
        self.cbox_CtrlEntrada_tipo.addItem("")
        self.cbox_CtrlEntrada_tipo.addItem("")
        self.cbox_CtrlEntrada_tipo.setObjectName(u"cbox_CtrlEntrada_tipo")
        self.cbox_CtrlEntrada_tipo.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlEntrada_tipo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.cbox_CtrlEntrada_tipo, 0, 1, 1, 1)

        self.qlinee_CtrlEntrada_actnombre = QLineEdit(ContrlEntrada)
        self.qlinee_CtrlEntrada_actnombre.setObjectName(u"qlinee_CtrlEntrada_actnombre")
        self.qlinee_CtrlEntrada_actnombre.setFocusPolicy(Qt.StrongFocus)
        self.qlinee_CtrlEntrada_actnombre.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.qlinee_CtrlEntrada_actnombre, 1, 1, 1, 1)

        self.ql_CtrlEntrada_cantidad = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_cantidad.setObjectName(u"ql_CtrlEntrada_cantidad")
        self.ql_CtrlEntrada_cantidad.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_cantidad.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_cantidad, 4, 2, 1, 1)

        self.ql_CtrlEntrada_numactivo = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_numactivo.setObjectName(u"ql_CtrlEntrada_numactivo")
        self.ql_CtrlEntrada_numactivo.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_numactivo.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_numactivo, 2, 0, 1, 1)

        self.cbox_CtrlEntrada_sede = QComboBox(ContrlEntrada)
        self.cbox_CtrlEntrada_sede.addItem("")
        self.cbox_CtrlEntrada_sede.addItem("")
        self.cbox_CtrlEntrada_sede.addItem("")
        self.cbox_CtrlEntrada_sede.setObjectName(u"cbox_CtrlEntrada_sede")
        self.cbox_CtrlEntrada_sede.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlEntrada_sede.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.cbox_CtrlEntrada_sede, 0, 3, 1, 1)

        self.qlinee_CtrlEntrada_totalxunidad = QLineEdit(ContrlEntrada)
        self.qlinee_CtrlEntrada_totalxunidad.setObjectName(u"qlinee_CtrlEntrada_totalxunidad")
        self.qlinee_CtrlEntrada_totalxunidad.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.qlinee_CtrlEntrada_totalxunidad, 5, 1, 1, 1)

        self.ql_CtrlEntrada_actnombre = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_actnombre.setObjectName(u"ql_CtrlEntrada_actnombre")
        self.ql_CtrlEntrada_actnombre.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_actnombre.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_actnombre, 1, 0, 1, 1)

        self.ql_CtrlEntrada_unidadxmedida = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_unidadxmedida.setObjectName(u"ql_CtrlEntrada_unidadxmedida")
        self.ql_CtrlEntrada_unidadxmedida.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_unidadxmedida.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_unidadxmedida, 4, 0, 1, 1)

        self.ql_CtrlEntrada_totalxunidad = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_totalxunidad.setObjectName(u"ql_CtrlEntrada_totalxunidad")
        self.ql_CtrlEntrada_totalxunidad.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_totalxunidad.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_totalxunidad, 5, 0, 1, 1)

        self.cbox_CtrlEntrada_sede_2 = QComboBox(ContrlEntrada)
        self.cbox_CtrlEntrada_sede_2.addItem("")
        self.cbox_CtrlEntrada_sede_2.addItem("")
        self.cbox_CtrlEntrada_sede_2.addItem("")
        self.cbox_CtrlEntrada_sede_2.addItem("")
        self.cbox_CtrlEntrada_sede_2.addItem("")
        self.cbox_CtrlEntrada_sede_2.setObjectName(u"cbox_CtrlEntrada_sede_2")
        self.cbox_CtrlEntrada_sede_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlEntrada_sede_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.cbox_CtrlEntrada_sede_2, 4, 1, 1, 1)

        self.qlinee_CtrlEntrada_numactivo = QLineEdit(ContrlEntrada)
        self.qlinee_CtrlEntrada_numactivo.setObjectName(u"qlinee_CtrlEntrada_numactivo")
        self.qlinee_CtrlEntrada_numactivo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.qlinee_CtrlEntrada_numactivo, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        self.label_17 = QLabel(ContrlEntrada)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)

        self.line = QFrame(ContrlEntrada)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(149, 170, 190);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 4, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.qlinee_CtrlEntrada_nivelexistencia = QLineEdit(ContrlEntrada)
        self.qlinee_CtrlEntrada_nivelexistencia.setObjectName(u"qlinee_CtrlEntrada_nivelexistencia")
        self.qlinee_CtrlEntrada_nivelexistencia.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.qlinee_CtrlEntrada_nivelexistencia, 2, 1, 1, 1)

        self.cbox_CtrlEntrada_recividocalidad = QComboBox(ContrlEntrada)
        self.cbox_CtrlEntrada_recividocalidad.addItem("")
        self.cbox_CtrlEntrada_recividocalidad.addItem("")
        self.cbox_CtrlEntrada_recividocalidad.addItem("")
        self.cbox_CtrlEntrada_recividocalidad.addItem("")
        self.cbox_CtrlEntrada_recividocalidad.setObjectName(u"cbox_CtrlEntrada_recividocalidad")
        self.cbox_CtrlEntrada_recividocalidad.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlEntrada_recividocalidad.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cbox_CtrlEntrada_recividocalidad, 0, 3, 1, 1)

        self.qlinee_CtrlEntrada_observaciones = QLineEdit(ContrlEntrada)
        self.qlinee_CtrlEntrada_observaciones.setObjectName(u"qlinee_CtrlEntrada_observaciones")
        self.qlinee_CtrlEntrada_observaciones.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.qlinee_CtrlEntrada_observaciones, 4, 1, 1, 1)

        self.ql_CtrlEntrada_detalles = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_detalles.setObjectName(u"ql_CtrlEntrada_detalles")
        self.ql_CtrlEntrada_detalles.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_detalles.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlEntrada_detalles, 1, 0, 1, 1)

        self.ql_CtrlEntrada_nivelexistencia = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_nivelexistencia.setObjectName(u"ql_CtrlEntrada_nivelexistencia")
        self.ql_CtrlEntrada_nivelexistencia.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_nivelexistencia.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlEntrada_nivelexistencia, 2, 0, 1, 1)

        self.ql_CtrlEntrada_condicion = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_condicion.setObjectName(u"ql_CtrlEntrada_condicion")
        self.ql_CtrlEntrada_condicion.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_condicion.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlEntrada_condicion, 0, 0, 1, 1)

        self.ql_CtrlEntrada_reciboencalidad = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_reciboencalidad.setObjectName(u"ql_CtrlEntrada_reciboencalidad")
        self.ql_CtrlEntrada_reciboencalidad.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_reciboencalidad.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlEntrada_reciboencalidad, 0, 2, 1, 1)

        self.cbox_CtrlEntrada_recibe = QComboBox(ContrlEntrada)
        self.cbox_CtrlEntrada_recibe.addItem("")
        self.cbox_CtrlEntrada_recibe.addItem("")
        self.cbox_CtrlEntrada_recibe.setObjectName(u"cbox_CtrlEntrada_recibe")
        self.cbox_CtrlEntrada_recibe.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlEntrada_recibe.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cbox_CtrlEntrada_recibe, 5, 1, 1, 1)

        self.cbox_CtrlEntrada_condicion = QComboBox(ContrlEntrada)
        self.cbox_CtrlEntrada_condicion.addItem("")
        self.cbox_CtrlEntrada_condicion.addItem("")
        self.cbox_CtrlEntrada_condicion.addItem("")
        self.cbox_CtrlEntrada_condicion.addItem("")
        self.cbox_CtrlEntrada_condicion.setObjectName(u"cbox_CtrlEntrada_condicion")
        self.cbox_CtrlEntrada_condicion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlEntrada_condicion.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cbox_CtrlEntrada_condicion, 0, 1, 1, 1)

        self.qlinee_CtrlEntrada_numguia = QLineEdit(ContrlEntrada)
        self.qlinee_CtrlEntrada_numguia.setObjectName(u"qlinee_CtrlEntrada_numguia")
        self.qlinee_CtrlEntrada_numguia.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.qlinee_CtrlEntrada_numguia, 3, 1, 1, 1)

        self.ql_CtrlEntrada_observaciones = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_observaciones.setObjectName(u"ql_CtrlEntrada_observaciones")
        self.ql_CtrlEntrada_observaciones.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_observaciones.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlEntrada_observaciones, 4, 0, 1, 1)

        self.qplt_CtrlEntrada_detalles = QPlainTextEdit(ContrlEntrada)
        self.qplt_CtrlEntrada_detalles.setObjectName(u"qplt_CtrlEntrada_detalles")
        self.qplt_CtrlEntrada_detalles.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.qplt_CtrlEntrada_detalles, 1, 1, 1, 1)

        self.ql_CtrlEntrada_numguia = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_numguia.setObjectName(u"ql_CtrlEntrada_numguia")
        self.ql_CtrlEntrada_numguia.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_numguia.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlEntrada_numguia, 3, 0, 1, 1)

        self.ql_CtrlEntrada_ubicacion = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_ubicacion.setObjectName(u"ql_CtrlEntrada_ubicacion")
        self.ql_CtrlEntrada_ubicacion.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_ubicacion.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlEntrada_ubicacion, 1, 2, 1, 1)

        self.cbox_CtrlEntrada_ubicacion = QComboBox(ContrlEntrada)
        self.cbox_CtrlEntrada_ubicacion.addItem("")
        self.cbox_CtrlEntrada_ubicacion.addItem("")
        self.cbox_CtrlEntrada_ubicacion.setObjectName(u"cbox_CtrlEntrada_ubicacion")
        self.cbox_CtrlEntrada_ubicacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlEntrada_ubicacion.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cbox_CtrlEntrada_ubicacion, 1, 3, 1, 1)

        self.ql_CtrlEntrada_recibe = QLabel(ContrlEntrada)
        self.ql_CtrlEntrada_recibe.setObjectName(u"ql_CtrlEntrada_recibe")
        self.ql_CtrlEntrada_recibe.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_recibe.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlEntrada_recibe, 5, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 3, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ContrlEntrada)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setWindowTitle("Guardar")
        
        self.buttonBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonBox.setStyleSheet(u"QPushButton{\n"
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
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout_3.addWidget(self.buttonBox, 5, 0, 1, 1, Qt.AlignHCenter)

        self.line_2 = QFrame(ContrlEntrada)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(149, 170, 190);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 1, 0, 1, 1)

        QWidget.setTabOrder(self.cbox_CtrlEntrada_tipo, self.cbox_CtrlEntrada_sede)
        QWidget.setTabOrder(self.cbox_CtrlEntrada_sede, self.qlinee_CtrlEntrada_actnombre)
        QWidget.setTabOrder(self.qlinee_CtrlEntrada_actnombre, self.qlinee_CtrlEntrada_numactivo)
        QWidget.setTabOrder(self.qlinee_CtrlEntrada_numactivo, self.qlinee_CtrlEntrada_fechaingreso)
        QWidget.setTabOrder(self.qlinee_CtrlEntrada_fechaingreso, self.cbox_CtrlEntrada_sede_2)
        QWidget.setTabOrder(self.cbox_CtrlEntrada_sede_2, self.qlinee_CtrlEntrada_cantidad)
        QWidget.setTabOrder(self.qlinee_CtrlEntrada_cantidad, self.qlinee_CtrlEntrada_totalxunidad)
        QWidget.setTabOrder(self.qlinee_CtrlEntrada_totalxunidad, self.cbox_CtrlEntrada_condicion)
        QWidget.setTabOrder(self.cbox_CtrlEntrada_condicion, self.cbox_CtrlEntrada_recividocalidad)
        QWidget.setTabOrder(self.cbox_CtrlEntrada_recividocalidad, self.qplt_CtrlEntrada_detalles)
        QWidget.setTabOrder(self.qplt_CtrlEntrada_detalles, self.cbox_CtrlEntrada_ubicacion)
        QWidget.setTabOrder(self.cbox_CtrlEntrada_ubicacion, self.qlinee_CtrlEntrada_nivelexistencia)
        QWidget.setTabOrder(self.qlinee_CtrlEntrada_nivelexistencia, self.qlinee_CtrlEntrada_numguia)
        QWidget.setTabOrder(self.qlinee_CtrlEntrada_numguia, self.qlinee_CtrlEntrada_observaciones)
        QWidget.setTabOrder(self.qlinee_CtrlEntrada_observaciones, self.cbox_CtrlEntrada_recibe)

        self.retranslateUi(ContrlEntrada)

        self.cbox_CtrlEntrada_tipo.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ContrlEntrada)
    # setupUi

    def retranslateUi(self, ContrlEntrada):
        ContrlEntrada.setWindowTitle(QCoreApplication.translate("ContrlEntrada", u"Control De Inventario (Entrada)", None))
        ContrlEntrada.setWindowFilePath("")
        self.ql_CtrlEntrada_tipo.setText(QCoreApplication.translate("ContrlEntrada", u"Tipo:", None))
        self.ql_CtrlEntrada_sede.setText(QCoreApplication.translate("ContrlEntrada", u"Sede:", None))
        self.ql_CtrlEntrada_fechaingreso.setText(QCoreApplication.translate("ContrlEntrada", u" Fecha de Ingreso: ", None))
        self.cbox_CtrlEntrada_tipo.setItemText(0, QCoreApplication.translate("ContrlEntrada", u"Bienes", None))
        self.cbox_CtrlEntrada_tipo.setItemText(1, QCoreApplication.translate("ContrlEntrada", u"Servicios", None))
        self.cbox_CtrlEntrada_tipo.setItemText(2, QCoreApplication.translate("ContrlEntrada", u"Medicamentos", None))
        self.cbox_CtrlEntrada_tipo.setItemText(3, QCoreApplication.translate("ContrlEntrada", u"Insumos Medicos", None))

        self.ql_CtrlEntrada_cantidad.setText(QCoreApplication.translate("ContrlEntrada", u" Cantidad: ", None))
        self.ql_CtrlEntrada_numactivo.setText(QCoreApplication.translate("ContrlEntrada", u"N\u00b0Activo:", None))
        self.cbox_CtrlEntrada_sede.setItemText(0, QCoreApplication.translate("ContrlEntrada", u"Maracay 1 (PRINCIPAL)", None))
        self.cbox_CtrlEntrada_sede.setItemText(1, QCoreApplication.translate("ContrlEntrada", u"Maracay 2 (SAN JACINTO)", None))
        self.cbox_CtrlEntrada_sede.setItemText(2, QCoreApplication.translate("ContrlEntrada", u"Maracay (A.MEDICA)", None))

        self.ql_CtrlEntrada_actnombre.setText(QCoreApplication.translate("ContrlEntrada", u"Activo: Nombre:", None))
        self.ql_CtrlEntrada_unidadxmedida.setText(QCoreApplication.translate("ContrlEntrada", u" Unidad de Medida: ", None))
        self.ql_CtrlEntrada_totalxunidad.setText(QCoreApplication.translate("ContrlEntrada", u"Total x Unidad:", None))
        self.cbox_CtrlEntrada_sede_2.setItemText(0, QCoreApplication.translate("ContrlEntrada", u"Cajas", None))
        self.cbox_CtrlEntrada_sede_2.setItemText(1, QCoreApplication.translate("ContrlEntrada", u"Frescos", None))
        self.cbox_CtrlEntrada_sede_2.setItemText(2, QCoreApplication.translate("ContrlEntrada", u"Unidad", None))
        self.cbox_CtrlEntrada_sede_2.setItemText(3, QCoreApplication.translate("ContrlEntrada", u"Bolsas", None))
        self.cbox_CtrlEntrada_sede_2.setItemText(4, QCoreApplication.translate("ContrlEntrada", u"Pases", None))

        self.label_17.setText(QCoreApplication.translate("ContrlEntrada", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">INTRODUZCA LOS DATOS DE LOS BIENES, ACTIVOS Y/O INSUMOS</span></p></body></html>", None))
        self.cbox_CtrlEntrada_recividocalidad.setItemText(0, QCoreApplication.translate("ContrlEntrada", u"Donaci\u00f3n", None))
        self.cbox_CtrlEntrada_recividocalidad.setItemText(1, QCoreApplication.translate("ContrlEntrada", u"Prestamo", None))
        self.cbox_CtrlEntrada_recividocalidad.setItemText(2, QCoreApplication.translate("ContrlEntrada", u"Ingreso", None))
        self.cbox_CtrlEntrada_recividocalidad.setItemText(3, QCoreApplication.translate("ContrlEntrada", u"Compra", None))

        self.ql_CtrlEntrada_detalles.setText(QCoreApplication.translate("ContrlEntrada", u" Detalles:", None))
        self.ql_CtrlEntrada_nivelexistencia.setText(QCoreApplication.translate("ContrlEntrada", u"  Nivel Min.Existencia:", None))
        self.ql_CtrlEntrada_condicion.setText(QCoreApplication.translate("ContrlEntrada", u"Condici\u00f3n:", None))
        self.ql_CtrlEntrada_reciboencalidad.setText(QCoreApplication.translate("ContrlEntrada", u" Recibido en Calidad: ", None))
        self.cbox_CtrlEntrada_recibe.setItemText(0, QCoreApplication.translate("ContrlEntrada", u"J.Almacen", None))
        self.cbox_CtrlEntrada_recibe.setItemText(1, QCoreApplication.translate("ContrlEntrada", u"Administraci\u00f3n", None))

        self.cbox_CtrlEntrada_condicion.setItemText(0, QCoreApplication.translate("ContrlEntrada", u"Nuevo", None))
        self.cbox_CtrlEntrada_condicion.setItemText(1, QCoreApplication.translate("ContrlEntrada", u"Buen Estado", None))
        self.cbox_CtrlEntrada_condicion.setItemText(2, QCoreApplication.translate("ContrlEntrada", u"Detalles", None))
        self.cbox_CtrlEntrada_condicion.setItemText(3, QCoreApplication.translate("ContrlEntrada", u"Desuso", None))

        self.ql_CtrlEntrada_observaciones.setText(QCoreApplication.translate("ContrlEntrada", u"Observaci\u00f3nes:", None))
        self.ql_CtrlEntrada_numguia.setText(QCoreApplication.translate("ContrlEntrada", u" N\u00b0Gu\u00eda:", None))
        self.ql_CtrlEntrada_ubicacion.setText(QCoreApplication.translate("ContrlEntrada", u"Ubicaci\u00f3n:", None))
        self.cbox_CtrlEntrada_ubicacion.setItemText(0, QCoreApplication.translate("ContrlEntrada", u"Almacen 1", None))
        self.cbox_CtrlEntrada_ubicacion.setItemText(1, QCoreApplication.translate("ContrlEntrada", u"Almacen 2", None))

        self.ql_CtrlEntrada_recibe.setText(QCoreApplication.translate("ContrlEntrada", u"Recibe", None))
    # retranslateUi

