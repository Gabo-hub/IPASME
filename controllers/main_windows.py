from views.main_windows import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import QtCore

class MainWindows(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.actionEntrada_de_Inventario.triggered.connect(self.control_invEntrada)
        self.actionOrden_de_Salida.triggered.connect(self.control_invSalida)
        self.actionEntrega_Medicina.triggered.connect(self.entrega_medicina)

    def control_invEntrada(self):
        from controllers.control_inventario_entrada import ContrlEntrada
        windows = ContrlEntrada(self)
        windows.show()

    def control_invSalida(self):
        from controllers.control_inventario_salida import ContrlSalida
        windows = ContrlSalida(self)
        windows.show()

    def entrega_medicina(self):
        from controllers.entrega_de_medicamento import EntradaMedicamento
        windows = EntradaMedicamento(self)
        windows.show()
