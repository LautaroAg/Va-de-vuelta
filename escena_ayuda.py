import pilas
from pilas.escena import Base
    
class Ayuda_juego(Base):

    def __init__(self):
        Base.__init__(self)

    def crear_texto_ayuda(self):
        ayuda = pilas.actores.Texto("Ayuda",x=-700,y=500, fuente="data/tipografias/lazy_sunday_shadow.ttf")
        ayuda.escala = 1.3
        ayuda.x= [-440]
        ayuda.y= [330]
        self.texto = pilas.actores.Texto(self.TEXTO,x=-100, y=1400)
        self.texto.y=[-200]
        #self.texto.color = pilas.colores.verde
        pilas.avisar("Pulsa ESC para regresar",40)

    def volver(self, *k, **kv):
        self.m.detener()
        pilas.recuperar_escena()

    def iniciar(self):
        self.TEXTO = 'Debes tirar el dado para avanzar en los casilleros, segun el casillero \nen el que caigas, deberas realizar una tarea. Por ejemplo si caes\n en el casillero con un dibujo de un ahorcado, deberas realizar\n el juego del ahorcado con el tema elegido.'
        pilas.fondos.Fondo('data/imagenes/fondos/menu.png')
        self.crear_texto_ayuda()
        self.pulsa_tecla_escape.conectar(self.volver)  
        
#Para chequear funcionamiento
pilas.iniciar(1024,712)

'''pilas.mundo.motor.alto_original = 712
pilas.mundo.motor.ancho_original = 1024
pilas.cambiar_escena(Ayuda_juego())
pilas.ejecutar()'''