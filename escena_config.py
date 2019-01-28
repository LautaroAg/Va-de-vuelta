import pilas
import pickle
from escena_casillas import Eleccion_casillas 
from escena_tema  import Tema
from pilas.escena import Base
from sonido import Sonido

class Config(Base):

    def  __init__(self):
        Base.__init__(self)

    def reanudar(self):
        self.m.reproducir()

    def menu(self):
        cartel_menu = pilas.actores.Texto('C O N F I G U R A C I O N',fuente="data/tipografias/American Captain.ttf",y=20)
        cartel_menu.escala=[4,2],3
        cartel_menu.color = pilas.colores.verde
        opciones = [('- Cantidad de casillas -',self.casillas),('- Tema -',self.tematica),('- Tiempo -',self.tiempo),('- volver -',self.volver)]
        self.menu = pilas.actores.Menu(opciones,y=-40,fuente="data/tipografias/American Captain.ttf")
        self.menu.escala = 1.4

    def casillas(self):
        self.m.detener()
        pilas.almacenar_escena(Eleccion_casillas())

    def tematica(self):
        self.anim = pilas.interfaz.Boton('Animales',x=-100,y=200)
        self.anim.conectar(self.fun_anim)
        self.prov = pilas.interfaz.Boton('Provincias',x=100,y=200)
        self.prov.conectar(self.fun_prov)
        self.el = pilas.actores.Texto('Elige un tema:', x=0, y=300, fuente='data\lazy_sunday_regular.ttf')
        #self.texto_temas = pilas.actores.Texto('Elige un tema:',fuente='data/lazy_sunday_regular.tff',x=0,y=300)
    
    def fun_prov(self):
        f = open('data/tema.txt','wb')
        pickle.dump('provincias',f)
        f.close()
        self.anim.eliminar()
        self.el.destruir()
        self.prov.eliminar()

    def fun_anim(self):
        f = open('data/tema.txt','wb')
        pickle.dump('animales',f)
        f.close()
        self.anim.eliminar()
        self.el.destruir()
        self.prov.eliminar()

    def tiempo(self):
        self.clock = pilas.interfaz.IngresoDeTexto(limite_de_caracteres = 2, ancho = 100, x=200,y=200)
        self.clock.solo_numeros()    
        self.f = open('data/tiempo.txt','wb')
        pickle.dump(self.clock,self.f)
        self.f.close()
    
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

    def verificar_musica(self):
        if self.musica.ver_estado():
            self.musica.apagar()
        else:
            self.musica.encender()
        
    def volver(self, *k, **kv):
        self.m.detener()
        pilas.recuperar_escena()

    def iniciar(self):
        pilas.fondos.Fondo("data/imagenes/fondos/caballo.png")
        self.iniciar_sonido()
        self.musica.conectar_presionado(self.verificar_musica)
        self.menu()
       


'''
pilas.iniciar(ancho=1366, alto=768)
pilas.cambiar_escena(Config())
pilas.ejecutar()'''


 

