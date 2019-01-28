import pilas
import pickle
from time import strftime
from pilas.escena import Base
import sys

class Final(Base):
	def __init__(self):
		Base.__init__(self)

	def salir(self):
		sys.exit(0)

	def levantar_vidas(self):
		f42 = open('data/vidas.txt', 'rb')
		jota = pickle.load(f42)
		f42.close()
		return jota

	def guardar_datos(self):
		file = open('ult_jugador.txt', 'rb')
		nombre = pickle.load(file)
		file.close()

		f1 = open('data/info_juego.txt','rb')
		data = pickle.load(f1)
		f1.close()

		data[nombre]['hora_final'] = strftime("%Y-%m-%d %H:%M:%S")
		data[nombre]['vidas_final'] = self.levantar_vidas()

	def iniciar(self):
		pilas.fondos.Fondo('data/imagenes/fondos/menu.png')
		txt_despedida = pilas.actores.Texto('Gracias por jugar!!!',x=0,y=200)
		txt_despedida.color = pilas.colores.negro


		tx = 'Te quedaron: ' + str(self.levantar_vidas()) + ' vidas.'
		txt_vidas = pilas.actores.Texto(tx, x=0, y=-100)
		txt_vidas.color = pilas.colores.negro

		self.guardar_datos()
		saliendo = pilas.interfaz.Boton('Salir')
		saliendo.conectar(self.salir)
'''
pilas.iniciar(ancho=1366, alto=768)
pilas.cambiar_escena(Final())
pilas.ejecutar()
'''