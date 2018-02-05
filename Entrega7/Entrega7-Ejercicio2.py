from funciones import pasar_a_segundos,calcular_coste,convertir_a_euros

with open("comunicaciones.txt","r") as comunica:
	listacomunica=comunica.readlines()

tarifa=int(listacomunica[0].replace("\n","").split(" ")[1])

total=0
num=0
for llamada in listacomunica[1:]:
	num+=1
	llam=llamada.replace("\n","")
	segundos=pasar_a_segundos(llam)
	centimos=calcular_coste(segundos,tarifa)
	total+=centimos
	euros=convertir_a_euros(centimos)
	print("La llamada nº {} ha tenido un coste de {} Euros".format(num,euros))

print("")
totaleuros=convertir_a_euros(total)
print("Las llamadas han tenido un coste total de {} Euros".format(totaleuros))