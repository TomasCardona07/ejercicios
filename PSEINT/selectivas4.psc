Algoritmo selectivas4
	Definir num1,num2,num3,numIntermedio,numMayor,numMenor como numero
	Mostrar 'ingrese el primer numero'
	Leer num1
	Mostrar 'ingrese el segundo numero'
	Leer num2
	Mostrar 'ingrese el tercer numero'
	Leer num3
	Si (num1 > num2 Y num1 > num3) Entonces
		numMayor <- num1
		Si (num2 > num3) Entonces
			numIntermedio <- num2
			numMenor <- num3
		Sino
			numIntermedio <- num3
			numMenor <- num2
		FinSi
	Sino
		Si (num2 > num1 Y num2 > num3) Entonces
			numMayor <- num2
			Si (num1 > num3) Entonces
				numIntermedio <- num1
				numMenor <- num3
			Sino
				numIntermedio <- num3
				numMenor <- num1
			FinSi
		Sino
			numMayor <- num3
			Si (num1 > num2) Entonces
				numIntermedio <- num1
				numMenor <- num2
			Sino
				numIntermedio <- num2
				numMenor <- num1
			FinSi
		FinSi
	FinSi
	
	Mostrar  'el numero mayor es: ',numMayor
	Mostrar 'el numero del medio es: ', numIntermedio
	Mostrar 'el numero menor es: ', numMenor
FinAlgoritmo