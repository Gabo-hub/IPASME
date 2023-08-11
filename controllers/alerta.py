from PySide2.QtWidgets import QMessageBox
from PySide2.QtGui import *
from PySide2.QtCore import *

msg = QMessageBox()

def MensajeCaja(titulo,texto): 
    msg.setWindowTitle(titulo)
    msg.setText(texto)
    msg.setIcon(msg.Warning)
    msg.setStyleSheet("background-color: rgb(240, 240, 240);")
    x = msg.exec_()