Algoritmo sin_titulo
	Definir num, multi1,multi2,multi3,multi4,multi5,multi6,multi7,multi8,multi9,multi10 como entero
	Escribir 'ingrese un numero entero entre 1-10'
	leer num
	Mientras num<1 o num>10 Hacer
		Escribir 'numero incorrecto, solo se admite del 1-10'
		Escribir 'ingrese el numero nuevamente'
		Leer num
	FinMientras
	Segun num Hacer
		1:
			Para multi1<-1 Hasta 10 Con Paso 1 Hacer
				resultado1<-num*multi1
				Escribir num,' X ', multi1, ' = ',resultado1
			Fin Para
		2:
			Para multi2<-1 Hasta 10 Con Paso 1 Hacer
				resultado2<-num*multi2
				Escribir num,' X ', multi2, ' = ',resultado2
			FinPara
		3:
			Para multi3<-1 Hasta 10 Con Paso 1 Hacer
				resultado3<-num*multi3
				Escribir num,' X ', multi3, ' = ',resultado3
			FinPara
		4:
			Para multi4<-1 Hasta 10 Con Paso 1 Hacer
				resultado4<-num*multi4
				Escribir num,' X ', multi4, ' = ',resultado4
			FinPara
		5:
			Para multi5<-1 Hasta 10 Con Paso 1 Hacer
				resultado5<-num*multi5
				Escribir num,' X ', multi5, ' = ',resultado5
			FinPara
		6:
			Para multi6<-1 Hasta 10 Con Paso 1 Hacer
				resultado6<-num*multi6
				Escribir num,' X ', multi6, ' = ',resultado6
			FinPara
		7:
			Para multi7<-1 Hasta 10 Con Paso 1 Hacer
				resultado7<-num*multi7
				Escribir num,' X ', multi7, ' = ',resultado7
			FinPara
		8: 	
			Para multi8<-1 Hasta 10 Con Paso 1 Hacer
				resultado8<-num*multi8
				Escribir num,' X ', multi8, ' = ',resultado8
			FinPara
		9:
			Para multi9<-1 Hasta 10 Con Paso 1 Hacer
				resultado9<-num*multi9
				Escribir num,' X ', multi9, ' = ',resultado9
			FinPara
		10:
			Para multi10<-1 Hasta 10 Con Paso 1 Hacer
				resultado10<-num*multi10
				Escribir num,' X ', multi10, ' = ',resultado10
			FinPara
	FinSegun
FinAlgoritmo
