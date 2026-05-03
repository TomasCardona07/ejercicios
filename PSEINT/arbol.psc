Algoritmo sin_titulo
	Definir base, contadorFilas, contador, contadorColumnas Como Entero
	Escribir 'ingrese numero entero impar mayor o igual a 3'
	leer base
	Mientras base mod 2=0 o base<3 Hacer
		Escribir 'numero incorrecto ingrese el numero nuevamente'
		Leer base
	FinMientras
	espacio<-trunc(base/2)
	contador<-1
	para contadorFilas<-1 hasta base con paso 2 Hacer
		para contadorColumnas<-1 Hasta contadorFilas con paso 1 Hacer
			Mientras contador<=espacio Hacer
				Escribir Sin Saltar ' '
				contador<-contador+1
			FinMientras
			Escribir Sin Saltar'X'
		FinPara
		Escribir ''
		espacio<-espacio-1
		contador<-1
	FinPara
FinAlgoritmo

	
