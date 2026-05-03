Algoritmo sin_titulo
	Definir ancho, alto Como Real
	Definir contador1, contador2 Como Entero
	contador1<-0
	contador2<-0
	Escribir 'ingrese el ancho'
	leer ancho
	Mientras ancho<=0 Hacer
		Escribir 'el ancho tiene que ser numero positivo'
		Leer ancho
	FinMientras
	Escribir 'ingrese el alto'
	leer alto
	Mientras alto<=0 Hacer
		Escribir 'el alto tiene que ser un valor positivo'
		leer alto
	FinMientras
	Mientras contador2<alto Hacer
		Escribir ''
		Mientras contador1<ancho Hacer
			Escribir Sin Saltar 'X'
			contador1<-contador1+1
		FinMientras
		contador2<-contador2+1
		contador1<-0
	FinMientras
FinAlgoritmo
