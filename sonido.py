import pilas
import pickle
import random
from pilas.actores import Boton

class Sonido(Boton):

    def __init__(self, musica, x=0, y=0, estado=True):
        Boton.__init__(self, x=x, y=y)
        #Se cargan imagenes
        self.pic_on = pilas.imagenes.cargar("data/imagenes/sound_on.png")
        self.pic_off = pilas.imagenes.cargar("data/imagenes/mute.png")
        # Sonido
        self.musica = musica
        #Incializamos variable auxilar para conocer estado de musica on=true/off=false}      
        self.est = estado
        if self.est:
            self.imagen = self.pic_on
        else:
            self.apagar()
        #Conectamos con funcion

    def habilitar_sonido (self):
        if self.est: self.apagar()
        else: self.encender()

    def apagar(self):
        self.imagen = self.pic_off
        pilas.mundo.deshabilitar_sonido()
        self.musica.detener()
        self.est = False
        f = open("data/estado_musica.txt",'wb')
        pickle.dump(ver_estado(),f)
        f.close()

    def encender(self):
        self.imagen = self.pic_on
        pilas.mundo.deshabilitar_sonido(False)
        self.musica.reproducir(repetir=True)
        self.est = True
        f = open("data/estado_musica.txt",'wb')
        pickle.dump(ver_estado(),f)
        f.close()

    def ver_estado(self):
        return self.est

        

        
