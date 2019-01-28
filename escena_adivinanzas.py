import pilas
import pickle
import random
from pilas.escena import Base
import os
import sys

tema1={'dragon':'Tiene alas pero no es ave.','personaje':'Es tan valiente que corre solo hasta el castillo, sin temer a lo que se enfrenta.'}

class Adivinanzas(Base):

	def __init__(self):
		Base.__init__(self)

	def fin_minijuego(self):
		try:
			f1 = open('data/vidas.txt', 'rb')
			vida = pickle.load(f1)
			f1.close()
			vida -= self.vidas_perdidas
			file = open('data/vidas.txt','wb')
			pickle.dump(vida, file)
			file.close()
		except IOError:
			pilas.avisar('except')
			f= open('data/vidas.txt','wb')
			pickle.dump('Error de archivos - Adivinanza',f)
			f.close()
		self.guardar_datos()
		self.boton_volver = pilas.interfaz.Boton("Volver al juego", y=-100)
		self.boton_volver.conectar(self.volver_juego)

	def volver_juego(self):
		pilas.avisar('Fin')
		if self.vidas_perdidas > 1:
			self.fracasado.eliminar()
		else:
			self.victorioso.eliminar()
		self.boton_volver.desactivar()
		self.boton_volver.eliminar()
		pilas.recuperar_escena()

	def iniciar(self):
		self.vidas_perdidas = 0
		self.contador = 0
		self.pos_bot = [(-200,-200),(0,-200),(200,-200)]
		pilas.fondos.Fondo('data/imagenes/fondos/menu.png')
		self.crear_botones()

	def elegir(self):
		adiv= random.choice(tema1.keys())
		self.texto_adiv = pilas.actores.Texto(tema1[adiv],x=0,y=150)
		return adiv
	
	def elegir_imagen_correcta(self,imagen):
		directorio = 'data/imagenes/adivinanzas/'
		self.correcto = directorio + imagen +'.png'
		return self.correcto
		
	def elegir_imagen_incorrecta(self):
		img = random.choice(os.listdir('data/imagenes/adivinanzas'))
		while (('data/imagenes/adivinanzas/' + img) == self.correcto):
			img = random.choice(os.listdir('data/imagenes/adivinanzas'))
		return 'data/imagenes/adivinanzas/' + img
		
	def limpiar_pantalla(self):
		self.boton_correcto.desactivar()
		self.boton_correcto.eliminar()
		self.boton_incorrecto.desactivar()
		self.boton_incorrecto.eliminar()
		self.boton_incorrecto2.desactivar()
		self.boton_incorrecto2.eliminar()
		self.texto_adiv.eliminar()
			
	def guardar_datos(self):
		file = open('ult_jugador.txt', 'rb')
		nombre = pickle.load(file)
		file.close()

		f1 = open('data/info_juego.txt','rb')
		data = pickle.load(f1)
		f1.close()
		data[nombre]['adivinanzas'] +=1
		f2 = open('data/info_juego.txt', 'wb')
		pickle.dump(data,f2)
		f2.close()


	def fracaso(self):
		self.contador += 1
		self.vidas_perdidas += 1
		if self.contador > 1:
			self.limpiar_pantalla()
			self.fracasado= pilas.actores.Texto ('Perdiste =(', x=0, y=0)
			self.fin_minijuego()

	def victoria(self):
		self.contador +=1
		self.vidas_perdidas -= 1
		self.limpiar_pantalla()
		self.victorioso = pilas.actores.Texto('Ganaste!', x=0, y=0)
		self.fin_minijuego()

	def crear_botones(self):
		pos1 = random.choice(self.pos_bot)
		self.pos_bot.remove(pos1)

		self.boton_correcto = pilas.actores.Boton(ruta_normal=self.elegir_imagen_correcta(self.elegir()), x=pos1[0], y=pos1[1])
		self.boton_correcto.escala = 0.4
		pos2 = random.choice(self.pos_bot)
		self.pos_bot.remove(pos2)
		self.boton_incorrecto = pilas.actores.Boton(ruta_normal=self.elegir_imagen_incorrecta(),x=pos2[0],y=pos2[1])
		self.boton_incorrecto.escala = 0.4
		
		pos3 = self.pos_bot[0]
		self.boton_incorrecto2 = pilas.actores.Boton(ruta_normal=self.elegir_imagen_incorrecta(),x=pos3[0],y=pos3[1])
		self.boton_incorrecto2.escala = 0.4 

		self.boton_correcto.conectar_presionado(self.victoria)
		self.boton_incorrecto.conectar_presionado(self.fracaso)
		self.boton_incorrecto2.conectar_presionado(self.fracaso)
#para testeo
'''
pilas.iniciar(ancho = 1024, alto = 768)
pilas.cambiar_escena(Adivinanzas())
pilas.ejecutar()'''