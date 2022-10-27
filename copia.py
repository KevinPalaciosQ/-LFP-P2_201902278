from Token import *
from Error import *
class analizador_lexico():
    def __init__(self):
        self.ListaTokens = []
        self.ListaErrores = []
    def AutomataFinitoDecimal(self, caracter):
            EstadoAceptacion = [2]
            MiEstado = 0
            for letra in caracter:
                if MiEstado == 0:
                    if letra.isdigit():
                        MiEstado = 1
                    else:
                        MiEstado = -1
                elif MiEstado == 1:
                    if letra.isdigit():
                        MiEstado = 1
                    elif letra == ".":
                        MiEstado = 2
                    else:
                        MiEstado =-1
                elif MiEstado == 2:
                    if letra.isdigit():
                        MiEstado = 2
                    else:
                        MiEstado = -1
                elif MiEstado ==-1:
                    return False
            return MiEstado in EstadoAceptacion
    def analizar(self, textozz):
        self.ListaTokens = []
        self.ListaErrores = []
        textozz += "&"  # para agregar un dollar para saber donde termina
        contador = 0
        linea = 1
        columna = 1
        buffer = ""
        estado = "S0"  # primer estado
        while(contador < len(textozz)):
            # texto en 0 para la primera letra y asiF
            letra = textozz[contador]
# ==============================estado=S0===================================================
            if estado == "S0":  # estado para todos los simbolos; estado de aceptacion
                if(letra == "<"):
                    buffer = letra
                    columna += 1
                    self.ListaTokens.append(Token("T_MENORQUE", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                elif(letra == ">"):
                    buffer = letra
                    columna += 1
                    self.ListaTokens.append(Token("T_MAYORQUE", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                elif(letra == ","):
                    buffer = letra
                    columna += 1
                    self.ListaTokens.append(Token("T_Coma", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                elif(letra == "."):
                    buffer = letra
                    columna += 1
                    self.ListaTokens.append(Token("T_punto", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                elif(letra == ";"):
                    buffer = letra
                    columna += 1
                    self.ListaTokens.append(Token("T_PuntoComa", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                elif(letra == "!"):
                    buffer = letra
                    columna += 1
                    self.ListaTokens.append(Token("T_Exclamacion", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                elif(letra == "-"):
                    buffer = letra
                    columna += 1
                    self.ListaTokens.append(Token("T_Guion", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                elif(letra == "("):
                    buffer = letra
                    columna += 1
                    self.ListaTokens.append(Token("T_PARABRE", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                elif(letra == ")"):
                    buffer = letra
                    columna += 1
                    self.ListaTokens.append(Token("T_PARCIERRA", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                elif(letra == "\n"):  # aumentar la linea
                    linea += 1
                    columna = 1
                elif(letra == " "):
                    columna += 1
                elif(letra == "\t"):
                    columna += 1
                elif (letra.isalpha()) and (not letra.isdigit()):#ISALPHA ENCUENTRA PALABRA Y ALMACENA
                    buffer=letra
                    columna+=1
                    estado="S1"
                elif(letra == '"'):  # si letra es comilla doble para cadena xd
                    buffer = letra
                    columna += 1
                    estado = "S3"
                elif letra.isdigit():
                    buffer = letra
                    columna +=1
                    estado = "S2"
                elif (letra == '&'):  # para cerrar
                    buffer = letra
                    columna += 1
                    self.ListaTokens.append(Token("Fin de la lectura", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                    print("=========================================")
                else:
                    self.ListaErrores.append(Error(letra, "error lexico", linea, columna))
                    buffer = ""
                    columna += 1
# ======================estado==S1================================================
            elif estado == "S1" :#PUEDEN VENIR LETRAS Y NUMEROS
                if (letra.isalpha())  and (not letra.isdigit()):
                    buffer+=letra
                    columna+=1
                    estado="S1"
                else:
                    if (buffer == "Controles"):
                        self.ListaTokens.append(Token("TCONTROLES",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "propiedades"):
                        self.ListaTokens.append(Token("TPROPIEDADES",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "Colocacion"):
                        self.ListaTokens.append(Token("TCOLOCACION",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "setColorLetra"):
                        self.ListaTokens.append(Token("T_SETCOLORLETRA",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "setTexto"):
                        self.ListaTokens.append(Token("T_SETTEXTO",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "setAlineacion"):
                        self.ListaTokens.append(Token("T_SETALINEACION",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "setColorFondo"):
                        self.ListaTokens.append(Token("T_SETCOLORFONDO",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "setMarcada"):
                        self.ListaTokens.append(Token("T_SETMARCADA",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "setGrupo"):
                        self.ListaTokens.append(Token("T_SETGRUPO",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "setAncho"):
                        self.ListaTokens.append(Token("T_SETANCHO",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1  
                    elif (buffer == "setAlto"):
                        self.ListaTokens.append(Token("T_SETALTO",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1   
                    elif (buffer == "setPosicion"):
                        self.ListaTokens.append(Token("T_SETPOSICION",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "add"):
                        self.ListaTokens.append(Token("T_ADD",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1     
                    elif (buffer == "this"):
                        self.ListaTokens.append(Token("T_THIS",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "Centro"):
                        self.ListaTokens.append(Token("T_CENTRO",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "Izquierdo"):
                        self.ListaTokens.append(Token("T_IZQUIERDO",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "Derecho"):
                        self.ListaTokens.append(Token("T_DERECHO",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "true"):
                        self.ListaTokens.append(Token("T_TRUE",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "false"):
                        self.ListaTokens.append(Token("T_FALSE",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1  
                    elif (buffer == "Etiqueta"):
                        self.ListaTokens.append(Token("TETIQUETA",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1 
                    elif (buffer == "Boton"):
                        self.ListaTokens.append(Token("TBOTON",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "Check"):
                        self.ListaTokens.append(Token("TCHECK",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "RadioBoton"):
                        self.ListaTokens.append(Token("TRADIOBOTON",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "Texto"):
                        self.ListaTokens.append(Token("TTexto",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "AreaTexto"):
                        self.ListaTokens.append(Token("TAREATEXTO",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "Clave"):
                        self.ListaTokens.append(Token("TCLAVE",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    elif (buffer == "Contenedor"):
                        self.ListaTokens.append(Token("TCONTENEDOR",buffer,linea,columna))
                        buffer=""
                        estado="S0"
                        contador-=1
                    #elif (buffer == "//"):#######hola
                    #    pass
                    else:
                        self.ListaErrores.append(Error(buffer,"Error Léxico",linea,columna))
                        buffer=""
                        columna+=1
# ===========================ESTADO=S2=================================================
            elif estado == "S2":
                if letra.isdigit():
                    buffer+=letra
                    columna+=1
                    estado="S2"
                elif(letra == "."):
                    buffer += letra
                    columna +=1
                    estado ="S2"
                else: 
                    if self.AutomataFinitoDecimal(letra):
                        self.ListaTokens.append(Token("Numero",buffer,linea,columna))
                    else:
                        self.ListaTokens.append(Token("Numero",buffer,linea,columna))
                    buffer = ""
                    contador -= 1
                    estado = "S0"
            contador += 1
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
