from views.login import Ui_Dialog
from PySide2.QtWidgets import QDialog
from PySide2 import QtCore
from PySide2.QtGui import *
from PySide2.QtCore import *
from db.connect import *

class LoginIpasme(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.conector = conectarse()
        self.respuesta = None
        self.bttn_Login_Ingresar.clicked.connect(self.loguear)
        self.bttn_Login_MostrarContra.clicked.connect(self.mostrarcontra)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.buttonBox.accepted.connect(EntradaMedicamento.accept)
        # self.buttonBox.rejected.connect(EntradaMedicamento.reject)
       
    def mostrarcontra(self): 

        if self.bttn_Login_MostrarContra.isChecked():
            icon2 = QIcon()
            icon2.addFile(u"./assets/icons/images.png", QSize(), QIcon.Normal, QIcon.Off)
            self.bttn_Login_MostrarContra.setIcon(icon2)
            self.ql_Login_contrasenainfo.setEchoMode(self.ql_Login_contrasenainfo.Normal)
        else:
            icon2 = QIcon()
            icon2.addFile(u"./assets/icons/descarga.png", QSize(), QIcon.Normal, QIcon.Off)
            self.bttn_Login_MostrarContra.setIcon(icon2)
            self.ql_Login_contrasenainfo.setEchoMode(self.ql_Login_contrasenainfo.Password)

    def loguear(self):
        self.loguearse = self.ql_Login_usuarioinfo.text()+" "+self.ql_Login_contrasenainfo.text()
        xcadena = """SELECT idusuario, usuario, contrasena FROM public.login WHERE usuario||' '||"contrasena"='"""+self.loguearse+"'"
        self.resultado = consultardb(self.conector, xcadena)       

        if self.resultado != None:
            self.close()          
            from controllers.main_windows import MainWindows
            windows = MainWindows(self)
            windows.show()
        else:
            from controllers.alerta import MensajeCaja
            self.ayuda = MensajeCaja("ERROR DE AUTENTICACION", f"EL USUARIO O CONTRASEÑA SON INCORRECTOS.")
            self.respuesta = False