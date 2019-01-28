import pilas
from escena_menu_principal import Menu
from sonido import Sonido


pilas.iniciar(1366, 768, titulo="Va de vuelta")
pilas.mundo.motor.alto_original = 768
pilas.mundo.motor.ancho_original = 1366
pilas.cambiar_escena(Menu())

pilas.ejecutar()
