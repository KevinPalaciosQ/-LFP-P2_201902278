from xml.dom.minidom import CharacterData
from Token import *
from Error import *
class analizador_lexico():
    def __init__(self):
        self.ListaTokens = []
        self.ListaErrores = []
    def AutomataFinitoDecimal(self, caracter):
            EstadoAceptacion = [2]
            MiEstado = 0
            for abc in caracter:
                if MiEstado == 0:
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
            return MiEstado in EstadoAceptacion
    def analizar(self, parametro):
        self.ListaTokens = []
        self.ListaErrores = []
        contador = 0
        linea = 1
        columna = 1
        lector = ""
        estado = "S0"  #Estado Inicial del automata
        while(contador < len(parametro)):
            abc = parametro[contador]
#-------------------------------Estado=S0--------------------------------------------------
# estado para todos los simbolos; estado de aceptacion
            if estado == "S0":  
                if(abc == "<"):
                    lector = abc
                    columna += 1
                    self.ListaTokens.append(Token("T_MENORQUE", lector, linea, columna))
                    lector = ""
                    estado = "S0"
                elif(abc == ">"):
                    lector = abc
                    columna += 1
                    self.ListaTokens.append(Token("T_MAYORQUE", lector, linea, columna))
                    lector = ""
                    estado = "S0"
                elif(abc == ","):
                    lector = abc
                    columna += 1
                    self.ListaTokens.append(Token("T_COMA",lector, linea, columna))
                    lector = ""
                    estado = "S0"
                elif(abc == "/"):
                    lector+= abc
                    columna += 1
                    estado = "S3"
                elif(abc == '"'):
                    lector+= abc
                    columna += 1
                    estado = "S6"
                elif(abc == "."):
                    lector = abc
                    columna += 1
                    self.ListaTokens.append(Token("T_PUNTO", lector, linea, columna))
                    lector = ""
                    estado = "S0"
                elif(abc == ";"):
                    lector = abc
                    columna += 1
                    self.ListaTokens.append(Token("T_PUNTOCOMA", lector, linea, columna))
                    lector = ""
                    estado = "S0"
                elif(abc == "!"):
                    lector = abc
                    columna += 1
                    self.ListaTokens.append(Token("T_Exclamacion", lector, linea, columna))
                    lector = ""
                    estado = "S0"
                elif(abc == "-"):
                    lector = abc
                    columna += 1
                    self.ListaTokens.append(Token("T_GUION", lector, linea, columna))
                    lector = ""
                    estado = "S0"
                elif(abc == "("):
                    lector = abc
                    columna += 1
                    self.ListaTokens.append(Token("T_PARABRE", lector, linea, columna))
                    lector = ""
                    estado = "S0"
                elif(abc == ")"):
                    lector = abc
                    columna += 1
                    self.ListaTokens.append(Token("T_PARCIERRA", lector, linea, columna))
                    lector = ""
                    estado = "S0"
                elif(abc == "\n"):  # aumentar la linea
                    linea += 1
                    columna = 1
                elif(abc == " "):
                    columna += 1
                elif(abc == "\t"):
                    columna += 1
                elif(abc == "\r"):
                    pass
                elif (abc.isalpha()) and (not abc.isdigit()):#ISALPHA ENCUENTRA PALABRA Y ALMACENA
                    lector=abc
                    columna+=1
                    estado="S1"
                elif(abc == '"'):  # si letra es comilla doble para cadena xd
                    lector = abc
                    columna += 1
                    estado = "S3"
                elif abc.isdigit():
                    lector = abc
                    columna +=1
                    estado = "S2"
                else:
                    self.ListaErrores.append(Error(abc, "Error Léxico", linea, columna))
                    lector = ""
                    columna += 1
#-------------------------------Estado=S1--------------------------------------------------
#Estado Utilizado para almacenar Palabras Reservadas/Tokens
            elif estado == "S1" :#PUEDEN VENIR LETRAS O CADENAS
                if (abc.isalpha())  or ( abc=="_"):
                    lector+=abc
                    columna+=1
                    estado="S1"
                else:
                    if (lector == "Controles"):
                        self.ListaTokens.append(Token("T_CONTROLES",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "propiedades"):
                        self.ListaTokens.append(Token("T_PROPIEDADES",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "Colocacion"):
                        self.ListaTokens.append(Token("T_COLOCACION",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "setColorLetra"):
                        self.ListaTokens.append(Token("T_SETCOLORLETRA",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "setTexto"):
                        self.ListaTokens.append(Token("T_SETTEXTO",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "setAlineacion"):
                        self.ListaTokens.append(Token("T_SETALINEACION",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "setColorFondo"):
                        self.ListaTokens.append(Token("T_SETCOLORFONDO",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "setMarcada"):
                        self.ListaTokens.append(Token("T_SETMARCADA",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "setGrupo"):
                        self.ListaTokens.append(Token("T_SETGRUPO",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "setAncho"):
                        self.ListaTokens.append(Token("T_SETANCHO",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1  
                    elif (lector == "setAlto"):
                        self.ListaTokens.append(Token("T_SETALTO",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1   
                    elif (lector == "setPosicion"):
                        self.ListaTokens.append(Token("T_SETPOSICION",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "add"):
                        self.ListaTokens.append(Token("T_ADD",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1     
                    elif (lector == "this"):
                        self.ListaTokens.append(Token("T_THIS",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "Centro"):
                        self.ListaTokens.append(Token("T_CENTRO",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "Izquierdo"):
                        self.ListaTokens.append(Token("T_IZQUIERDO",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "Derecho"):
                        self.ListaTokens.append(Token("T_DERECHO",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "true"):
                        self.ListaTokens.append(Token("T_TRUE",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "false"):
                        self.ListaTokens.append(Token("T_FALSE",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1  
                    elif (lector == "Etiqueta"):
                        self.ListaTokens.append(Token("TETIQUETA",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1 
                    elif (lector == "Boton"):
                        self.ListaTokens.append(Token("TBOTON",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "Check"):
                        self.ListaTokens.append(Token("TCHECK",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "RadioBoton"):
                        self.ListaTokens.append(Token("TRADIOBOTON",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "Texto"):
                        self.ListaTokens.append(Token("TTexto",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "AreaTexto"):
                        self.ListaTokens.append(Token("TAREATEXTO",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector== "Clave"):
                        self.ListaTokens.append(Token("TCLAVE",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "Contenedor"):
                        self.ListaTokens.append(Token("TCONTENEDOR",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    else:
                        self.ListaTokens.append(Token("TIDENTIFICADOR",lector,linea,columna))
                        lector=""
                        columna+=1
                        estado="S0"
#-------------------------------Estado=S2--------------------------------------------------
#Estado Utilizado para almacenar Números sin decimal y con decimal
            elif estado == "S2":
                if abc.isdigit():
                    lector+=abc
                    columna+=1
                    estado="S2"
                elif(abc == "."):
                    lector += abc
                    columna +=1
                    estado ="S2"
                else: 
                    if self.AutomataFinitoDecimal(abc):
                        self.ListaTokens.append(Token("Numero",lector,linea,columna))
                    else:
                        self.ListaTokens.append(Token("Numero",lector,linea,columna))
                    lector = ""
                    contador -= 1
                    estado = "S0"
                    columna+=1
#-------------------------------Estado=S3--------------------------------------------------
            elif estado == "S3":
                if abc =="/":
                    lector+=abc
                    columna +=1
                    estado ="S4"
                elif abc =="*":
                    lector+=abc
                    columna +=1
                    estado ="S5"
                else:
                    lector+=abc
                    columna +=1
                    self.ListaErrores.append(Error(abc, "No Reconocido", linea, columna))
                    lector= ""
                    estado ="S0"
#-------------------------------Estado=S4--------------------------------------------------
#Estado Utilizado para almacenar el comentario simple
            elif estado == "S4":
                if abc =="\n":
                    self.ListaTokens.append(Token("Comentario Simple",lector,linea,columna))
                    columna=1
                    linea+=1
                    lector=""
                    contador -=1
                    estado ="S0"
                else:
                    lector+=abc
                    columna+=1
                    estado ="S4"
#-------------------------------Estado=S5--------------------------------------------------
#Estado utilizado para almacenar comentario Multilinea
            elif estado == "S5":
                if abc =="*":
                    lector+=abc
                    columna+=1
                    if parametro[contador+1]=="/":
                        lector+=parametro[contador+1]
                        columna+=1
                        self.ListaTokens.append(Token("Comentario Multilinea",lector,linea,columna))
                        lector=""
                        estado="S0"
                        contador+=1
                    else:
                        lector+=abc
                        columna+=1
                        estado ="S5"
                elif abc =="\n":
                    lector+=abc
                    columna==1
                    linea+=1
                else:
                    lector+=abc
                    columna+=1
                    estado ="S5"
#-------------------------------Estado=S6--------------------------------------------------
#Estado Encargado de almacenar cadenas de texto " "
            elif estado == "S6":
                if abc =='"':
                    lector+=abc
                    self.ListaTokens.append(Token("Cadena",lector,linea,columna))
                    columna+=1
                    lector=""
                    estado ="S0"
                else:
                    lector+=abc
                    columna+=1
                    estado ="S6"
            contador += 1
        self.ListaTokens.append(Token("EOF","",linea,columna))
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
