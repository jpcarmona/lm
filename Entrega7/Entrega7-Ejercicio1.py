from funciones import pasar_a_segundos,calcular_coste,convertir_a_euros

tarifa=int(input("¿Cuál es tu tarifa en céntimos (por cada segundo)?: "))

numllam=int(input("¿Cuántas llamadas se ha realizado?: "))

listallam=[]
for llam in range(numllam):
	tiempo=input("¿Cuánto ha durado la llamada nº {}?(99:59:59): ".format(llam+1))
	listallam.append(tiempo)

total=0
num=0
for llam in listallam:
	num+=1
	segundos=pasar_a_segundos(llam)
	centimos=calcular_coste(segundos,tarifa)
	total+=centimos
	euros=convertir_a_euros(centimos)
	print("La llamada nº {} ha costado {} Euros".format(num,euros))

totaleuros=convertir_a_euros(total)
print("Las llamadas han tenido un coste total de {} Euros".format(totaleuros))

