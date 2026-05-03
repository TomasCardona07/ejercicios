Algoritmo sin_titulo
	Definir num1,num2,num3 como numero
	Escribir 'ingrese el primer numero'
	leer num1
	si num1<0 Entonces
		Escribir 'el numero ingresado no es valido'
	SiNo
		Escribir 'ingrese el segundo numero'
		Leer num2
		si num2<0 Entonces
			Escribir 'el numero ingresado no es valido'
		SiNo
			Escribir 'ingrese el tercer numero'
			leer num3
			si num3<0 Entonces
				escribir'el numero ingresado no es valido'
			SiNo
				si num1>num2 y num2>num3 Entonces
					Escribir 'el numero mayor es ',num1
					Escribir 'el numero menor es ',num3
				FinSi
				si num1>num3 y num3>num2 Entonces
					Escribir 'el numero mayor es ',num1
					Escribir 'el numero menor es ',num2
				FinSi
				si num2>num1 y num1>num3 Entonces
					Escribir 'el numero mayor es ',num2
					Escribir 'el numero menor es ',num3
				FinSi
				si num2>num3 y num3>num1 Entonces
					Escribir 'el numero mayor es ',num2
					Escribir 'el numero menor es ',num1
				FinSi
				si num3>num2 y num2>num1 Entonces
					Escribir 'el numero mayor es ',num3
					Escribir 'el numero menor es ',num1
				FinSi
				si num3>num1 y num1>num2 Entonces
					Escribir 'el numero mayor es ',num3
					Escribir 'el numero menor es ',num2
				FinSi
				si num1=num2 y num2=num3 Entonces
					Escribir 'los numeros son iguales'
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
