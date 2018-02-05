def pasar_a_segundos(tiempo):
	""" Calcula los segundos (integer).
	Dada una cadena del tipo:
		"99:59:59" 		"""
	horas=int(tiempo.split(":")[0])
	minutos=int(tiempo.split(":")[1])
	segundos=int(tiempo.split(":")[2])

	return horas*3600+minutos*60+segundos

def calcular_coste(segundos,tarifa):
	""" Calcula el coste en centimos
	(integer). Dado unos segundos (entero) y
	una tarifa (integer)"""
	centimos=segundos*tarifa
	return centimos

def convertir_a_euros(centimos):
	""" Calcula el coste en Euros y centimos
	(string). Dado unos centimos(entero)"""
	eur=centimos//100
	cent=centimos%100
	euros=str(eur)+","+str(cent)
	return euros



