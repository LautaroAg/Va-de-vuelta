import pilas
import pickle
from pilas.escena import Base
from sonido import Sonido

class Eleccion_casillas(Base): 

    def  __init__(self):
        Base.__init__(self)

    def reanudar(self):
        self.m.detener()

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

    def menuCasillas(self):
        cartelMenu_casillas = pilas.actores.Texto('Cantidad de casillas de cada color',fuente='data/tipografias/American Captain.ttf')
        cartelMenu_casillas.escala =[4,2],3  
        cartelMenu_casillas.color = pilas.colores.verde
        opciones = [('- Celeste -',self.funcion_celeste),
                    ('- Violeta -',self.funcion_violeta),
                    (' - Verde -',self.funcion_verde),
                    (' - Ahorcado -',self.funcion_ahorcado),
                    (' - Comodin -',self.funcion_comodin),
                    (' - volver -',self.volver)]
        self.menu2= pilas.actores.Menu(opciones,y=-40)
        self.menu2.escala = 1.4  

    def funcion_celeste(self):
        self.cantidad('celeste')

    def funcion_violeta(self):
        self.cantidad('violeta')

    def funcion_verde(self):
        self.cantidad('verde')

    def funcion_ahorcado(self):
        self.cantidad('ahorcado')

    def funcion_comodin(self):
        self.cantidad('comodin')

    def total_casillas(self):
        cant = 0
        try:
            f = open('data/estado_casillas.txt','rb')
            dicc = pickle.load(f)
            f.close()
            dicc[self.color_act] = int(self.txt.texto)
            for color in dicc.keys():
                cant = cant + dicc[color]
        except IOError:
            pass
        finally:
            return cant + 3

    def cantidad(self,color):
        #self.menu.desactivar()
        self.txt = pilas.interfaz.IngresoDeTexto(limite_de_caracteres = 2, x=0,y=150)

        self.color_act = color
        self.blisto = pilas.interfaz.Boton('listo',x=205 , y= 150)
        self.blisto.conectar(self.guardar_datos)


    def guardar_datos(self):
        if str(self.txt.texto).isdigit():
            if int(self.total_casillas()) < 69:
                try:
                    f = open('data/estado_casillas.txt','rb')
                    dicc = pickle.load(f)
                    f.close()
                    #proceso
                    dicc[self.color_act] = int(self.txt.texto)
                    #guardar
                    f= open('data/estado_casillas.txt','wb')
                    pickle.dump(dicc,f)
                    f.close()
                except:
                    dicc = {'celeste': 0,'violeta': 0,'verde': 0,'ahorcado': 0, 'comodin': 0}
                    dicc[self.color_act] = int(self.txt.texto)
                    f = open('data/estado_casillas.txt','wb')
                    pickle.dump(dicc,f)
                    f.close()
                finally:
                    self.blisto.desactivar()
                    self.txt.eliminar()
                    #self.menu.activar()
                    self.blisto.destruir()
            else:
                pilas.avisar('Demasiadas casillas Max 69, vas: ' + str(int(self.total_casillas()) - int(self.txt.texto) ) )
        else:
            pilas.avisar('Solo numeros!')

    def volver(self, *k, **kv):
        self.m.detener()
        pilas.recuperar_escena()
 
    def iniciar(self):
        self.casillas = 69
    	pilas.fondos.Fondo('data/imagenes/fondos/caballo.png')
        self.iniciar_sonido()
        self.musica.conectar_presionado(self.verificar_musica)
    	self.menuCasillas()

'''
pilas.iniciar(ancho=1366, alto=768)
pilas.cambiar_escena(Eleccion_casillas())
pilas.ejecutar()'''