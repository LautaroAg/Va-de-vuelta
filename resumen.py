import pickle

def levantar_dicc():
	try:
		f1 = open('data/info_juego.txt','rb')
		data = pickle.load(f1)
		f1.close()
		return data
	except:
		return 'Error de archivos - No se encontró un archivo'


dicc = levantar_dicc()
print dicc
for nombre in dicc.keys():
        print 'Nombre: ' + nombre
        print 'Hora de inicio: ' + str(dicc[nombre]['hora_inicio'])
        print 'Hora de finalizado: ' + str(dicc[nombre]['hora_final'])
        print 'Adivinanzas realizadas: ' + str(dicc[nombre]['adivinanzas'])
        print 'Ahorcados realizados: ' + str(dicc[nombre]['ahorcados'])
        print 'Inventa historia realizadas: ' + str(dicc[nombre]['historias'])
        print 'Casillas recorridas: ' + str(dicc[nombre]['casillas_recorridas'])
        print 'Vidas con las que inicia: ' + str(dicc[nombre]['vidas_iniciales'])
        print 'Vidas con las que termina: ' + str(dicc[nombre]['vidas_final'])
        print '----------------------------------------------------------------'
