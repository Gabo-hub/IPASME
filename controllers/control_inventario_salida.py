from views.control_inventario_salida import Ui_ContrlSalida
from controllers.caja_mensajes import MensajeCaja
from PySide2.QtWidgets import QDialog, QMessageBox
from PySide2.QtGui import *
from PySide2.QtCore import *

class ContrlSalida(QDialog, Ui_ContrlSalida):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.pushButton_2.clicked.connect(self.activarmodificacion)
        self.pushButton.clicked.connect(self.messagebox)

    def activarmodificacion(self):
        if self.BodyFrame.isEnabled():
            self.BodyFrame.setEnabled(False)
        else:
            self.BodyFrame.setEnabled(True)
    def messagebox(self):
        if not self.FooterFrame.isEnabled():
            a = MensajeCaja("Comenzar Edición", "¿Desea egresar datos adicionales?")
        
            if a:
                self.FooterFrame.setEnabled(True)
            else:
                return
        else:
            a = MensajeCaja("Cancelar Edición", "¿Desea cancelar la edicion de egresos?")
            
            if a:
                self.FooterFrame.setEnabled(True)
            else:
                return