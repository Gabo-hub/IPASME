# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from views.resources_rc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(903, 570)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/logo_ipasme/icons/IPASME-logo-DABC2AE9B1-seeklogo.com.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(94, 133, 185);")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.actionGenerar_Respaldo = QAction(MainWindow)
        self.actionGenerar_Respaldo.setObjectName(u"actionGenerar_Respaldo")
        self.actionCambio_Usuario = QAction(MainWindow)
        self.actionCambio_Usuario.setObjectName(u"actionCambio_Usuario")
        self.actionAdmin_Perfil = QAction(MainWindow)
        self.actionAdmin_Perfil.setObjectName(u"actionAdmin_Perfil")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionRegistro = QAction(MainWindow)
        self.actionRegistro.setObjectName(u"actionRegistro")
        self.actionModificar = QAction(MainWindow)
        self.actionModificar.setObjectName(u"actionModificar")
        self.actionCulminar_Afil = QAction(MainWindow)
        self.actionCulminar_Afil.setObjectName(u"actionCulminar_Afil")
        self.actionCulminar_Afil_2 = QAction(MainWindow)
        self.actionCulminar_Afil_2.setObjectName(u"actionCulminar_Afil_2")
        self.actionReportes = QAction(MainWindow)
        self.actionReportes.setObjectName(u"actionReportes")
        self.actionEntrega_Medicina = QAction(MainWindow)
        self.actionEntrega_Medicina.setObjectName(u"actionEntrega_Medicina")
        self.actionIngreso_de_Medicina = QAction(MainWindow)
        self.actionIngreso_de_Medicina.setObjectName(u"actionIngreso_de_Medicina")
        self.actionReportes_de_Entrega = QAction(MainWindow)
        self.actionReportes_de_Entrega.setObjectName(u"actionReportes_de_Entrega")
        self.actionReporte_de_Entrega = QAction(MainWindow)
        self.actionReporte_de_Entrega.setObjectName(u"actionReporte_de_Entrega")
        self.actionReporte_de_Ingreso = QAction(MainWindow)
        self.actionReporte_de_Ingreso.setObjectName(u"actionReporte_de_Ingreso")
        self.actionEntrada_de_Inventario = QAction(MainWindow)
        self.actionEntrada_de_Inventario.setObjectName(u"actionEntrada_de_Inventario")
        self.actionOrden_de_Salida = QAction(MainWindow)
        self.actionOrden_de_Salida.setObjectName(u"actionOrden_de_Salida")
        self.actionActualizar_Inventario = QAction(MainWindow)
        self.actionActualizar_Inventario.setObjectName(u"actionActualizar_Inventario")
        self.actionReporte = QAction(MainWindow)
        self.actionReporte.setObjectName(u"actionReporte")
        self.actionCreditos_H = QAction(MainWindow)
        self.actionCreditos_H.setObjectName(u"actionCreditos_H")
        self.actionParto_Humanitario = QAction(MainWindow)
        self.actionParto_Humanitario.setObjectName(u"actionParto_Humanitario")
        self.actionCitas_Odontologicas = QAction(MainWindow)
        self.actionCitas_Odontologicas.setObjectName(u"actionCitas_Odontologicas")
        self.actionReportes_2 = QAction(MainWindow)
        self.actionReportes_2.setObjectName(u"actionReportes_2")
        self.actionAyuda = QAction(MainWindow)
        self.actionAyuda.setObjectName(u"actionAyuda")
        self.actionAcerca_de = QAction(MainWindow)
        self.actionAcerca_de.setObjectName(u"actionAcerca_de")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/logo_mercuryweb/icons/mercury-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/logo_mercuryweb/icons/mercury-icon.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(132, 37))
        self.pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 903, 21))
        self.menubar.setStyleSheet(u"background-color: rgb(164, 186, 209);")
        self.menuIPASME = QMenu(self.menubar)
        self.menuIPASME.setObjectName(u"menuIPASME")
        self.menuIPASME.setStyleSheet(u"")
        self.menuAFILIADO = QMenu(self.menubar)
        self.menuAFILIADO.setObjectName(u"menuAFILIADO")
        self.menuFARMACIA = QMenu(self.menubar)
        self.menuFARMACIA.setObjectName(u"menuFARMACIA")
        self.menuINVENTARIO = QMenu(self.menubar)
        self.menuINVENTARIO.setObjectName(u"menuINVENTARIO")
        self.menuBENEFICIOS = QMenu(self.menubar)
        self.menuBENEFICIOS.setObjectName(u"menuBENEFICIOS")
        self.menuAYUDA = QMenu(self.menubar)
        self.menuAYUDA.setObjectName(u"menuAYUDA")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuIPASME.menuAction())
        self.menubar.addAction(self.menuAFILIADO.menuAction())
        self.menubar.addAction(self.menuFARMACIA.menuAction())
        self.menubar.addAction(self.menuINVENTARIO.menuAction())
        self.menubar.addAction(self.menuBENEFICIOS.menuAction())
        self.menubar.addAction(self.menuAYUDA.menuAction())
        self.menuIPASME.addAction(self.actionGenerar_Respaldo)
        self.menuIPASME.addAction(self.actionCambio_Usuario)
        self.menuIPASME.addSeparator()
        self.menuIPASME.addAction(self.actionAdmin_Perfil)
        self.menuIPASME.addAction(self.actionSalir)
        self.menuAFILIADO.addAction(self.actionRegistro)
        self.menuAFILIADO.addAction(self.actionModificar)
        self.menuAFILIADO.addSeparator()
        self.menuAFILIADO.addAction(self.actionCulminar_Afil_2)
        self.menuAFILIADO.addAction(self.actionReportes)
        self.menuFARMACIA.addAction(self.actionEntrega_Medicina)
        self.menuFARMACIA.addAction(self.actionIngreso_de_Medicina)
        self.menuFARMACIA.addSeparator()
        self.menuFARMACIA.addAction(self.actionReporte_de_Entrega)
        self.menuFARMACIA.addAction(self.actionReporte_de_Ingreso)
        self.menuINVENTARIO.addAction(self.actionEntrada_de_Inventario)
        self.menuINVENTARIO.addAction(self.actionOrden_de_Salida)
        self.menuINVENTARIO.addAction(self.actionActualizar_Inventario)
        self.menuINVENTARIO.addSeparator()
        self.menuINVENTARIO.addAction(self.actionReporte)
        self.menuBENEFICIOS.addAction(self.actionCreditos_H)
        self.menuBENEFICIOS.addAction(self.actionParto_Humanitario)
        self.menuBENEFICIOS.addAction(self.actionCitas_Odontologicas)
        self.menuBENEFICIOS.addSeparator()
        self.menuBENEFICIOS.addAction(self.actionReportes_2)
        self.menuAYUDA.addAction(self.actionAyuda)
        self.menuAYUDA.addAction(self.actionAcerca_de)

        self.retranslateUi(MainWindow)
        self.actionSalir.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"IPASME", None))
        self.actionGenerar_Respaldo.setText(QCoreApplication.translate("MainWindow", u"Generar Respaldo", None))
        self.actionCambio_Usuario.setText(QCoreApplication.translate("MainWindow", u"Cambio Usuario", None))
        self.actionAdmin_Perfil.setText(QCoreApplication.translate("MainWindow", u"Administrar Perfil", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionRegistro.setText(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.actionModificar.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.actionCulminar_Afil.setText(QCoreApplication.translate("MainWindow", u"Culminar Afil", None))
        self.actionCulminar_Afil_2.setText(QCoreApplication.translate("MainWindow", u"Culminar Afil", None))
        self.actionReportes.setText(QCoreApplication.translate("MainWindow", u"Reportes", None))
        self.actionEntrega_Medicina.setText(QCoreApplication.translate("MainWindow", u"Entrega Medicina", None))
        self.actionIngreso_de_Medicina.setText(QCoreApplication.translate("MainWindow", u"Ingreso de Medicina", None))
        self.actionReportes_de_Entrega.setText(QCoreApplication.translate("MainWindow", u"Reportes de Entrega", None))
        self.actionReporte_de_Entrega.setText(QCoreApplication.translate("MainWindow", u"Reporte de Entrega", None))
        self.actionReporte_de_Ingreso.setText(QCoreApplication.translate("MainWindow", u"Reporte de Ingreso", None))
        self.actionEntrada_de_Inventario.setText(QCoreApplication.translate("MainWindow", u"Entrada de Inventario", None))
        self.actionOrden_de_Salida.setText(QCoreApplication.translate("MainWindow", u"Orden de Salida", None))
        self.actionActualizar_Inventario.setText(QCoreApplication.translate("MainWindow", u"Actualizar Inventario", None))
        self.actionReporte.setText(QCoreApplication.translate("MainWindow", u"Reporte", None))
        self.actionCreditos_H.setText(QCoreApplication.translate("MainWindow", u"Creditos H", None))
        self.actionParto_Humanitario.setText(QCoreApplication.translate("MainWindow", u"Parto H", None))
        self.actionCitas_Odontologicas.setText(QCoreApplication.translate("MainWindow", u"Citas Odontol\u00f3gicas", None))
        self.actionReportes_2.setText(QCoreApplication.translate("MainWindow", u"Reportes", None))
        self.actionAyuda.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.actionAcerca_de.setText(QCoreApplication.translate("MainWindow", u"Acerca de", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/logo_ipasme/icons/7192de9b3edb2bbe.png\"/></p></body></html>", None))
        self.pushButton.setText("")
        self.menuIPASME.setTitle(QCoreApplication.translate("MainWindow", u"IPASME", None))
        self.menuAFILIADO.setTitle(QCoreApplication.translate("MainWindow", u"AFILIADO", None))
        self.menuFARMACIA.setTitle(QCoreApplication.translate("MainWindow", u"FARMACIA", None))
        self.menuINVENTARIO.setTitle(QCoreApplication.translate("MainWindow", u"INVENTARIO", None))
        self.menuBENEFICIOS.setTitle(QCoreApplication.translate("MainWindow", u"BENEFICIOS", None))
        self.menuAYUDA.setTitle(QCoreApplication.translate("MainWindow", u"AYUDA", None))
    # retranslateUi

