import pilas
import pickle
from time import strftime
from pilas.escena import Base
from sonido import Sonido
from escena_juego_final import Juego


class Ingreso_datos(Base):

    def __init__(self):
        Base.__init__(self)
        self.nombre = ''

    def volver_al_menu(self,*k, **kv):
        pilas.recuperar_escena()

    def variable_datos(self, nombre=''):
        self.nombre = str(nombre)
        dia=strftime('%d/%m/%y')
        datos = nombre + ' - ' + dia
        return str(datos)

    def rotacion_actor(self,n=0):
        self.actor.rotacion = n

    def cambiar_escena(self):
        name = str(self.info_juego)
        pilas.cambiar_escena(Juego(name))

    def comenzar_a_jugar(self):
        pilas.avisar('%s'%self.info_juego)
        self.actor.x = [0]
        self.actor.y = [-30]
        def ver_rta(r):
            self.actor.x = [-700],1
            self.actor.y = [200],1
            pilas.mundo.agregar_tarea(1.3,self.cambiar_escena)
        self.d.elegir(self.actor,'Estas listo %s?' % self.nombre,['>> Si! a jugar...<<'],ver_rta)
        pilas.mundo.agregar_tarea(1.5,self.d.iniciar)
    
    def guardar_datos(self):
        f = open('ult_jugador.txt', 'wb')
        pickle.dump(self.nombre,f)
        f.close()
        try:
            f3 = open('data/info_juego.txt', 'rb')
            dicc = pickle.load(f3)
            f3.close()
        except:
            dicc = {}
        dicc[self.nombre] = {}
        dicc[self.nombre]['nombre'] = self.nombre
        dicc[self.nombre]['hora_inicio'] = strftime('%Y-%m-%d %H:%M:%S')
        dicc[self.nombre]['adivinanzas'] = 0
        dicc[self.nombre]['ahorcados'] = 0
        dicc[self.nombre]['historias'] = 0
        dicc[self.nombre]['casillas_recorridas'] = 0
        try:
            file = open('data/vidas.txt', 'rb')
            vida = pickle.load(file)
            file.close()
            dicc['vidas_iniciales'] = vida
        except IOError:
            dicc['vidas_iniciales'] = 3
        f = open('data/info_juego.txt', 'wb')
        pickle.dump(dicc,f)
        f.close()

    def verificar(self):
        nombre = str(self.box.texto)
        self.box.desactivar()
        self.blisto.desactivar()
        if (len(nombre) < 4):
            self.d.decir(self.actor,'Ingresa un nombre mas largo. Al menos 4 letras')
            self.box.activar()
            self.blisto.activar()
            self.d.iniciar()
        elif nombre.isdigit():
            self.d.decir(self.actor,'No solo numeros! intentalo de nuevo')
            self.box.activar()
            self.blisto.activar()
            self.d.iniciar()
        else :
            self.box.eliminar()
            self.blisto.eliminar()
            self.info_juego = self.variable_datos(nombre)
            pilas.avisar('me trabo')
            self.guardar_datos()
            self.comenzar_a_jugar()


    def continuar_animacion(self):
        self.box.mostrar()
        self.blisto = pilas.interfaz.Boton('Listo',x=205)
        self.blisto.conectar(self.verificar)
        self.d = pilas.actores.Dialogo()
        self.d.decir(self.actor,'Hola! Ingresa tu nombre \n para comenzar a jugar.')
        self.d.iniciar()
 
    def iniciar(self):
        pilas.fondos.Fondo('data/imagenes/fondos/menu.png')
      #  self.iniciar_sonido()
        pilas.avisar('Preciona ESC para volver al menu')
        self.pulsa_tecla_escape.conectar(self.volver_al_menu)
        #Iniciamos actor interactor
        self.actor = pilas.actores.Mono()
        self.actor.x=600
        self.actor.rotacion = 330
        #Ingreso de texto
        self.box = pilas.interfaz.IngresoDeTexto(ancho=200)
        self.box.ocultar()
        self.box.escala = 1.5
        #animacion
        self.actor.x = [220]
        self.actor.y = [140],2
        pilas.mundo.agregar_tarea(2,self.rotacion_actor)
        pilas.mundo.agregar_tarea(2.3,self.continuar_animacion)

'''pilas.iniciar(ancho=1024, alto=768)
pilas.cambiar_escena(Ingreso_datos())
pilas.ejecutar()'''