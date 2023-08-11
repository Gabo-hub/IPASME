
from views.entrega_de_medicamentos import Ui_EntradaMedicamento
from PySide2.QtWidgets import QWidget,QMessageBox
from PySide2.QtGui import *
from PySide2.QtCore import *
from db.connect import *
from controllers.caja_mensajes import *


class EntradaMedicamento(QWidget, Ui_EntradaMedicamento):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.afiliadoEsNuevo=0       
        #Variables
        self.conector = conectarse()
        #Lista para tomar la informacion deacuerdo a mi tabla # .text() Qlinees | currentIndex() + 1 QComboBox
        self.listahijo = ["int(self.qlinee_CtrlEntrada_cedulainfo.text())","self.qlinee_CtrlEntrada_nombreinfo.text()",
        "self.qlinee_CtrlEntrada_apellidosinfo.text()","self.cbox_CtrlEntrada_nacionalidad.currentText()",
        "self.cbox_CtrlEntrada_tipo_2.currentIndex() + 1","self.qlinee_CtrlEntrada_telefonoinfo.text()",
        "self.qlinee_CtrlEntrada_fechanacinfo.text()","self.cbox_CtrlEntrada_estadoinfo.currentIndex() + 1",
        "self.qplt_CtrlEntrada_direccioninfo.toPlainText()","self.cbox_CtrlEntrada_aceptadoporinfo.currentIndex() + 1",
        "self.cbox_CtrlEntrada_origenrecipeinfo.currentIndex() + 1","self.cbox_CtrlEntrada_encalidaddetextinfo.currentIndex() + 1",
        "self.cbox_CtrlEntrada_entregainfo.currentIndex() + 1","self.qplt_CtrlEntrada_direccioninfo_2.toPlainText()"]
                                                                #LO DE ARRIBA ES PROVICIONAL
        
        #Funciones para agregar lista de estado al Combo Box
        self.listaestado = "SELECT * FROM public.estados"
        self.cargarinfo = consultardb(self.conector, self.listaestado)
        self.listadoComboBox= dict(self.cargarinfo)
        self.valores = list(self.listadoComboBox.values())
        self.cbox_CtrlEntrada_estadoinfo.addItems(self.valores)
        self.cbox_CtrlEntrada_estadoinfo.setCurrentIndex(-1)
         
         # Evento para controlar la entrada de datos según su tipo

        self.Validador = QRegExpValidator(QRegExp("[1-9]\\d{0,10}"),self)
        self.qlinee_CtrlEntrada_cedulainfo.setValidator(self.Validador)
        self.Validador = QRegExpValidator(QRegExp("[A-Za-z áéíóú]*"),self)
        self.qlinee_CtrlEntrada_apellidosinfo.setValidator(self.Validador)
        self.qlinee_CtrlEntrada_nombreinfo.setValidator(self.Validador)

        # Control de eventos de los botones 
        #         
        self.pushButton_2.clicked.connect(self.confirmar_ingreso)
 

        self.qlinee_CtrlEntrada_cedulainfo.editingFinished.connect(self.Buscar)
        
        
        ############################### Cambio de colo de fondo en los campos ##############################
    def cambioColorFondo(self,color):
        self.color=color 
        self.qlinee_CtrlEntrada_nombreinfo.setStyleSheet(self.color)
        self.qlinee_CtrlEntrada_apellidosinfo.setStyleSheet(self.color)
        self.cbox_CtrlEntrada_nacionalidad.setStyleSheet(self.color)
        self.cbox_CtrlEntrada_tipo_2.setStyleSheet(self.color)
        self.qlinee_CtrlEntrada_telefonoinfo.setStyleSheet(self.color)
        self.qplt_CtrlEntrada_direccioninfo.setStyleSheet(self.color)
        self.qlinee_CtrlEntrada_fechanacinfo.setStyleSheet(self.color)
        self.cbox_CtrlEntrada_estadoinfo.setStyleSheet(self.color)

    # Definir el estado de los campos Habilitado o NO
    def habilitarObjetos(self,estado):
        
        self.qlinee_CtrlEntrada_nombreinfo.setEnabled(estado)
        self.qlinee_CtrlEntrada_apellidosinfo.setEnabled(estado)
        self.cbox_CtrlEntrada_nacionalidad.setEnabled(estado)
        self.cbox_CtrlEntrada_tipo_2.setEnabled(estado)
        self.qlinee_CtrlEntrada_telefonoinfo.setEnabled(estado)
        self.qplt_CtrlEntrada_direccioninfo.setEnabled(estado)
        self.qlinee_CtrlEntrada_fechanacinfo.setEnabled(estado)
        self.cbox_CtrlEntrada_estadoinfo.setEnabled(estado)

    def limpiarObjetos(self):
        self.qlinee_CtrlEntrada_nombreinfo.setText("")
        self.qlinee_CtrlEntrada_apellidosinfo.setText("")
        self.cbox_CtrlEntrada_nacionalidad.setCurrentText("V")
        self.cbox_CtrlEntrada_tipo_2.setCurrentIndex(-1)
        self.qlinee_CtrlEntrada_telefonoinfo.setText("")
        self.qplt_CtrlEntrada_direccioninfo.setPlainText("Introduzca su dirección...")
        self.qlinee_CtrlEntrada_fechanacinfo.setDate(QDate(1910, 1,1))
        self.cbox_CtrlEntrada_estadoinfo.setCurrentIndex(-1)


    def Buscar(self):
        self.buscarcedula=[]
        self.buscarcedula = f"SELECT * FROM public.afiliado where cedulaafiliado={self.qlinee_CtrlEntrada_cedulainfo.text()} lIMIT 1;"
        self.cargarinfo = consultardb(self.conector, self.buscarcedula)

        #########################################   Limpieza de objetos para refrescar datos
        self.limpiarObjetos()
        ########################################################333

        ###########################        Condicionales para evaluar la busqueda de cedula 
        if self.cargarinfo and (int(self.cargarinfo[0][2])==int(self.qlinee_CtrlEntrada_cedulainfo.text())):
            
            self.LbEjemplo.setText("Ced Existente..")
            self.LbEjemplo.setStyleSheet(u"color: rgb(135,0,0);")
            self.qlinee_CtrlEntrada_cedulainfo.setStyleSheet(u"background-color: rgb(251, 255, 212);")
            self.qlinee_CtrlEntrada_nombreinfo.setText(self.cargarinfo[0][0])
            self.qlinee_CtrlEntrada_apellidosinfo.setText(self.cargarinfo[0][1])
            self.cbox_CtrlEntrada_nacionalidad.setCurrentText(self.cargarinfo[0][9])
            self.cbox_CtrlEntrada_tipo_2.setCurrentIndex(self.cargarinfo[0][6]-1)
            self.qlinee_CtrlEntrada_telefonoinfo.setText(self.cargarinfo[0][3])
            self.qplt_CtrlEntrada_direccioninfo.setPlainText(self.cargarinfo[0][7])
            valorfecha =  self.cargarinfo[0][8].split("/")
            self.qlinee_CtrlEntrada_fechanacinfo.setDate(QDate(int(valorfecha[2]), int(valorfecha[1]), int(valorfecha[0])))
            self.cbox_CtrlEntrada_estadoinfo.setCurrentIndex(self.cargarinfo[0][11]-2)
            
            self.tb_tabla.setFocus()
            self.habilitarObjetos(False)
            self.cambioColorFondo("background-color: rgb(251, 255, 212);")
            #self.cambioColorFondo("QLineEdit { background-color: Red; \n  border: 2px solid Black; \n border-radius: 15px; }")
            # Variable que define 
            self.afiliadoEsNuevo=self.cargarinfo[0][10]  
        else:
            self.LbEjemplo.setText(" Nuevo Registro")
            self.LbEjemplo.setStyleSheet(u"color: rgb(0,0,0);")
            self.qlinee_CtrlEntrada_cedulainfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.cambioColorFondo(u"background-color: rgb(255, 255, 255);")
            self.habilitarObjetos(True)
            self.afiliadoEsNuevo=-1
            


            




        

# Método para registrar el ingreso de los datos, valida los obligatorios y los registra

    def confirmar_ingreso(self):
        
        resultado=MensajeCaja(self,"GUARDAR","¿ DESEA GUARDAR EL NUEVO RECIPE ?",2)                                                                                                                                                                                                                                                                                                                                                                                     
        
        if resultado==1:
            self.guardar_informacion()

           


    #Evento para validar la Información verificando si los campos principales entán vacios
    def guardar_informacion(self):

        self.lista=[]
        def verificacionDeDatos(self): # verificacion de variables 
            # Validación de los campos para que sean de obligatorio almacanamiento **********************

            #Primera validación de celdas en el Grid
            if not self.tb_tabla.item(0,0).text(): #si es nulo o vacio devuelve Falso
                return False
            #Segunda validación para cedula
            elif not self.qlinee_CtrlEntrada_cedulainfo.text(): #si es nulo o vacio devuelve Falso
                return False
            #Validación de nombre de Beneficiario
            elif not self.qlinee_CtrlEntrada_nombreinfo.text(): #si es nulo o vacio devuelve Falso
                return False
            elif self.cbox_CtrlEntrada_estadoinfo.currentIndex()==-1:
                return False 
            else:
                return True

        def verificaElGrig(self):
            
            for i in range(self.tb_tabla.rowCount()-1):
                # Intentamos verificar si hay celdas vacias en caso contrario hay que generar la lista para grabar
                try:
                    if self.tb_tabla.item(i,0).text():
                        if not self.tb_tabla.item(i,0).text() or not self.tb_tabla.cellWidget(i,1).currentText() or not self.tb_tabla.cellWidget(i,2).currentText() or not self.tb_tabla.item(i,3).text():
                            return False
                        else:
                            # Agrega por orden los campos CANTIDAD,UNIDAD,TIPO,NOMBRE MEDICAMENTO
                            xunidad=''
                            if self.tb_tabla.cellWidget(i,1).currentText()=="Frascos":
                                xunidad='1'
                            elif self.tb_tabla.cellWidget(i,1).currentText()=="Unidad":
                                xunidad='2'
                            elif self.tb_tabla.cellWidget(i,1).currentText()=="Bolsas":
                                xunidad='3'
                            elif self.tb_tabla.cellWidget(i,1).currentText()=="Pares":
                                xunidad='4'
                            elif self.tb_tabla.cellWidget(i,1).currentText()=="Paquetes":
                                xunidad='5'
                            elif self.tb_tabla.cellWidget(i,1).currentText()=="Sacos/Bultos":
                                xunidad='6'

                            # Validacion de combobox para tipo de recipe
                                
                            if self.tb_tabla.cellWidget(i,2).currentText()=="Agudo":
                                xTipoR='1'
                            elif self.tb_tabla.cellWidget(i,2).currentText()=="Crónico":
                                xTipoR='2'
                            elif self.tb_tabla.cellWidget(i,2).currentText()=="OPS":
                                xTipoR='3'
                            elif self.tb_tabla.cellWidget(i,2).currentText()=="Otros":
                                xTipoR='4'
                            
                            self.lista.append([xunidad+","+self.tb_tabla.item(i,0).text()+",'"+xTipoR+"','"+self.tb_tabla.item(i,3).text()+"'"])
                except:
                    return False       
                       
            return True



        if verificacionDeDatos(self) and verificaElGrig(self):
            self.listaimprimir = []
            
            #primerValor=self.tb_tabla.item(1,1).text()
            #a=verificacionDeDatos()
            #print (primerValor)

            for i in self.listahijo:
                self.listaimprimir.append(eval(i)) #Evalua la informacion de los qLineText
            
            if self.afiliadoEsNuevo==-1:
                xGuardarAfiliado=f"""insert into afiliado (nombresafiliado,apellidosafiliado,cedulaafiliado,telefonoafiliado,telefonocasaafiliado,dependencia,idtipoafiliado,direccionafiliado,fnacimientoafiliado,nacionalidadafiliado,idestado)  
                values ('{self.listaimprimir[1]}','{self.listaimprimir[2]}',{self.listaimprimir[0]}, '{self.listaimprimir[5]}','{self.listaimprimir[5]}','ESCUELA', {self.listaimprimir[4]},'{self.listaimprimir[8]}', '{self.listaimprimir[6]}','{self.listaimprimir[3]}',{self.listaimprimir[7]+1}) """
                self.guardando = guardardb(self.conector, xGuardarAfiliado)   
                self.conector.connection.commit()
                xGuardarRecipe=f""" insert into recipe(frecipe,idafiliado,identregapor,idcalidadde, idorigenrecipe,idpreviafirma,observaciones) 
                                    values (CURRENT_TIMESTAMP,(select max(idafiliado) from afiliado),{self.listaimprimir[12]},{self.listaimprimir[11]},{self.listaimprimir[10]},{self.listaimprimir[9]},'{self.listaimprimir[13]}');"""
            else:
                xGuardarRecipe=f""" insert into recipe(frecipe,idafiliado,identregapor,idcalidadde, idorigenrecipe,idpreviafirma,observaciones) 
                                    values (CURRENT_TIMESTAMP,{self.afiliadoEsNuevo},{self.listaimprimir[12]},{self.listaimprimir[11]},{self.listaimprimir[10]},{self.listaimprimir[9]},'{self.listaimprimir[13]}');
                                    select max(idrecipe) from recipe; """
            self.guardando = guardardb(self.conector, xGuardarRecipe)   

            
            if self.guardando!=None:
                self.numeroRecipe= self.guardando[0][0]
            else:
                self.numeroRecipe=0

            

            self.conector.connection.commit()

            for i in range(len(self.lista)):
                xGuardarMedicamento=f"""insert into  medicamento (idrecipe,cantidad,idunidad,tipo,nombremed) 
                values ((select max(idrecipe) from recipe),{self.lista[i][0]}); """
                self.guardando = guardardb(self.conector, xGuardarMedicamento)   
                self.conector.connection.commit()

            self.resultado=MensajeCaja(self,"GUARDAR",f"LOS DATOS FUERON REGISTRADOS CON ÉXITO, RECIPE N° {self.numeroRecipe}",1)
            self.cambioColorFondo(u"background-color: rgb(255, 255, 255);")
            self.habilitarObjetos(True)
            self.afiliadoEsNuevo=-1
            self.LbEjemplo.setText(" Nuevo Registro")
            self.qlinee_CtrlEntrada_cedulainfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.qlinee_CtrlEntrada_cedulainfo.setText("")
            self.limpiarObjetos()
            self.qlinee_CtrlEntrada_cedulainfo.setFocus()
            return True
        else:
            
            self.resultado=MensajeCaja(self,"ERROR INFORMACION INCOMPLETA","POR FAVOR, RELLENE LOS CAMPOS VACIOS",1)
            #return False

         

