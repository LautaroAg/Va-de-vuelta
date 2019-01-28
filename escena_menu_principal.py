# -*- coding: cp1252 -*-   
import pilas
import pickle
import random
from pilas.escena import Base
from escena_datos import Ingreso_datos
from escena_ayuda import Ayuda_juego
from escena_puntajes import Puntajes
from escena_config import Config
from sonido import Sonido     

class Menu(Base):

	def __init__(self):
		pilas.escena.Base.__init__(self)

	def ver_ayuda(self):
		pilas.almacenar_escena(Ayuda_juego())

	def ver_puntaje(self):
		pilas.almacenar_escena(Puntajes())

	def ver_configuracion(self):
		self.m.detener()
		pilas.almacenar_escena(Config())

	def reanudar(self):
		self.m.reproducir()

	def salir(self):
		import sys
		sys.exit(0)

	def iniciar_sonido(self):
	   try:
	       f = open("data/estado_musica.txt",'rb')
	       est = pickle.load(f)
	       f.close()
	   except:
	       est = True
	       f = open("data/estado_musica.txt",'wb')
	       pickle.dump(est,f)
	       f.close()
	   self.m = pilas.sonidos.cargar("data/musica/Sneaky_Adventure.ogg")
	   if est:  
	       self.m.reproducir()
	       self.musica = Sonido(musica=self.m,x=250,y=250,estado=est)

	def iniciar_fondo(self):
		self.cont = 0
		pilas.fondos.Fondo("data/imagenes/fondos/menu.png")
	    
	def iniciar_menu(self):
		cartel_menu = pilas.actores.Texto("M E N U",fuente="data/tipografias/lazy_sunday_regular.ttf",x=0,y=0)
		cartel_menu.escala=[4,2],3
		cartel_menu.color = pilas.colores.verde
		opciones = [('- Jugar -',self.comenzar_juego),('- Configuracion -',self.ver_configuracion),('- Ver puntajes -',self.ver_puntaje),('- Ayuda -',self.ver_ayuda),(' - Salir -',self.salir)]
		self.menu = pilas.actores.Menu(opciones,y=-40,fuente="data/tipografias/American Captain.ttf")
		self.menu.escala = 1.4 
	    
	def comenzar_juego(self):
		self.m.detener()
		pilas.almacenar_escena(Ingreso_datos())

	def verificar_musica(self):
		if self.musica.ver_estado():
			self.musica.apagar()
		else:
			self.musica.encender()

	def iniciar(self):
		self.iniciar_sonido()
		self.iniciar_fondo()
		self.iniciar_menu()
		self.musica.conectar_presionado(self.verificar_musica)
	  #Titulo
		self.titulo = pilas.actores.Texto("Va de vuelta", fuente='data/tipografias/Animated.ttf', y=150)
		self.titulo.escala = [8,4],6





'''pilas.iniciar(ancho=1366, alto=768)
pilas.cambiar_escena(Menu())
pilas.ejecutar()'''
 