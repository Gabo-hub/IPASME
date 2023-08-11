from PySide2.QtWidgets import QApplication
from controllers.login import LoginIpasme
from controllers.main_windows import MainWindows


if __name__ == "__main__":
    app = QApplication()
    Dialog = LoginIpasme()
    Dialog.show()
    app.exec_()



   
    #******************************************

    # FALTA COLOCAR LOS NOMBRES EN MAYUSCULA
    
    
    