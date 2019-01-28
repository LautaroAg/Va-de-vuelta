# -*- coding: cp1252 -*-
import pilas
import pickle
import os
from escena_juego_final import Juego
from pilas.escena import Base

class Puntajes(Base):

    def __init__(self):
        Base.__init__(self)


    def imprimir_puntajes(self):
        try:
            archivo = open("data/historial.txt",'rb')
            dic = pickle.load(archivo)
            archivo.close()
            claves = dic.keys()
            cadena = ""
            for i in claves:
                aux = str(i) + "- Puntos: " + str(dic[i]) + "\n"
                cadena = cadena + aux
        except:
            cadena = "Todavia no hay historial."
        texto = pilas.actores.Texto(cadena)
    
    def volver(self,*k, **kv):
        pilas.avisar("volviendo")
        pilas.recuperar_escena()
    
    def opcion_limpiar_historial(self):
        bot = pilas.interfaz.Boton("Limpiar historial",x=400,y=-300)
        def limpiar_historial():
            bot.desactivar()
            try:
                os.remove("data/historial.txt")
            except:
                pilas.avisar("No hay datos para limpiar")
            pilas.recuperar_escena()
        bot.conectar(limpiar_historial)
    
    def iniciar(self): 
        pilas.fondos.Fondo("data/imagenes/fondos/caballo.png") 
        titulo = pilas.actores.Texto("Historial de puntajes",y=250, fuente="data/tipografias/American Captain.ttf")
        titulo.escala = 2.3
        pilas.avisar("Presiona ESC para regresar.")
        self.imprimir_puntajes()
        self.pulsa_tecla_escape.conectar(self.volver)
        #self.opcion_limpiar_historial()

'''pilas.iniciar(1024,712)
pilas.mundo.motor.alto_original = 712
pilas.mundo.motor.ancho_original = 1024
pilas.cambiar_escena(Puntajes())
pilas.ejecutar()'''
                