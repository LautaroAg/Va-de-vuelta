# coding=utf-8
import pilas
import pickle
import random
import os
from pilas.escena import Base
from final_partida import Final
from escena_ahorcado import Animales
from escena_ayuda import Ayuda_juego
#from escena_menu_principal import Menu
from escena_adivinanzas import Adivinanzas
from escena_inventa_historia import Inventa_historia
from dado import Dado
from sonido import Sonido


class Juego(Base):
    def __init__(self, nombre=''):
        Base.__init__(self)
        #self.musica = pilas.sonidos.cargar('data/musica/Two_Finger_Johnny.ogg')
        self.nombre = nombre
        self.puntos_fin = 0
        self.fin = False
        self.pos = [3, 1]
        #self.nivel = 1
        self.inf2 = False
        self.inf3 = False
        self.sonido_fallo = pilas.sonidos.cargar('data/musica/fail_sound.ogg')
        self.sonido_bien = pilas.sonidos.cargar('data/musica/ok_sound.ogg')
        self.sonido_llegada = pilas.sonidos.cargar('data/musica/ta da.ogg')
        self.estructura = {(3, 1): [(302, -307), ('arriba', 'fin_tablero'), 'actividad'],
              (3, 2): [(302, -257), ('derecha', 'abajo'), 'bifurcacion1'],
              (1, 2): [(402, -257), ('arriba', 'fin_tablero'), 'actividad'],
              (2, 2): [(352, -257), ('derecha', 'izquierda'), 'flecha_der'],
              (8, 6): [(52, -57), ('arriba', 'abajo'), 'flecha_arr'],
              (17, 6): [(-398, -57), ('arriba', 'abajo'), 'flecha_arr'],
              (14, 6): [(-248, -57), ('arriba', 'abajo'), 'flecha_arr'],
              (14, 2): [(-248, -257), ('abajo', 'arriba'), 'flecha_abj'],
              (6, 7): [(152, -7), ('izquierda', 'derecha'), 'flecha_izq'],
              (1, 3): [(402, -207), ('arriba', 'abajo'), 'actividad'],
              (1, 4): [(402, -157), ('arriba', 'abajo'), 'actividad'],
              (1, 5): [(402, -107), ('arriba', 'abajo'), 'actividad'],
              (1, 6): [(402, -57), ('arriba', 'abajo'), 'actividad'],
              (1, 7): [(402, -7), ('izquierda', 'abajo'), 'actividad'],
              (2, 7): [(352, -7), ('izquierda', 'derecha'), 'actividad'],
              (3, 7): [(302, -7), ('izquierda', 'derecha'), 'actividad'],
              (4, 7): [(252, -7), ('izquierda', 'derecha'), 'actividad'],
              (5, 7): [(202, -7), ('izquierda', 'derecha'), 'actividad'],
              (7, 7): [(102, -7), ('izquierda', 'derecha'), 'actividad'],
              (8, 7): [(52, -7), ('izquierda', 'derecha'), 'bifurcacion3'],
              (4, 2): [(252, -257), ('izquierda', 'derecha'), 'actividad'],
              (5, 2): [(202, -257), ('izquierda', 'derecha'), 'actividad'],
              (6, 2): [(152, -257), ('izquierda', 'derecha'), 'actividad'],
              (7, 2): [(102, -257), ('izquierda', 'derecha'), 'actividad'],
              (8, 2): [(52, -257), ('arriba', 'derecha'), 'actividad'],
              (8, 3): [(52, -207), ('arriba', 'abajo'), 'actividad'],
              (8, 4): [(52, -157), ('izquierda', 'abajo'), 'bifurcacion2'],
              (8, 5): [(52, -107), ('arriba', 'abajo'), 'actividad'],
              (9, 7): [(2, -7), ('izquierda', 'derecha'), 'actividad'],
              (10, 7): [(-48, -7), ('izquierda', 'derecha'), 'actividad'],
              (11, 7): [(-98, -7), ('izquierda', 'derecha'), 'actividad'],
              (12, 7): [(-148, -7), ('izquierda', 'derecha'), 'actividad'],
              (13, 7): [(-198, -7), ('izquierda', 'derecha'), 'actividad'],
              (14, 7): [(-248, -7), ('izquierda', 'derecha'), 'actividad'],
              (15, 7): [(-298, -7), ('izquierda', 'derecha'), 'actividad'],
              (16, 7): [(-348, -7), ('izquierda', 'derecha'), 'actividad'],
              (17, 7): [(-398, -7), ('arriba', 'derecha'), 'actividad'],
              (17, 8): [(-398, 43), ('arriba', 'abajo'), 'actividad'],
              (17, 9): [(-398, 93), ('arriba', 'abajo'), 'actividad'],
              (17, 10): [(-398, 143), ('arriba', 'abajo'), 'actividad'],
              (17, 11): [(-398, 193), ('arriba', 'abajo'), 'actividad'],
              (17, 12): [(-398, 243), ('arriba', 'abajo'), 'actividad'],
              (17, 13): [(-398, 293), ('fin_tablero', 'abajo'), 'actividad'],
              (8, 8): [(52, 43), ('arriba', 'abajo'), 'actividad'],
              (8, 9): [(52, 93), ('arriba', 'abajo'), 'actividad'],
              (8, 10): [(52, 143), ('arriba', 'abajo'), 'actividad'],
              (8, 11): [(52, 193), ('arriba', 'abajo'), 'actividad'],
              (8, 12): [(52, 243), ('arriba', 'abajo'), 'actividad'],
              (8, 13): [(52, 293), ('arriba', 'abajo'), 'actividad'],
              (8, 14): [(52, 343), ('izquierda', 'abajo'), 'actividad'],
              (9, 14): [(2, 343), ('izquierda', 'derecha'), 'actividad'],
              (10, 14): [(-48, 343), ('izquierda', 'derecha'), 'actividad'],
              (11, 14): [(-98, 343), ('izquierda', 'derecha'), 'actividad'],
              (12, 14): [(-148, 343), ('izquierda', 'derecha'), 'actividad'],
              (13, 14): [(-198, 343), ('izquierda', 'derecha'), 'actividad'],
              (14, 14): [(-248, 343), ('izquierda', 'derecha'), 'actividad'],
              (15, 14): [(-298, 343), ('izquierda', 'derecha'), 'actividad'],
              (16, 14): [(-348, 343), ('fin_tablero', 'derecha'), 'actividad'],
              (9, 4): [(2, -157), ('izquierda', 'derecha'), 'actividad'],
              (10, 4): [(-48, -157), ('izquierda', 'derecha'), 'actividad'],
              (11, 4): [(-98, -157), ('izquierda', 'derecha'), 'actividad'],
              (12, 4): [(-148, -157), ('izquierda', 'derecha'), 'actividad'],
              (13, 4): [(-198, -157), ('izquierda', 'derecha'), 'actividad'],
              (14, 4): [(-248, -157), ('abajo', 'derecha'), 'bifurcacion4'],
              (14, 5): [(-248, -107), ('arriba', 'abajo'), 'actividad'],
              (14, 3): [(-248, -207), ('abajo', 'arriba'), 'actividad'],
              (14, 1): [(-248, -307), ('izquierda', 'arriba'), 'actividad'],
              (15, 1): [(-298, -307), ('izquierda', 'derecha'), 'actividad'],
              (16, 1): [(-343, -307), ('izquierda', 'derecha'), 'actividad'],
              (17, 1): [(-398, -307), ('arriba', 'derecha'), 'actividad'],
              (17, 2): [(-398, -257), ('arriba', 'abajo'), 'actividad'],
              (17, 3): [(-398, -207), ('arriba', 'abajo'), 'actividad'],
              (17, 4): [(-398, -157), ('arriba', 'abajo'), 'actividad'],
              (17, 5): [(-398, -107), ('arriba', 'abajo'), 'actividad']} 
        self.teleport = []
        self.total_casillas = 68

    def colocar_imagen(self, imagen, posicion, escala):
        actor_aleatorio = pilas.actores.Actor(imagen, x=posicion[0], y=posicion[1])
        actor_aleatorio.escala = escala

    def ver_ayuda(self):
        pilas.almacenar_escena(Ayuda_juego())
    
    def volver(self):
        pilas.recuperar_escena(Menu())

    def casilla(self):
        return self.estructura[tuple(self.pos)][1][0]

    def casilla_retroceder(self):
        return self.estructura[tuple(self.pos)][1][1]
    
    def sumar_vidas(self,cant):
      pilas.avisar(cant)
      if cant > 0:
        for indice in cant:
          objeto_vidas_actuales = self.vidas_actuales[len(self.vidas_actuales)-1]
          self.vidas_actuales.append(pilas.actores.Actor(imagen='data/imagenes/vida.png',x= objeto_vidas_actuales.x + 25,y=objeto_vidas_actuales.y))
          pilas.avisar(indice)
      else: #cant < 0
        cant = cant*(-1)
        for indice in cant:
          self.vidas_actuales.remove(self.vidas_actuales[len(self.vidas_actuales)-1])

    def actualizar_puntaje(self):
      try:
        f = open('data/vidas.txt','rb')
        data = pickle.load(f)
        f.close()
        if type(data) == str:
          raise IOError
        if data == 0:
          self.fin_partida()
        elif data > len(self.vidas_actuales):
          self.sumar_vidas(data-len(self.vidas_actuales))
        elif data < len(self.vidas_actuales):
          self.sumar_vidas(data-len(self.vidas_actuales))
      except IOError:
        j = 3
        f = open('data/vidas.txt','wb')
        pickle.dump(j,f)
        f.close()
        #self.actualizar_puntaje()

    def accion_dragon(self):
      pilas.avisar('Dragon! pierdes una vida =(')
      f = open('data/vidas.txt','rb')
      data = pickle.load(f)
      f.close()
      data -= 1
      f = open('data/vidas.txt','wb')
      pickle.dump(data,f)
      f.close()
      self.actualizar_puntaje()

    def reanudar(self):
      self.actualizar_puntaje()
      #self.m.detener()

    def es_final(self):
      if (self.pos == tuple[17, 13]) or (self.pos == [15, 14]):
        return True
      else:
        return False

    def verificar_musica(self):
      if self.musica.ver_estado():
        self.musica.apagar()
      else:
        self.musica.encender()

    def avanzando(self,tirada_dado):
      for cant in range(tirada_dado):
            if self.casilla() == 'arriba':
                if self.estructura[tuple(self.pos)][1][0] == 'fin_tablero':
                  cant = tirada_dado
                else:
                    self.pos[1] +=1
            elif self.casilla() == 'izquierda':
                if self.estructura[tuple(self.pos)][1][0] == 'fin_tablero':
                  cant = tirada_dado
                else:
                    self.pos[0] += 1
            elif self.casilla() == 'derecha':
                self.pos[0] -= 1
            else: #abajo
                self.pos[1] -= 1

            if self.estructura[tuple(self.pos)][2] == 'flecha_arr':
              self.pos[1] +=1
            elif self.estructura[tuple(self.pos)][2] == 'flecha_abj':
              self.pos[1] -=1
            elif self.estructura[tuple(self.pos)][2] == 'flecha_der':
              self.pos[0] -=1
            elif self.estructura[tuple(self.pos)][2] == 'flecha_izq':
              self.pos[0] +=1
#              pilas.avisar('0masuno')
            
            if self.estructura[tuple(self.pos)][1][0] == 'fin_tablero':
              self.guardar_puntaje()
              pilas.cambiar_escena(Final())
            self.actor.x = self.estructura[tuple(self.pos)][0][0]
            self.actor.y = self.estructura[tuple(self.pos)][0][1]

    def avanzar(self):
        tirada_dado = self.dado.tirar()
        self.dado.desactivar()
        self.avanzando(tirada_dado)
        self.dado.activar()
        self.ver_colisiones()
#        if self.es_final() and (tirada_dado >= 0):
 #           self.nivel = 'Finalizado'
  #          self.sonido_llegada.reproducir()
   #         self.terminar_juego()
    #    else:
     #     self.ver_colisiones()
               
    def retroceder(self):
        tirada_dado = self.dado.tirar()
        self.dado.desactivar()
        for cant in range(tirada_dado):  
            if self.casilla_retroceder() == 'abajo':
                if self.estructura[tuple(self.pos)][2] == 'fin_tablero':
                    break
                else:
                    self.pos[1] -= 1
            elif self.casilla_retroceder() == 'arriba':
                self.pos[1] += 1
            elif self.casilla_retroceder() == 'izquierda':
                self.pos[0] += 1
            else:  # derecha
                self.pos[0] -= 1
            self.actor.x = self.estructura[tuple(self.pos)][0][0]
            self.actor.y = self.estructura[tuple(self.pos)][0][1]
        self.ver_colisiones()
        self.dado.activar()

    def elige_izq(self):
      if self.cual_bifu == 'bifurcacion1':
        self.estructura[tuple(self.pos)][1] = ('izquierda', 'abajo')
        self.b_der.eliminar()
      elif self.cual_bifu == 'bifurcacion2':
        self.estructura[tuple(self.pos)][1] = ('izquierda', 'abajo')
        self.b_arr.eliminar()
      elif self.cual_bifu == 'bifurcacion3':
        self.estructura[tuple(self.pos)][1] = ('izquierda', 'derecha')
        self.b_arr.eliminar()
      self.actor_bifu.destruir()
      self.dado.activar()
      self.b_izq.eliminar()

    def elige_der(self):
      self.estructura[tuple(self.pos)][1] = ('derecha', 'abajo')
      self.b_izq.eliminar()
      self.actor_bifu.destruir()
      self.dado.activar()
      self.b_der.eliminar()
    
    def elige_arr(self):
      if self.cual_bifu == 'bifurcacion4':
        self.estructura[tuple(self.pos)][1] = ('arriba', 'derecha')
        self.b_abj.eliminar()
      elif self.cual_bifu == 'bifurcacion2':
        self.estructura[tuple(self.pos)][1] = ('arriba', 'derecha')
        self.b_izq.eliminar()
      elif self.cual_bifu == 'bifurcacion3':
        self.estructura[tuple(self.pos)][1] = ('arriba', 'derecha')
        self.b_izq.eliminar()
      self.actor_bifu.destruir()
      self.dado.activar()
      self.b_arr.eliminar()

    def elige_abj(self):
      self.estructura[tuple(self.pos)][1] = ('abajo', 'derecha')
      self.b_arr.eliminar()
      self.actor_bifu.destruir()
      self.dado.activar()
      self.b_abj.eliminar()
    
    def accion_bifurcacion(self):
      self.dado.desactivar()
      self.cual_bifu = self.estructura[tuple(self.pos)][2]

      if self.cual_bifu == 'bifurcacion1':
        self.b_izq = pilas.interfaz.Boton('izquierda',x=175,y=55)
        self.b_der = pilas.interfaz.Boton('derecha',x=250,y=55)
        self.b_izq.conectar(self.elige_izq)
        self.b_der.conectar(self.elige_der)
      elif self.cual_bifu == 'bifurcacion2':
        self.b_izq = pilas.interfaz.Boton('izquierda',x=175,y=55)
        self.b_arr = pilas.interfaz.Boton('arriba',x=250,y=55)
        self.b_izq.conectar(self.elige_izq)
        self.b_arr.conectar(self.elige_arr)
      elif self.cual_bifu == 'bifurcacion3':
        self.b_arr = pilas.interfaz.Boton('arriba',x=175,y=55)
        self.b_izq = pilas.interfaz.Boton('izquierda',x=250,y=55)
        self.b_izq.conectar(self.elige_izq)
        self.b_arr.conectar(self.elige_arr)
      elif self.cual_bifu == 'bifurcacion4':
        self.b_arr = pilas.interfaz.Boton('arriba',x=175,y=55)
        self.b_abj = pilas.interfaz.Boton('abajo',x=250,y=55)
        self.b_arr.conectar(self.elige_arr)
        self.b_abj.conectar(self.elige_abj)

      pregunta = 'Bifurcacion!, Elige el camino'
      self.actor_bifu = pilas.actores.Actor(imagen= 'data/imagenes/bifurcacion.png')
      self.actor_bifu.x = 600
      self.actor_bifu.escala = 0.12
      #animacion
      self.actor_bifu.x = [220]
      self.actor_bifu.y = [140],2

      self.actor_bifu.decir(pregunta)
      

    def accion_cueva(self):
        opciones = ['avanzar', 'retroceder', 'retroceder']
        opcion = random.choice(opciones)
        if opcion == 'avanzar':
            self.avanzar()
        else:
            self.retroceder()

    def accion_inventa_historia(self):
        pilas.almacenar_escena(Inventa_historia())

    def contar_chiste(self):
        chistes = []
        for direct in os.listdir('data/chistes'):
            chistes.append(direct)
        opcion = random.choice(chistes)
        pilas.sonido.Reproducir(opcion)

    def accion_adivinanza(self):
       # pilas.fondos.Fondo('data/imagenes/fondos/menu.png')
        pilas.almacenar_escena(Adivinanzas())

    def accion_ahorcado(self):
        pilas.almacenar_escena(Animales())

    def ver_colisiones(self):
        actividad_act = self.estructura[tuple(self.pos)][2]
        if actividad_act != 'actividad':
            if actividad_act == 'cueva':
                self.accion_cueva()
            elif actividad_act == 'comodin':
                self.accion_comodin()
            elif actividad_act == 'ahorcado':
                self.accion_ahorcado()
            elif actividad_act == 'celeste' :
                self.accion_inventa_historia()
            elif actividad_act == 'verde':
                self.contar_chiste()
            elif (actividad_act == 'bifurcacion1') or (actividad_act == 'bifurcacion2') or (actividad_act == 'bifurcacion3') or (actividad_act == 'bifurcacion4'):
                self.accion_bifurcacion()
            elif actividad_act == 'violeta':
                self.accion_adivinanza()
            elif actividad_act == 'teletransportacion':
                self.accion_teletransportacion()
            elif actividad_act == 'dragon':
                self.accion_dragon()
        else:
            pilas.avisar('No ocurre nada especial en este casillero')

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

    def cuando_pulsa_tecla(self, evento):
        if evento.texto == 'a':
            self.ver_ayuda()
        elif evento.texto == 'p':
            pilas.escena.pausar()
        elif evento.texto == 't':
            self.terminar_juego()
   
    def guardar_puntaje(self): #mal implementado ??
      try:
        f = open('ult_puntaje.txt', 'rb')
        puntaje = pickle.load(f)
        f.close()
        puntaje['puntos'] = self.puntaje
        puntaje['tiempo'] = self.tiempo_jugado
        f = open('ult_puntaje.txt', 'wb')
        pickle.dump(puntaje, f)
        f.close()
      except:
        f = open('ult_puntaje.txt', 'wb')
        pickle.dump('error de archivo', f)
        f.close()

    def fin_partida(self):
        self.guardar_puntaje()
        pilas.cambiar_escena(Final())

    def accion_comodin(self):
      def fun_ahor():
        self.b_ahor.destruir()
        self.b_verd.destruir()
        self.b_viol.destruir()
        self.b_azul.destruir()
        self.actor_comodin.destruir()
        self.dado.activar()
        self.accion_ahorcado()
      def fun_verd():
        self.b_ahor.destruir()
        self.b_verd.destruir()
        self.b_viol.destruir()
        self.b_azul.destruir()
        self.actor_comodin.destruir()
        self.dado.activar()
        self.contar_chiste()
      def fun_viol():
        self.b_ahor.destruir()
        self.b_verd.destruir()
        self.b_viol.destruir()
        self.b_azul.destruir()
        self.actor_comodin.destruir()
        self.dado.activar()
        self.accion_inventa_historia()
      def fun_azul():
        self.b_ahor.destruir()
        self.b_verd.destruir()
        self.b_viol.destruir()
        self.b_azul.destruir()
        self.actor_comodin.destruir()
        self.dado.activar()
        self.accion_adivinanza()

      self.dado.desactivar()
      self.b_ahor = pilas.interfaz.Boton('Ahorcado',x=375,y = 70)
      self.b_verd = pilas.interfaz.Boton('Verde',x=300,y = 70)
      self.b_viol = pilas.interfaz.Boton('Violeta',x=225,y = 70)
      self.b_azul = pilas.interfaz.Boton('Azul',x=150,y = 70)
      
      self.b_azul.conectar(fun_azul)
      self.b_ahor.conectar(fun_ahor)
      self.b_viol.conectar(fun_viol)
      self.b_verd.conectar(fun_verd)

      pregunta = 'Comodin, elige una activdad por su color'
      self.actor_comodin = pilas.actores.Actor(imagen= 'data/imagenes/comodin.png')
      self.actor_comodin.x = 600
      self.actor_comodin.escala = 0.12
      #animacion
      self.actor_comodin.x = [220]
      self.actor_comodin.y = [140],2
      self.actor_comodin.decir(pregunta)
        
    def accion_teletransportacion(self):
        if self.pos == list(self.teleport[0]):
          self.pos = list(self.teleport[1])
        else:
            self.pos = list(self.teleport[0])
        self.actor.x = self.estructura[tuple(self.pos)][0][0]
        self.actor.y = self.estructura[tuple(self.pos)][0][1]        

    def colocar_actividades(self):
        def colocar_actividad(pos, actividad):
            self.estructura[tuple(pos)][2] = actividad
        try:
            f = open('data/estado_casillas.txt', 'rb')
            dicc = pickle.load(f)
            dicc['cueva'] = 1
            dicc['teletransportacion'] = 2
            dicc['dragon'] = 1
            f.close()
        except:
            dicc = {'celeste': 0, 'violeta': 0, 'ahorcado': 0, 'comodin': 0, 'verde': 0}
            n = self.total_casillas - 10
            for color_1 in dicc.keys():
                if n == 0:
                    break
                cant = random.randint(1, n/2)
                dicc[color_1] = cant
                n = n - cant
            dicc['teletransportacion'] = 2
            dicc['cueva'] = 1
            dicc['dragon'] = 1
        finally:
            pos_tablero = self.estructura.keys()
            for color in dicc.keys(): 
                for cantidad in range(dicc[color]):
                    rand_pos = random.choice(pos_tablero)
                    while (self.estructura[rand_pos][2] != 'actividad' or self.estructura[rand_pos][2] == 'flecha' or
                            self.estructura[rand_pos][2] == 'bifurcacion1' or self.estructura[rand_pos][2] == 'bifurcacion2' or 
                            self.estructura[rand_pos][2] == 'bifurcacion3' or self.estructura[rand_pos][2] == 'bifurcacion4' ):
                        pos_tablero.remove(rand_pos)
                        rand_pos = random.choice(pos_tablero)

                    colocar_actividad(rand_pos, color)
                    pos_tablero.remove(rand_pos)
                    est_rand = self.estructura[rand_pos][0]
                    if color == 'celeste':
                        self.colocar_imagen(imagen='data/imagenes/piedraCeleste.png', posicion=est_rand,
                                            escala=0.15)
                    elif color == 'violeta':
                        self.colocar_imagen(imagen='data/imagenes/piedraVioleta.png', posicion=est_rand,
                                            escala=0.15)
                    elif color == 'ahorcado':
                        self.colocar_imagen(imagen='data/imagenes/ahorcado.png', posicion=est_rand,
                                            escala=0.25)
                    elif color == 'comodin':
                        self.colocar_imagen(imagen='data/imagenes/comodin.png', posicion=est_rand,
                                            escala=0.05)
                    elif color == 'verde':
                        self.colocar_imagen(imagen='data/imagenes/piedraVerde.png', posicion=est_rand,
                                            escala=0.15)
                    elif color == 'teletransportacion':
                        self.colocar_imagen(imagen='data/imagenes/teletransportacion.png',
                                            posicion=est_rand, escala=0.05)
                        self.teleport.append(est_rand)
                    elif color == 'cueva':
                        self.colocar_imagen(imagen='data/imagenes/cueva.png', posicion=est_rand,
                                            escala=0.05)
                    else:  # DRAGON
                        self.colocar_imagen(imagen='data/imagenes/dragon.png', posicion=est_rand,
                                            escala=0.15)
            for relleno in pos_tablero:
                if self.estructura[relleno][2] == 'actividad':
                  self.colocar_imagen(imagen='data/imagenes/piedra.png', posicion=self.estructura[relleno][0], escala=0.15)

    def poner_fijas(self):
        n = 0.15
        self.colocar_imagen(imagen='data/imagenes/flecha_izq.png', posicion=(152, -7), escala=n)
        self.colocar_imagen(imagen='data/imagenes/flecha_arriba.png', posicion=(-248, -57), escala=n)
        self.colocar_imagen(imagen='data/imagenes/flecha_der.png', posicion=(352, -257), escala=n)
        self.colocar_imagen(imagen='data/imagenes/flecha_abajo.png', posicion=(-248, -257), escala=n)
        self.colocar_imagen(imagen='data/imagenes/flecha_arriba.png', posicion=(-398, -57), escala=n)
        self.colocar_imagen(imagen='data/imagenes/flecha_arriba.png', posicion=(52, -57), escala=n)
        self.colocar_imagen(imagen='data/imagenes/arbol.png', posicion=(-520, 0), escala=1.4)
        self.colocar_imagen(imagen='data/imagenes/mapa.png', posicion=(322, -357), escala=0.07)
        self.colocar_imagen(imagen='data/imagenes/rosasDeLosVientos.png', posicion=(500, -300), escala=0.5)
        self.colocar_imagen(imagen='data/imagenes/sol.png', posicion=(-550, 340), escala=0.7)
        self.colocar_imagen(imagen='data/imagenes/castillo.png', posicion=(-405, 350), escala=0.1)
        self.colocar_imagen(imagen='data/imagenes/bifurcacion.png', posicion=(302, -257), escala=0.05)
        self.colocar_imagen(imagen='data/imagenes/bifurcacion.png', posicion=(52, -7), escala=0.05)
        self.colocar_imagen(imagen='data/imagenes/bifurcacion.png', posicion=(52, -157), escala=0.05)
        self.colocar_imagen(imagen='data/imagenes/bifurcacion.png', posicion=(-248, -157), escala=0.05)
        
    def iniciar(self):
        pilas.fondos.Fondo('data/imagenes/fondos/fondo_juego.png')
        self.total_casillas = 69
        self.poner_fijas()
        self.colocar_actividades()
        self.dado = Dado(x=300,y=250)
        self.dado.conectar_presionado(self.avanzar)
        self.iniciar_sonido()
        self.musica.conectar_presionado(self.verificar_musica)
        self.actor = pilas.actores.Actor('data/imagenes/personaje.png', x=301, y=-307)
        self.actor.escala = 0.07
        self.vidas_actuales = []
        try:
          f = open('data/vidas.txt','rb')
          data = pickle.load(f)
          f.close()
          if type(data) == str:
            raise IOError
          f = open('data/vidas.txt','wb')
          data += 3
          pickle.dump(data,f)
          f.close()
          self.actualizar_puntaje()
          pilas.avisar('iniciar')
        except IOError:
          f = open('data/vidas.txt','wb')
          pickle.dump(3,f)
          f.close()
          self.actualizar_puntaje()
          pilas.avisar('iniciar')


pilas.iniciar(ancho=1366, alto=768)
pilas.cambiar_escena(Juego())
pilas.ejecutar()
