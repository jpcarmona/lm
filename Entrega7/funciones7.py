def pasar_a_segundos(tiempo):
	""" Calcula los segundos.
	Dada una cadena del tipo:
		"99:59:59" 		"""
	horas=tiempo.split(":")[0]
	minutos=tiempo.split(":")[1]
	segundos=tiempo.split(":")[2]

	return horas*3600+minutos*60+segundos

def calcular_coste