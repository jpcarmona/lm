import funciones

tarifa=int(input("¿Cuál es tu tarifa en céntimos (por cada segundo)?: "))

numllam=int(input("¿Cuántas llamadas se ha realizado?: "))

listallam=[]
for llam in range(numllam):
	tiempo=input("¿Cuánto ha durado esta llamada?(99:59:59): ")
	listallam.append(tiempo)

total=0
for llam in listallam:
	segundos=pasar_a_segundos(llam)
	centimos=calcular_coste(segundos,tarifa)
	total+=centimos
	euros=convertir_a_euros(centimos)
	print("Esta llamada a costado {} euros".format(euros))

totaleuros=convertir_a_euros(total)
print("Las llamadas han tenido un coste total de {} euros".format(totaleuros))

