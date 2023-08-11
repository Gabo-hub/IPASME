from views.control_inventario_entrada import Ui_ContrlEntrada
from PySide2.QtWidgets import QDialog
from PySide2.QtGui import *
from PySide2.QtCore import *

class ContrlEntrada(QDialog, Ui_ContrlEntrada):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
