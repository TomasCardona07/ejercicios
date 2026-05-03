Algoritmo sin_titulo
	Definir num como numero
	Escribir 'ingrese el numero'
	leer num
	mientras num<=0 Hacer
		Escribir 'el numero tiene que ser positivo'
		Escribir 'ingrese el numero nuevamente'
		Leer num
	FinMientras
	si num mod 2=0 Entonces
		num<-num-2
		Escribir 'el numero es par'
		Para num<-num hasta 0 Con Paso -2 Hacer
			Escribir Sin Saltar' ',num,' '
		FinPara
	SiNo
		num<-num-1
		Escribir 'el numero es impar'
		Para num<-num hasta 0 Con Paso -2 Hacer
			Escribir Sin Saltar' ',num,' '
		FinPara
	FinSi
FinAlgoritmo
