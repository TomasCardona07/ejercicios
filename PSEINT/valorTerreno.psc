Algoritmo valorTerreno
	definir ancho, largo, precioMtrCuad,precioTerr,cantMtsAlamabre,areaCuad,valorMtsCuadrados como numero
	Escribir "ingrese el ancho del terreno en metros"
	leer ancho
	Escribir "ingrese el largo del terreno en metros"
	Leer largo
	Escribir "ingrese el precio del metro cuadrado"
	leer precioMtrCuad
	perimetro<-(largo*2)+(ancho*2)
	areaCuad<-largo*ancho
	valorMtsCuadrados<-areaCuad*precioMtrCuad
	escribir"el valor total del cuadrado es de: ", valorMtsCuadrados," pesos"
	alambrado<-perimetro*3
	Escribir "el total de metros de alambre que se necesita para cercarlo 3 veces es de: ", alambrado," metros"
FinAlgoritmo
