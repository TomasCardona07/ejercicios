Algoritmo sin_titulo
	Definir cantPerson, edad, contador como numero
	Escribir 'ingrese la cantidad de personas'
	leer cantPerson
	contadorEdad<-0
	Para contador<-1 Hasta cantPerson Con Paso 1 Hacer
		Escribir 'ingrese la edad numero ',contador
		Leer edad
		Mientras no(edad>1 y edad<120) Hacer
			Escribir 'edad incorrecta, ingrese nuevamente la edad'
			Leer edad
		FinMientras
		si edad>=18 Entonces
			contadorEdad<-contadorEdad+1
		FinSi
	FinPara
	porcentajeMayorEdad<-(contadorEdad/cantPerson)*100
	Escribir 'el ',porcentajeMayorEdad,'% es mayor de edad'
FinAlgoritmo
