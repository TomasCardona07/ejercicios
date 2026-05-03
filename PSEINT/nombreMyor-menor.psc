Algoritmo sin_titulo
	Definir edad,contador, edadminima Como Entero
	Definir nombre como cadena
	contador<-1
	corte<-'*'
	edadminima<-9999999
	edadmaxima<--999999
	mayoredad<-18
	contadorMayorEdad<-0
	Escribir 'ingrese el nombre de la persona ',contador
	Leer nombre
	si nombre=corte Entonces
		Escribir 'no se ingreso ningun nombre'
	SiNo
		mientras nombre<>corte Hacer
		Escribir 'ingrese la edad de ',nombre
		Leer edad
		Mientras edad<0 Hacer
			Escribir 'la edad no puede ser negativa'
			Leer edad
		FinMientras
		si edad<edadminima Entonces
			edadminima<-edad
			nombreminimo<-nombre
		FinSi
		si edad>edadmaxima Entonces
			edadmaxima<-edad
			nombremaximo<-nombre
		FinSi
		si edad>=mayoredad Entonces
			contadorMayorEdad<-contadorMayorEdad+1
		FinSi
		contador<-contador+1
		Escribir 'ingrese el nombre de la persona ',contador
		Leer nombre
	FinMientras
	Escribir nombreminimo,' es el menor porque tiene ',edadminima,' años'
	Escribir nombremaximo,' es el mayor porque tiene ',edadmaxima,' años'
	si contadorMayorEdad=1 Entonces
		Escribir 'solo hay una persona que es mayor de edad'
	SiNo
		Escribir 'hay ',contadorMayorEdad,' personas que son mayores de edad'
	FinSi
FinSi
FinAlgoritmo
