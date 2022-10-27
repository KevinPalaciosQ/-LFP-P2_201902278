from pydoc import text
from re import A
from Token import *
from Error import *
class Analizadorr:
    def __init__(self):
        self.ListaTokens = []
        self.ListaErrores = []

    #Método para reconocer decimales
    def AutomataFinitoDecimal(self, caracter):
        Estado_aceptacion = [2]
        MiEstado = 0
        for abc in caracter:
            if MiEstado ==0:
                if abc.isdigit():
                    MiEstado = 1
                else:
                    MiEstado = -1
            elif MiEstado == 1:
                if abc.isdigit():
                    MiEstado = 1
                elif abc == ".":
                    MiEstado = 2
                else:
                    MiEstado =-1
            elif MiEstado == 2:
                if abc.isdigit():
                    MiEstado = 2
                else:
                    MiEstado = -1
            elif MiEstado ==-1:
                return False
        return MiEstado in Estado_aceptacion

    def AnalisisLexico1(self, dato):
        self.ListaTokens = []
        self.ListaErrores = []
        contador = 0
        linea = 1
        columna = 1
        lector = ""#buffer
        estado="S0"#ESTADO INICIAL PARA PALABRAS RESERVADAS
        while contador<len(dato):
            abc=dato[contador]
            #INICIO ESTADO S0-------TOKENS
            if estado == "S0":
                if (abc == "!"):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"!","T_Exclamacion",linea,columna))
                    lector=""
                    estado="S0"
                elif (abc == "<"):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"<","T_MENORQUE",linea,columna))
                    lector=""
                    estado="S0"             
                elif (abc == ">"):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,">","T_MAYORQUE",linea,columna))
                    lector=""
                    estado="S0"  
                elif (abc == "-"):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"-","T_Guion",linea,columna))
                    lector=""
                    estado="S0"
                elif (abc == ";"):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,";","T_PuntoComa",linea,columna))
                    lector=""
                    estado="S0"
                elif (abc == "."):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,".","T_Punto",linea,columna))
                    lector=""
                    estado="S0"  
                elif (abc == "("):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"(","T_PARABRE",linea,columna))
                    lector=""
                    estado="S0"
                elif (abc == ")"):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,")","T_PARCIERRA",linea,columna))
                    lector=""
                    estado="S0" 
                elif (abc == ","):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,",","T_Coma",linea,columna))
                    lector=""
                    estado="S0"   
                elif (abc.isalpha()) and (not abc.isdigit()):#ISALPHA ENCUENTRA PALABRA Y ALMACENA
                    lector=abc
                    columna+=1
                    estado="S1"
                elif (abc.isdigit()):#ISDIGIT ENCUENTRA DIGITOS Y ALMACENA
                    lector=abc
                    columna+=1
                    estado="S2"
                elif abc == '\n':
                    columna = 1
                    linea +=1
                elif abc == ' ':#" " espacio en blanco
                    columna+=1
                elif abc == '\t' or abc=="\r":
                    columna+=1
                else:
                    self.ListaErrores.append(Error(lector,"Error",linea,columna))
                    lector=""
                    columna+=1
            #INICIO ESTADO S1
            elif estado == "S1" :#PUEDEN VENIR LETRAS O NUMEROS O ALGUN ASCII
                if (abc.isalpha()):
                    lector+=abc
                    columna+=1
                    estado="S1"
                else:
                    if abc=="Controles":
                        self.ListaTokens.append(Token(lector,"Controles","TCONTROLES",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif abc=="propiedades":
                        self.ListaTokens.append(Token(lector,"propiedades","TPROPIEDADES",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif abc=="Colocacion":
                        self.ListaTokens.append(Token(lector,"Colocacion","TCOLOCACION",linea,columna))
                        lector=""
                        estado="S0"     
                        contador-=1
                    elif abc=="Etiqueta":
                        self.ListaTokens.append(Token(lector,"Etiqueta","TETIQUETA",linea,columna))
                        lector=""
                        estado="S0"   
                        contador-=1    
                    elif abc=="Boton":
                        self.ListaTokens.append(Token(lector,"Boton","TBOTON",linea,columna))
                        lector=""
                        estado="S0"  
                        contador-=1     
                    elif abc=="Check":
                        self.ListaTokens.append(Token(lector,"Check","TCHECK",linea,columna))
                        lector=""
                        estado="S0"   
                        contador-=1    
                    elif abc=="RadioBoton": 
                        self.ListaTokens.append(Token(lector,"RadioBoton","TRADIOBOTON",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif abc=="Texto":    
                        self.ListaTokens.append(Token(lector,"Texto","TTexto",linea,columna))
                        lector=""
                        estado="S0"  
                        contador-=1   
                    elif abc=="AreaTexto":        
                        self.ListaTokens.append(Token(lector,"AreaTexto","TAREATEXTO",linea,columna))
                        lector=""
                        estado="S0"    
                        contador-=1       
                    elif abc=="Clave": 
                        self.ListaTokens.append(Token(lector,"Clave","TCLAVE",linea,columna))
                        lector=""
                        estado="S0" 
                        contador-=1                                                           
                    elif abc=="Contenedor":
                        self.ListaTokens.append(Token(lector,"Contenedor","TCONTENEDOR",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif abc=="setColorLetra":
                        self.ListaTokens.append(Token(lector,"setColorLetra","T_SETCOLORLETRA",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif abc=="setTexto":
                        self.ListaTokens.append(Token(lector,"setTexto","T_SETTEXTO",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif abc=="setAlineacion":
                        self.ListaTokens.append(Token(lector,"setAlineacion","T_SETALINEACION",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif abc=="setColorFondo":
                        self.ListaTokens.append(Token(lector,"setColorFondo","T_SETCOLORFONDO",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif abc=="setMarcada":
                        self.ListaTokens.append(Token(lector,"setMarcada","T_SETMARCADA",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif abc=="setGrupo":
                        self.ListaTokens.append(Token(lector,"setGrupo","T_SETGRUPO",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif abc=="setAncho":
                        self.ListaTokens.append(Token(lector,"setAncho","T_SETANCHO",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1  
                    elif abc=="setAlto":
                        self.ListaTokens.append(Token(lector,"setAlto","T_SETALTO",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif abc=="setPosicion":
                        self.ListaTokens.append(Token(lector,"setPosicion","T_SETPOSICION",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif abc=="add":
                        self.ListaTokens.append(Token(lector,"add","T_ADD",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif abc=="this":
                        self.ListaTokens.append(Token(lector,"this","T_THIS",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif abc=="Centro":
                        self.ListaTokens.append(Token(lector,"Centro","T_CENTRO",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1   
                    elif abc=="Izquierdo":
                        self.ListaTokens.append(Token(lector,"Izquierdo","T_IZQUIERDO",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1   
                    elif abc=="Derecho":
                        self.ListaTokens.append(Token(lector,"Derecho","T_DERECHO",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1   
                    elif abc=="true":
                        self.ListaTokens.append(Token(lector,"true","T_TRUE",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1    
                    elif abc=="false":
                        self.ListaTokens.append(Token(lector,"false","T_FALSE",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1  
                    else:
                        self.ListaErrores.append(Error(lector,"Error",linea,columna))
                        lector=""
                        columna+=1
            #INICIO ESTADO S2     
            elif estado == "S2":#Numeros
                if abc.isdigit():
                    lector+=abc
                    columna+=1
                    estado="S2"
                elif abc == ".":
                    lector+=abc
                    columna+=1
                    estado="S2"
                else:
                    if self.AutomataFinitoDecimal(abc):
                        self.ListaTokens.append(Token(lector,"Double","\d\d*\.\d\d*",linea,columna))
                    else:
                        self.ListaTokens.append(Token(lector,"Entero","\d\d*",linea,columna))
                    lector = ""
                    contador -= 1
                    estado = "S0"
            #INICIO ESTADO S3
            elif estado == "S3":#CONTENIDO ENTRE ABREVIATURAS
                if abc != "<":
                    lector += abc
                    columna += 1
                    estado = "S3"

                elif abc == "\n":
                    lector += abc
                    linea += 1
                    columna = 1
                    estado = "S3"

                else:
                    self.ListaTokens.append(Token(lector, "cadena", ".[^<]", linea, columna))
                    lector = ""
                    estado = "S0"
                    contador -= 1

            contador+=1

    def impresion(self):
        print("TOKENS: ")
        for Tokkens in self.ListaTokens:
            Tokkens.ver()
        print("")
        print("ERRORES: ")
        for Errrores in self.ListaErrores:
            Errrores.vererrores()
        print("Cantidad de Tokens en el Texto: "+str(len(self.ListaTokens)))
        print("Cantidad de Errores en el Texto: "+str(len(self.ListaErrores)))