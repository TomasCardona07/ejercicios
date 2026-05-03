Algoritmo ejercicio7
	Definir capacDisco, cd, megaB Como numero
	Escribir 'ingrese la capacidad del disco en GB'
	Leer capacDisco
	megaB<-(capacDisco * 1024)
	cd<- trunc(megaB/700)+1
	Escribir 'se necesitan ', cd,' CDs para la copia de seguridad'
FinAlgoritmo
