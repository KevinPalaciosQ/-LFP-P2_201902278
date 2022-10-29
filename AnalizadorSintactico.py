from dis import Instruction
from Token import *
from Error import *
from instrucciones import *
class AnalizadoSintactico():
    def __init__(self):
        self.ListaTokens = []
        self.ListaErrores = []
        self.Contador=0
    def Analizar(self,ListaTokens,ListaErrores):
        self.ListaTokens = ListaTokens
        self.ListaErrores = ListaErrores
    def Inicio(self):
        i=self.Instrucciones()
    def Instrucciones(self):
            i=self.Instrucciones()
            i2=self.Instrucciones2()
    def Instrucciones2(self):
        if self.ListaTokens[self.Contador].tipo=="EOF":
            print("Análisis Sintáctico Terminado")
        else:
            i=self.Instruccion()
            i2=None
            if self.Contador<len(self.ListaTokens):
                i2=self.Instrucciones2()
    def Instruccion(self):
        if self.ListaTokens[self.Contador+3].tipo=="TCONTROLES":
            i=self.Controles()
        elif self.ListaTokens[self.Contador+3].tipo=="TPROPIEDADES":
            i=self.propiedades()
        elif self.ListaTokens[self.Contador+3].tipo=="TCOLOCACION":
            i=self.Colocacion()
        else:
            self.ListaErrores.append("Error")
    def Controles(self):
        pass
    def propiedades(self):
        pass
    def Colocacion(self):
        pass
    def InstruccionesControles(self):
        i=self.Instrucciones()
        i2=self.Instrucciones2()