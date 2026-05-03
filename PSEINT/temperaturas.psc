Algoritmo sin_titulo
	//programa que registra temperaturas
	Definir maximo, minimo, contador, temperatura como numero
	Definir hminimo, hmaximo,hora como numero
	contador<-1
	Escribir 'ingrese la ',contador,' temperatura registrada (unicamente el numero)'
	Leer temperatura
	Escribir 'ingrese la hora en la que fue registrada la temperatura ',contador
	Leer hora
	hmaximo<-hora
	hminimo<-hora
	maximo<-temperatura
	minimo<-temperatura
	Para contador<-2 Hasta 3 Con Paso 1 Hacer
		escribir'ingrese la ',contador,' temperatura registrada (unicamente el numero)'
		leer temperatura
		Escribir 'ingrese la hora en la que fue registrada la temperatura ',contador
		Leer hora
		si temperatura>maximo Entonces
			maximo<-temperatura
			si hora>hmaximo Entonces
				hmaximo<-hora
			FinSi
		SiNo
			si temperatura<minimo Entonces
				minimo<-temperatura
				si hora<hminimo Entonces
					hminimo<-hora
				FinSi
			FinSi
		FinSi
	FinPara
	Escribir 'la temperatura mas alta registrada fue de: ',maximo,'° y fue a las: ',hmaximo
	Escribir 'la temperatura mas baja registrada fue de: ',minimo,'° y fue a las: ',hminimo
	FinAlgoritmo
