import pilas
import random
import pickle
from pilas.escena import Base

class Inventa_historia(Base):
	def __init__(self):
		Base.__init__(self)

	def acierto(self):
		self.aciertos += 1

	def fallo(self):
		self.errores += 1

	def guardar_datos(self):
		file = open('ult_jugador.txt', 'rb')
		nombre = pickle.load(file)
		file.close()

		f1 = open('data/info_juego.txt','rb')
		data = pickle.load(f)
		f1.close()
		data[nombre]['hisorias'] +=1
		f2 = open('data/info_juego.txt', 'wb')
		pickle.dump(data,f2)
		f2.close()

	def fin_minijuego(self):
		pilas.avisar('fin')
		try:
			f = open('data/vidas.txt', 'rb')
			vida = pickle.load(f)
			f.close()
			vida = vida - self.errores
			vida = vida + self.aciertos
			f = open('data/vidas.txt', 'wb')
			pickle.dump(vida, f)
			f.close()
		except:
			f= open('data/vidas.txt','wb')
			pickle.dump('Error de archivos - Inventa Historia',f)
			f.close()
		boton_volver = pilas.interfaz.Boton("Volver al juego",y=-100)
		boton_volver.conectar(pilas.recuperar_escena)

	def poner_ok(self,actor,lugar):
		jota = pilas.actores.Actor(imagen='data/imagenes/ok.png',x=lugar.x,y=lugar.y+50)
		actor.eliminar_habilidad(pilas.habilidades.Arrastrable)
		actor.x = lugar.x
		actor.y = lugar.y
		self.acierto()
		self.contador+=1
		if self.contador >= 3:
			self.fin_minijuego()
		pilas.escena_actual().colisiones.eliminar_colisiones_con_actor(actor,lugar)

	def poner_not_ok(self,actor,lugar):
		jota = pilas.actores.Actor(imagen = 'data/imagenes/not_ok.png',x=lugar.x,y=lugar.y+50)
		actor.x = lugar.x
		actor.y = lugar.y			
		self.fallo()
		self.contador +=1
		actor.eliminar_habilidad(pilas.habilidades.Arrastrable)
		if self.contador >= 3:
			self.fin_minijuego()
		pilas.escena_actual().colisiones.eliminar_colisiones_con_actor(actor,lugar)

	def cuando_tira_dado_per(self):
		num = random.randrange(1,7)
		pos = self.dado_per.x
		self.dado_per.desactivar()
		self.dado_per.destruir()
		direccion = 'data\imagenes\imagen_dado_personajes\img' + str(num) + '.png'
		self.actor_pers = pilas.actores.Actor(direccion, x=pos, y=self.pos_y)
		self.actor_pers.aprender(pilas.habilidades.Arrastrable)
		self.actor_pers.radio_de_colision = 30

		pilas.avisar('arrastra la imagen a su posicion')
		pilas.escena_actual().colisiones.agregar(self.actor_pers, self.aca_pers, self.poner_ok)
		pilas.escena_actual().colisiones.agregar(self.actor_pers, self.aca_acc, self.poner_not_ok)
		pilas.escena_actual().colisiones.agregar(self.actor_pers, self.aca_obj, self.poner_not_ok)
		
	def cuando_tira_dado_acc(self):
		pilas.avisar('arrastra la imagen a su posicion')
		num = random.randrange(1,7)
		pos = self.dado_acc.x
		self.dado_acc.desactivar()
		self.dado_acc.destruir()
		direccion = 'data\imagenes\imagen_dado_acciones\img' + str(num) + '.png'
		self.actor_acc = pilas.actores.Actor(direccion, x=pos, y=self.pos_y)
		self.actor_acc.aprender(pilas.habilidades.Arrastrable)
		self.actor_acc.radio_de_colision = 30

		pilas.escena_actual().colisiones.agregar(self.actor_acc, self.aca_acc, self.poner_ok)
		pilas.escena_actual().colisiones.agregar(self.actor_acc, self.aca_pers, self.poner_not_ok)
		pilas.escena_actual().colisiones.agregar(self.actor_acc, self.aca_obj, self.poner_not_ok)

	def cuando_tira_dado_obj(self):
		pilas.avisar('arrastra la imagen a su posicion')
		num = random.randrange(1,7)
		pos = self.dado_obj.x
		self.dado_obj.desactivar()
		self.dado_obj.destruir()
		direccion = 'data\imagenes\imagen_dado_objeto\img' + str(num) + '.png'
		self.actor_obj = pilas.actores.Actor(direccion, x=pos, y=self.pos_y)
		self.actor_obj.aprender(pilas.habilidades.Arrastrable)
		self.actor_obj.radio_de_colision = 30
		pilas.escena_actual().colisiones.agregar(self.actor_obj, self.aca_obj, self.poner_ok)
		pilas.escena_actual().colisiones.agregar(self.actor_obj, self.aca_acc, self.poner_not_ok)
		pilas.escena_actual().colisiones.agregar(self.actor_obj, self.aca_pers, self.poner_not_ok)

	def iniciar(self):
		self.el = pilas.actores.Texto('El', x=-350, y=150, fuente='data\lazy_sunday_regular.ttf')
		self.el.color = pilas.colores.negro
		self.con = pilas.actores.Texto('con/en',x = -100,y=150,fuente='data\lazy_sunday_regular.ttf')
		self.con.color = pilas.colores.negro
		self.errores = 0
		self.aciertos = 0
		self.contador = 0
		self.pos_y = -200

		pilas.fondos.Fondo('data/imagenes/fondos/menu.png')
		posiciones = [-200, 0, 200]

		pos_pers = random.choice(posiciones)
		posiciones.remove(pos_pers)

		self.dado_per = pilas.actores.Boton(ruta_normal='data/imagenes/imagen_dado_personajes/img0.png', x=pos_pers, y=self.pos_y)
		
		pos_acc = random.choice(posiciones)
		posiciones.remove(pos_acc)
		self.dado_acc = pilas.actores.Boton(ruta_normal='data/imagenes/imagen_dado_acciones/img0.png', x=pos_acc, y=self.pos_y)		
		
		pos_obj = posiciones[0]
		self.dado_obj = pilas.actores.Boton(ruta_normal='data/imagenes/imagen_dado_objeto/img0.png', x=pos_obj, y=self.pos_y)

		self.dado_per.conectar_presionado(self.cuando_tira_dado_per)
		self.dado_acc.conectar_presionado(self.cuando_tira_dado_acc)
		self.dado_obj.conectar_presionado(self.cuando_tira_dado_obj)

		self.aca_pers = pilas.actores.Actor('data/imagenes/blank.png', x=-300, y=150)
		self.aca_pers.escala = 0.5
		self.aca_pers.radio_de_colision = 30

		self.aca_acc = pilas.actores.Actor('data/imagenes/blank.png', x=-200, y=150)
		self.aca_acc.escala = 0.5
		self.aca_acc.radio_de_colision = 30

		self.aca_obj = pilas.actores.Actor('data/imagenes/blank.png', x=0, y=150)
		self.aca_obj.escala = 0.5
		self.aca_obj.radio_de_colision = 30

		self.aca_cosas = [self.aca_pers, self.aca_obj, self.aca_acc]

		pilas.avisar('Tira los dados!')

#para testeo
'''
pilas.iniciar(ancho=1024, alto=768)
pilas.cambiar_escena(Inventa_historia())
pilas.ejecutar()'''
