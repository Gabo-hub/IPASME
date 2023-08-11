
#********************************** respaldo de entrega de medicamento **********************************************************

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entrega_de_medicamentos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from views.resources_rc import *
from views.AgregarComboGridMed import *

class Ui_EntradaMedicamento(object):
    def setupUi(self, EntradaMedicamento):
        if not EntradaMedicamento.objectName():
            EntradaMedicamento.setObjectName(u"EntradaMedicamento")
        EntradaMedicamento.setWindowModality(Qt.WindowModal)
        EntradaMedicamento.resize(772, 527)
        icon = QIcon()
        icon.addFile(u":/logo_ipasme/icons/IPASME-logo-DABC2AE9B1-seeklogo.com.png", QSize(), QIcon.Normal, QIcon.Off)
        EntradaMedicamento.setWindowIcon(icon)
        EntradaMedicamento.setStyleSheet(u"background-color: rgb(177, 214, 166);")
        self.gridLayout_3 = QGridLayout(EntradaMedicamento)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_17 = QLabel(EntradaMedicamento)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)

        self.label = QLabel(EntradaMedicamento)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setStyleSheet(u"background-color: rgb(44, 86, 16);\n"
"color: rgb(255, 255, 127);")

        self.gridLayout_3.addWidget(self.label, 7, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.ql_CtrlEntrada_origenrecipetext = QLabel(EntradaMedicamento)
        self.ql_CtrlEntrada_origenrecipetext.setObjectName(u"ql_CtrlEntrada_origenrecipetext")
        self.ql_CtrlEntrada_origenrecipetext.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_origenrecipetext.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlEntrada_origenrecipetext, 1, 2, 1, 1)

        self.cbox_CtrlEntrada_encalidaddetextinfo = QComboBox(EntradaMedicamento)
        self.cbox_CtrlEntrada_encalidaddetextinfo.addItem("")
        self.cbox_CtrlEntrada_encalidaddetextinfo.addItem("")
        self.cbox_CtrlEntrada_encalidaddetextinfo.addItem("")
        self.cbox_CtrlEntrada_encalidaddetextinfo.addItem("")
        self.cbox_CtrlEntrada_encalidaddetextinfo.addItem("")
        self.cbox_CtrlEntrada_encalidaddetextinfo.setObjectName(u"cbox_CtrlEntrada_encalidaddetextinfo")
        self.cbox_CtrlEntrada_encalidaddetextinfo.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlEntrada_encalidaddetextinfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cbox_CtrlEntrada_encalidaddetextinfo, 2, 1, 1, 1)

        self.ql_CtrlEntrada_entregatext = QLabel(EntradaMedicamento)
        self.ql_CtrlEntrada_entregatext.setObjectName(u"ql_CtrlEntrada_entregatext")
        self.ql_CtrlEntrada_entregatext.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_entregatext.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlEntrada_entregatext, 2, 2, 1, 1)

        self.cbox_CtrlEntrada_origenrecipeinfo = QComboBox(EntradaMedicamento)
        self.cbox_CtrlEntrada_origenrecipeinfo.addItem("")
        self.cbox_CtrlEntrada_origenrecipeinfo.addItem("")
        self.cbox_CtrlEntrada_origenrecipeinfo.addItem("")
        self.cbox_CtrlEntrada_origenrecipeinfo.addItem("")
        self.cbox_CtrlEntrada_origenrecipeinfo.addItem("")
        self.cbox_CtrlEntrada_origenrecipeinfo.addItem("")
        self.cbox_CtrlEntrada_origenrecipeinfo.addItem("")
        self.cbox_CtrlEntrada_origenrecipeinfo.setObjectName(u"cbox_CtrlEntrada_origenrecipeinfo")
        self.cbox_CtrlEntrada_origenrecipeinfo.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlEntrada_origenrecipeinfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cbox_CtrlEntrada_origenrecipeinfo, 1, 3, 1, 1)

        self.ql_CtrlEntrada_aceptadoportext = QLabel(EntradaMedicamento)
        self.ql_CtrlEntrada_aceptadoportext.setObjectName(u"ql_CtrlEntrada_aceptadoportext")
        self.ql_CtrlEntrada_aceptadoportext.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_aceptadoportext.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlEntrada_aceptadoportext, 1, 0, 1, 1)

        self.cbox_CtrlEntrada_aceptadoporinfo = QComboBox(EntradaMedicamento)
        self.cbox_CtrlEntrada_aceptadoporinfo.addItem("")
        self.cbox_CtrlEntrada_aceptadoporinfo.addItem("")
        self.cbox_CtrlEntrada_aceptadoporinfo.addItem("")
        self.cbox_CtrlEntrada_aceptadoporinfo.addItem("")
        self.cbox_CtrlEntrada_aceptadoporinfo.setObjectName(u"cbox_CtrlEntrada_aceptadoporinfo")
        self.cbox_CtrlEntrada_aceptadoporinfo.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlEntrada_aceptadoporinfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cbox_CtrlEntrada_aceptadoporinfo, 1, 1, 1, 1)

        self.cbox_CtrlEntrada_entregainfo = QComboBox(EntradaMedicamento)
        self.cbox_CtrlEntrada_entregainfo.addItem("")
        self.cbox_CtrlEntrada_entregainfo.addItem("")
        self.cbox_CtrlEntrada_entregainfo.addItem("")
        self.cbox_CtrlEntrada_entregainfo.addItem("")
        self.cbox_CtrlEntrada_entregainfo.addItem("")
        self.cbox_CtrlEntrada_entregainfo.setObjectName(u"cbox_CtrlEntrada_entregainfo")
        self.cbox_CtrlEntrada_entregainfo.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlEntrada_entregainfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cbox_CtrlEntrada_entregainfo, 2, 3, 1, 1)

        self.ql_CtrlEntrada_encalidaddetext = QLabel(EntradaMedicamento)
        self.ql_CtrlEntrada_encalidaddetext.setObjectName(u"ql_CtrlEntrada_encalidaddetext")
        self.ql_CtrlEntrada_encalidaddetext.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_encalidaddetext.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ql_CtrlEntrada_encalidaddetext, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.ql_CtrlEntrada_direccioninfo_2 = QLabel(EntradaMedicamento)
        self.ql_CtrlEntrada_direccioninfo_2.setObjectName(u"ql_CtrlEntrada_direccioninfo_2")
        self.ql_CtrlEntrada_direccioninfo_2.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_direccioninfo_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.ql_CtrlEntrada_direccioninfo_2)

        self.qplt_CtrlEntrada_direccioninfo_2 = QPlainTextEdit(EntradaMedicamento)
        self.qplt_CtrlEntrada_direccioninfo_2.setObjectName(u"qplt_CtrlEntrada_direccioninfo_2")
        self.qplt_CtrlEntrada_direccioninfo_2.setMinimumSize(QSize(0, 0))
        self.qplt_CtrlEntrada_direccioninfo_2.setMaximumSize(QSize(16777215, 40))
        self.qplt_CtrlEntrada_direccioninfo_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.qplt_CtrlEntrada_direccioninfo_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)

        self.tb_tabla = QTableWidget(EntradaMedicamento)
        if (self.tb_tabla.columnCount() < 4):
            self.tb_tabla.setColumnCount(4)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        self.tb_tabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tb_tabla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tb_tabla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tb_tabla.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tb_tabla.rowCount() < 10):
            self.tb_tabla.setRowCount(10)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(0, 2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_tabla.setItem(0, 3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(1, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(1, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(2, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(2, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(3, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(3, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(4, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(4, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(5, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(5, 2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(6, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(6, 2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(7, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(7, 2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(8, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(8, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(9, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.tb_tabla.setItem(9, 2, __qtablewidgetitem24)
        self.tb_tabla.setObjectName(u"tb_tabla")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_tabla.sizePolicy().hasHeightForWidth())
        self.tb_tabla.setSizePolicy(sizePolicy)
        self.tb_tabla.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tb_tabla.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"")
        self.tb_tabla.setFrameShape(QFrame.NoFrame)
        self.tb_tabla.setDragDropOverwriteMode(True)
        self.tb_tabla.setAlternatingRowColors(True)
        self.tb_tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tb_tabla.setRowCount(10)
        self.tb_tabla.setColumnCount(4)
        self.tb_tabla.horizontalHeader().setVisible(False)
        self.tb_tabla.horizontalHeader().setStretchLastSection(True)
        self.tb_tabla.verticalHeader().setVisible(True)
        self.tb_tabla.verticalHeader().setProperty("showSortIndicator", False)

        self.gridLayout_3.addWidget(self.tb_tabla, 8, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(EntradaMedicamento)
        self.pushButton_2.setObjectName(u"pushButton_2")
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

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(EntradaMedicamento)
        self.pushButton.setObjectName(u"pushButton")
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

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 10, 0, 1, 1)

        self.line_2 = QFrame(EntradaMedicamento)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(149, 170, 190);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 1, 0, 1, 1)

        self.line = QFrame(EntradaMedicamento)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(149, 170, 190);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 9, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.qlinee_CtrlEntrada_nombreinfo = QLineEdit(EntradaMedicamento)
        self.qlinee_CtrlEntrada_nombreinfo.setObjectName(u"qlinee_CtrlEntrada_nombreinfo")
        self.qlinee_CtrlEntrada_nombreinfo.setFocusPolicy(Qt.WheelFocus)
        self.qlinee_CtrlEntrada_nombreinfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_CtrlEntrada_nombreinfo.setMaxLength(30)

        self.gridLayout_2.addWidget(self.qlinee_CtrlEntrada_nombreinfo, 1, 1, 1, 1)

        self.ql_CtrlEntrada_apellidostext = QLabel(EntradaMedicamento)
        self.ql_CtrlEntrada_apellidostext.setObjectName(u"ql_CtrlEntrada_apellidostext")
        self.ql_CtrlEntrada_apellidostext.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_apellidostext.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_apellidostext, 1, 2, 1, 1)

        self.ql_CtrlEntrada_estadotext = QLabel(EntradaMedicamento)
        self.ql_CtrlEntrada_estadotext.setObjectName(u"ql_CtrlEntrada_estadotext")
        self.ql_CtrlEntrada_estadotext.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_estadotext.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_estadotext, 5, 0, 1, 1)

        self.qlinee_CtrlEntrada_apellidosinfo = QLineEdit(EntradaMedicamento)
        self.qlinee_CtrlEntrada_apellidosinfo.setObjectName(u"qlinee_CtrlEntrada_apellidosinfo")
        self.qlinee_CtrlEntrada_apellidosinfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.qlinee_CtrlEntrada_apellidosinfo, 1, 3, 1, 1)

        self.ql_CtrlEntrada_telefonotext = QLabel(EntradaMedicamento)
        self.ql_CtrlEntrada_telefonotext.setObjectName(u"ql_CtrlEntrada_telefonotext")
        self.ql_CtrlEntrada_telefonotext.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_telefonotext.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_telefonotext, 4, 0, 1, 1)

        self.ql_CtrlEntrada_cedulatext = QLabel(EntradaMedicamento)
        self.ql_CtrlEntrada_cedulatext.setObjectName(u"ql_CtrlEntrada_cedulatext")
        self.ql_CtrlEntrada_cedulatext.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_cedulatext.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_cedulatext, 0, 0, 1, 1)

        self.ql_CtrlEntrada_nombrestext = QLabel(EntradaMedicamento)
        self.ql_CtrlEntrada_nombrestext.setObjectName(u"ql_CtrlEntrada_nombrestext")
        self.ql_CtrlEntrada_nombrestext.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_nombrestext.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_nombrestext, 1, 0, 1, 1)

        self.qlinee_CtrlEntrada_telefonoinfo = QLineEdit(EntradaMedicamento)
        self.qlinee_CtrlEntrada_telefonoinfo.setObjectName(u"qlinee_CtrlEntrada_telefonoinfo")
        self.qlinee_CtrlEntrada_telefonoinfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.qlinee_CtrlEntrada_telefonoinfo, 4, 1, 1, 1)

        self.ql_CtrlEntrada_nacionalidadtext = QLabel(EntradaMedicamento)
        self.ql_CtrlEntrada_nacionalidadtext.setObjectName(u"ql_CtrlEntrada_nacionalidadtext")
        self.ql_CtrlEntrada_nacionalidadtext.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_nacionalidadtext.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_nacionalidadtext, 3, 0, 1, 1)

        self.cbox_CtrlEntrada_tipo_2 = QComboBox(EntradaMedicamento)
        self.cbox_CtrlEntrada_tipo_2.addItem("")
        self.cbox_CtrlEntrada_tipo_2.addItem("")
        self.cbox_CtrlEntrada_tipo_2.addItem("")
        self.cbox_CtrlEntrada_tipo_2.setObjectName(u"cbox_CtrlEntrada_tipo_2")
        self.cbox_CtrlEntrada_tipo_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlEntrada_tipo_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.cbox_CtrlEntrada_tipo_2, 3, 3, 1, 1)

        self.qlinee_CtrlEntrada_cedulainfo = QLineEdit(EntradaMedicamento)
        self.qlinee_CtrlEntrada_cedulainfo.setObjectName(u"qlinee_CtrlEntrada_cedulainfo")
        self.qlinee_CtrlEntrada_cedulainfo.setBaseSize(QSize(0, 0))
        self.qlinee_CtrlEntrada_cedulainfo.setCursor(QCursor(Qt.IBeamCursor))
        self.qlinee_CtrlEntrada_cedulainfo.setFocusPolicy(Qt.WheelFocus)
        self.qlinee_CtrlEntrada_cedulainfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_CtrlEntrada_cedulainfo.setFrame(True)

        self.gridLayout_2.addWidget(self.qlinee_CtrlEntrada_cedulainfo, 0, 1, 1, 1)

        self.cbox_CtrlEntrada_estadoinfo = QComboBox(EntradaMedicamento)
        self.cbox_CtrlEntrada_estadoinfo.setObjectName(u"cbox_CtrlEntrada_estadoinfo")
        self.cbox_CtrlEntrada_estadoinfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.cbox_CtrlEntrada_estadoinfo, 5, 1, 1, 1)

        self.ql_CtrlEntrada_fechanactext = QLabel(EntradaMedicamento)
        self.ql_CtrlEntrada_fechanactext.setObjectName(u"ql_CtrlEntrada_fechanactext")
        self.ql_CtrlEntrada_fechanactext.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_fechanactext.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_fechanactext, 4, 2, 1, 1)

        self.ql_CtrlEntrada_tipotext = QLabel(EntradaMedicamento)
        self.ql_CtrlEntrada_tipotext.setObjectName(u"ql_CtrlEntrada_tipotext")
        self.ql_CtrlEntrada_tipotext.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_tipotext.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ql_CtrlEntrada_tipotext, 3, 2, 1, 1)

        self.cbox_CtrlEntrada_nacionalidad = QComboBox(EntradaMedicamento)
        self.cbox_CtrlEntrada_nacionalidad.addItem("")
        self.cbox_CtrlEntrada_nacionalidad.addItem("")
        self.cbox_CtrlEntrada_nacionalidad.setObjectName(u"cbox_CtrlEntrada_nacionalidad")
        self.cbox_CtrlEntrada_nacionalidad.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbox_CtrlEntrada_nacionalidad.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.cbox_CtrlEntrada_nacionalidad, 3, 1, 1, 1)

        self.qlinee_CtrlEntrada_fechanacinfo = QDateEdit(EntradaMedicamento)
        self.qlinee_CtrlEntrada_fechanacinfo.setObjectName(u"qlinee_CtrlEntrada_fechanacinfo")
        self.qlinee_CtrlEntrada_fechanacinfo.setLayoutDirection(Qt.LeftToRight)
        self.qlinee_CtrlEntrada_fechanacinfo.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.qlinee_CtrlEntrada_fechanacinfo.setMaximumDate(QDate(2026, 12, 31))
        self.qlinee_CtrlEntrada_fechanacinfo.setMinimumDate(QDate(1910, 1, 1))
        self.qlinee_CtrlEntrada_fechanacinfo.setCalendarPopup(True)
        self.qlinee_CtrlEntrada_fechanacinfo.setDate(QDate(1910, 1, 1))

        self.gridLayout_2.addWidget(self.qlinee_CtrlEntrada_fechanacinfo, 4, 3, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ql_CtrlEntrada_direccioninfo = QLabel(EntradaMedicamento)
        self.ql_CtrlEntrada_direccioninfo.setObjectName(u"ql_CtrlEntrada_direccioninfo")
        self.ql_CtrlEntrada_direccioninfo.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);")
        self.ql_CtrlEntrada_direccioninfo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.ql_CtrlEntrada_direccioninfo)

        self.qplt_CtrlEntrada_direccioninfo = QPlainTextEdit(EntradaMedicamento)
        self.qplt_CtrlEntrada_direccioninfo.setObjectName(u"qplt_CtrlEntrada_direccioninfo")
        self.qplt_CtrlEntrada_direccioninfo.setMaximumSize(QSize(16777215, 40))
        self.qplt_CtrlEntrada_direccioninfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.qplt_CtrlEntrada_direccioninfo)


        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 6, 0, 1, 1)

        QWidget.setTabOrder(self.qlinee_CtrlEntrada_cedulainfo, self.qlinee_CtrlEntrada_nombreinfo)
        QWidget.setTabOrder(self.qlinee_CtrlEntrada_nombreinfo, self.qlinee_CtrlEntrada_apellidosinfo)
        QWidget.setTabOrder(self.qlinee_CtrlEntrada_apellidosinfo, self.cbox_CtrlEntrada_nacionalidad)
        QWidget.setTabOrder(self.cbox_CtrlEntrada_nacionalidad, self.cbox_CtrlEntrada_tipo_2)
        QWidget.setTabOrder(self.cbox_CtrlEntrada_tipo_2, self.qlinee_CtrlEntrada_telefonoinfo)
        QWidget.setTabOrder(self.qlinee_CtrlEntrada_telefonoinfo, self.qlinee_CtrlEntrada_fechanacinfo)
        QWidget.setTabOrder(self.qlinee_CtrlEntrada_fechanacinfo, self.cbox_CtrlEntrada_estadoinfo)
        QWidget.setTabOrder(self.cbox_CtrlEntrada_estadoinfo, self.qplt_CtrlEntrada_direccioninfo)
        QWidget.setTabOrder(self.qplt_CtrlEntrada_direccioninfo, self.cbox_CtrlEntrada_aceptadoporinfo)
        QWidget.setTabOrder(self.cbox_CtrlEntrada_aceptadoporinfo, self.cbox_CtrlEntrada_origenrecipeinfo)
        QWidget.setTabOrder(self.cbox_CtrlEntrada_origenrecipeinfo, self.cbox_CtrlEntrada_encalidaddetextinfo)
        QWidget.setTabOrder(self.cbox_CtrlEntrada_encalidaddetextinfo, self.cbox_CtrlEntrada_entregainfo)
        QWidget.setTabOrder(self.cbox_CtrlEntrada_entregainfo, self.qplt_CtrlEntrada_direccioninfo_2)
        QWidget.setTabOrder(self.qplt_CtrlEntrada_direccioninfo_2, self.tb_tabla)
        QWidget.setTabOrder(self.tb_tabla, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton)

        self.retranslateUi(EntradaMedicamento)
        self.pushButton.clicked.connect(EntradaMedicamento.close)

        self.cbox_CtrlEntrada_encalidaddetextinfo.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(EntradaMedicamento)
    # setupUi

    def retranslateUi(self, EntradaMedicamento):
        EntradaMedicamento.setWindowTitle(QCoreApplication.translate("EntradaMedicamento", u"Entrada de Medicamento", None))
        self.label_17.setText(QCoreApplication.translate("EntradaMedicamento", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">INTRODUZCA LOS DATOS DEL AFILIADO Y EL R\u00c9CIPE M\u00c9DICO</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("EntradaMedicamento", u"            CANTIDAD          \u2588         UNIDAD        \u2588             TIPO        \u2588                                               MEDICAMENTO", None))
        self.ql_CtrlEntrada_origenrecipetext.setText(QCoreApplication.translate("EntradaMedicamento", u"  Origen Recipe  ", None))
        self.cbox_CtrlEntrada_encalidaddetextinfo.setItemText(0, QCoreApplication.translate("EntradaMedicamento", u"Donaci\u00f3n", None))
        self.cbox_CtrlEntrada_encalidaddetextinfo.setItemText(1, QCoreApplication.translate("EntradaMedicamento", u"Pr\u00e9stamo", None))
        self.cbox_CtrlEntrada_encalidaddetextinfo.setItemText(2, QCoreApplication.translate("EntradaMedicamento", u"Ingreso", None))
        self.cbox_CtrlEntrada_encalidaddetextinfo.setItemText(3, QCoreApplication.translate("EntradaMedicamento", u"Compra", None))
        self.cbox_CtrlEntrada_encalidaddetextinfo.setItemText(4, QCoreApplication.translate("EntradaMedicamento", u"Asignaci\u00f3n", None))

        self.ql_CtrlEntrada_entregatext.setText(QCoreApplication.translate("EntradaMedicamento", u"Entrega", None))
        self.cbox_CtrlEntrada_origenrecipeinfo.setItemText(0, QCoreApplication.translate("EntradaMedicamento", u"Seguro Social", None))
        self.cbox_CtrlEntrada_origenrecipeinfo.setItemText(1, QCoreApplication.translate("EntradaMedicamento", u"Hospital", None))
        self.cbox_CtrlEntrada_origenrecipeinfo.setItemText(2, QCoreApplication.translate("EntradaMedicamento", u"Clinica Privada", None))
        self.cbox_CtrlEntrada_origenrecipeinfo.setItemText(3, QCoreApplication.translate("EntradaMedicamento", u"Barrio Adentro", None))
        self.cbox_CtrlEntrada_origenrecipeinfo.setItemText(4, QCoreApplication.translate("EntradaMedicamento", u"IPASME", None))
        self.cbox_CtrlEntrada_origenrecipeinfo.setItemText(5, QCoreApplication.translate("EntradaMedicamento", u"Hospital Civil", None))
        self.cbox_CtrlEntrada_origenrecipeinfo.setItemText(6, QCoreApplication.translate("EntradaMedicamento", u"Cardiol\u00f3gico", None))

        self.ql_CtrlEntrada_aceptadoportext.setText(QCoreApplication.translate("EntradaMedicamento", u"  Aceptado por  ", None))
        self.cbox_CtrlEntrada_aceptadoporinfo.setItemText(0, QCoreApplication.translate("EntradaMedicamento", u"Director", None))
        self.cbox_CtrlEntrada_aceptadoporinfo.setItemText(1, QCoreApplication.translate("EntradaMedicamento", u"Coordinador M\u00e9dico", None))
        self.cbox_CtrlEntrada_aceptadoporinfo.setItemText(2, QCoreApplication.translate("EntradaMedicamento", u"Doctor", None))
        self.cbox_CtrlEntrada_aceptadoporinfo.setItemText(3, QCoreApplication.translate("EntradaMedicamento", u"Sin Autorizaci\u00f3n", None))

        self.cbox_CtrlEntrada_entregainfo.setItemText(0, QCoreApplication.translate("EntradaMedicamento", u"Farmacia", None))
        self.cbox_CtrlEntrada_entregainfo.setItemText(1, QCoreApplication.translate("EntradaMedicamento", u"Administraci\u00f3n", None))
        self.cbox_CtrlEntrada_entregainfo.setItemText(2, QCoreApplication.translate("EntradaMedicamento", u"Director Medico", None))
        self.cbox_CtrlEntrada_entregainfo.setItemText(3, QCoreApplication.translate("EntradaMedicamento", u"Gesti\u00f3n Humana", None))
        self.cbox_CtrlEntrada_entregainfo.setItemText(4, QCoreApplication.translate("EntradaMedicamento", u"Jefe de almac\u00e9n", None))

        self.ql_CtrlEntrada_encalidaddetext.setText(QCoreApplication.translate("EntradaMedicamento", u"  En Calidad de  ", None))
        self.ql_CtrlEntrada_direccioninfo_2.setText(QCoreApplication.translate("EntradaMedicamento", u" Observaci\u00f3n  ", None))
        self.qplt_CtrlEntrada_direccioninfo_2.setPlainText("")
        ___qtablewidgetitem = self.tb_tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EntradaMedicamento", u"Cantidad", None));
        ___qtablewidgetitem1 = self.tb_tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EntradaMedicamento", u"Unidad", None));
        ___qtablewidgetitem2 = self.tb_tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EntradaMedicamento", u"Tipo", None));
        ___qtablewidgetitem3 = self.tb_tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("EntradaMedicamento", u"Medicamento", None));

        __sortingEnabled = self.tb_tabla.isSortingEnabled()
        self.tb_tabla.setSortingEnabled(False)
        self.tb_tabla.setSortingEnabled(__sortingEnabled)
        
        # Agregar los combobox a las celdas de la tablas
             
        comboGrid(self)
        
        #row=0
        #for item in range(self.tb_tabla.rowCount()):
        #        cellinfo=QTableWidgetItem(item)
        #        comboTipo = QComboBox()
        #        comboUnidad=QComboBox()
        #        comboUnidad.addItems(["","Frascos","Unidad","Bolsas","Pares","Paquetes","Sacos/Bultos"])
        #        comboTipo.addItems(["","Agudo","Crónico","OPS"])
        #        
        #        self.tb_tabla.setItem(row, 0, cellinfo)
        #        self.tb_tabla.setCellWidget(row, 2, comboTipo)
        #        self.tb_tabla.setCellWidget(row,1,comboUnidad)
        #        row += 1


        self.pushButton_2.setText(QCoreApplication.translate("EntradaMedicamento", u"Guardar", None))
        self.pushButton.setText(QCoreApplication.translate("EntradaMedicamento", u"Salir", None))
        self.qlinee_CtrlEntrada_nombreinfo.setInputMask(QCoreApplication.translate("EntradaMedicamento", u">aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", None))
        self.qlinee_CtrlEntrada_nombreinfo.setPlaceholderText("")
        self.ql_CtrlEntrada_apellidostext.setText(QCoreApplication.translate("EntradaMedicamento", u"Apellidos", None))
        self.ql_CtrlEntrada_estadotext.setText(QCoreApplication.translate("EntradaMedicamento", u" Estado ", None))
        self.qlinee_CtrlEntrada_apellidosinfo.setInputMask(QCoreApplication.translate("EntradaMedicamento", u">aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", None))
        self.ql_CtrlEntrada_telefonotext.setText(QCoreApplication.translate("EntradaMedicamento", u" Telefono ", None))
        self.ql_CtrlEntrada_cedulatext.setText(QCoreApplication.translate("EntradaMedicamento", u"Cedula", None))
        self.ql_CtrlEntrada_nombrestext.setText(QCoreApplication.translate("EntradaMedicamento", u"Nombres", None))
        self.qlinee_CtrlEntrada_telefonoinfo.setInputMask(QCoreApplication.translate("EntradaMedicamento", u"(9999)-(99999999)", None))
        self.ql_CtrlEntrada_nacionalidadtext.setText(QCoreApplication.translate("EntradaMedicamento", u"Nacionalidad", None))
        self.cbox_CtrlEntrada_tipo_2.setItemText(0, QCoreApplication.translate("EntradaMedicamento", u"Beneficiado", None))
        self.cbox_CtrlEntrada_tipo_2.setItemText(1, QCoreApplication.translate("EntradaMedicamento", u"Afiliado", None))
        self.cbox_CtrlEntrada_tipo_2.setItemText(2, QCoreApplication.translate("EntradaMedicamento", u"Labor Social", None))

        self.qlinee_CtrlEntrada_cedulainfo.setInputMask(QCoreApplication.translate("EntradaMedicamento", u"99999999999999", None))
        self.qlinee_CtrlEntrada_cedulainfo.setText("")
        self.cbox_CtrlEntrada_estadoinfo.setPlaceholderText("")
        self.ql_CtrlEntrada_fechanactext.setText(QCoreApplication.translate("EntradaMedicamento", u" Fecha Nac. ", None))
        self.ql_CtrlEntrada_tipotext.setText(QCoreApplication.translate("EntradaMedicamento", u"Tipo", None))
        self.cbox_CtrlEntrada_nacionalidad.setItemText(0, QCoreApplication.translate("EntradaMedicamento", u"V", None))
        self.cbox_CtrlEntrada_nacionalidad.setItemText(1, QCoreApplication.translate("EntradaMedicamento", u"E", None))

        self.qlinee_CtrlEntrada_fechanacinfo.setDisplayFormat(QCoreApplication.translate("EntradaMedicamento", u"dd/MM/yyyy", None))
        self.ql_CtrlEntrada_direccioninfo.setText(QCoreApplication.translate("EntradaMedicamento", u"Direcci\u00f3n", None))
        self.qplt_CtrlEntrada_direccioninfo.setPlainText(QCoreApplication.translate("EntradaMedicamento", u"Introduzca su direcci\u00f3n...", None))
    # retranslateUi

#  ***************************************************************************************************************