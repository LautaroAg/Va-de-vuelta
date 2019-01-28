import pilas
import pickle
from pilas.escena import Base


class Tema(Base):
    def  __init__(self):
        Base.__init__(self)

    def menuTema(self):
        cartelMenu_temas = pilas.actores.Texto('Eleccion de tema',fuente= "data/tipografias/lazy_sunday_regular.ttf")
        cartelMenu_temas.escala =[4,2],3  
        cartelMenu_temas.color = pilas.colores.verde
        opciones = [('- animales -',self.selector1),
                    ('- provincias argentinas -',self.selector2),('-volver-',self.volver)]
        self.menu3= pilas.actores.Menu(opciones,y=-40)
        self.menu3.escala = 1.4  

    def selector1(self):
        try:
            f = open ("data/estado_tema.txt","rb") 
            dicc=pickle.load(f)
            f.close()
            if (dicc['tema1']==True):
                dicc['tema1']=False 
                pilas.avisar("decidiste no elegir este tema")
            else:
                dicc['tema1']=True 
                pilas.avisar("elegiste este tema")   
            f = open("data/estado_tema.txt","wb")
            dicc['tema1']= True
            pickle.dump(dicc['tema1'],f)
            f.close()
        except:
            dicc = {'tema1': False,'tema2': False}
            f = open("data/estado_tema.txt","wb")
            pickle.dump(dicc,f)
            f.close()
            
    def selector2(self):
        try:
            f = open ("data/estado_tema.txt","rb") 
            dicc=pickle.load(f)
            f.close()
            if (dicc['tema2']==True):
                dicc['tema2']=False 
                pilas.avisar("decidiste no elegir este tema")
            else:
                dicc['tema2']=True 
                pilas.avisar("elegiste este tema")   
            f = open("data/estado_tema.txt","wb")
            dicc['tema1']= True
            pickle.dump(dicc['tema2'],f)
            f.close()
        except:
            dicc = {'tema1': False,'tema2': False}
            f = open("data/estado_tema.txt","wb")
            pickle.dump(dicc,f)
            f.close()
            
    def volver(self,*k, **kv):
        pilas.recuperar_escena()   

        
    def iniciar(self):
       	pilas.fondos.Fondo('data/imagenes/fondos/menu.png')
    	self.menuTema()	
        pilas.avisar("Presiona ESC para regresar.")
        self.pulsa_tecla_escape.conectar(self.volver)
        

'''pilas.iniciar(ancho=1366, alto=768)
pilas.cambiar_escena(Tema())
pilas.ejecutar()'''
