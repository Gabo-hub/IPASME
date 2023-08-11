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

def comboGrid(self):
    
        row=0
        for item in range(self.tb_tabla.rowCount()):
                cellinfo=QTableWidgetItem(item)
                comboTipo = QComboBox()
                comboUnidad=QComboBox()
                comboUnidad.addItems(["","Frascos","Unidad","Bolsas","Pares","Paquetes","Sacos/Bultos"])
                comboTipo.addItems(["","Agudo","Crónico","OPS"])
                comboUnidad.setFrame(False)
                comboTipo.setFrame(False)
                self.tb_tabla.setItem(row, 0, cellinfo)
                self.tb_tabla.setCellWidget(row, 2, comboTipo)
                self.tb_tabla.setCellWidget(row,1,comboUnidad)
                
                row += 1



