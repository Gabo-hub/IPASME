from PySide2.QtWidgets import QMessageBox
from PySide2.QtGui import *
from PySide2.QtCore import *
from views.resources_rc import *



def MensajeCaja(self,titulo,texto,tipo): 
    self.tipo=tipo
    self.msg = QMessageBox(self)
    icon = QIcon()
    icon.addFile(u":/logo_ipasme/icons/IPASME-logo-DABC2AE9B1-seeklogo.com.png", QSize(), QIcon.Normal, QIcon.Off)
    self.msg.setWindowTitle(titulo)
    self.msg.setText(texto)
    #self.msg.setStyle(u"background-color: rgb(177, 214, 166);")
    



    if self.tipo == 1:
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setIcon(self.msg.Information) 
    elif self.tipo == 2:
        self.msg.setIcon(self.msg.Question)  
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

    self.msg.setWindowIcon(icon)
    self.msg.setStyleSheet("background-color: rgb(223, 223, 223);")
    #self.msg.setStyleSheet("background-color: rgb(240, 240, 240); \n QMessageBox{\n color:rgb(255, 255, 255); \n background-color: rgb(71, 93, 144);}")
    
    respuestaMensaje=self.msg.exec_()

    if respuestaMensaje==QMessageBox.Yes:
        return 1  
    else:
        return 2

    