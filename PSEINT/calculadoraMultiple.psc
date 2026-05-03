Algoritmo calculadoraMultiple
	definir operacion,num1,num2 como numero
	escribir 'indique que operacion desea hacer con el numero de la operacion correspondiente:'
	Escribir '[1] suma'
	Escribir '[2] resta'
	Escribir '[3] multiplicacion'
	Escribir '[4] division'
	Leer operacion
	Segun operacion Hacer
		1:
			Escribir 'indique el primer numero para realizar la suma'
			Leer num1
			Escribir 'indique el segundo numero para realizar la suma'
			Leer num2
			resultadoSuma<-num1+num2
			Escribir 'el resultado de la suma es: ', resultadoSuma
		2:
			Escribir 'indique el primer numero para realizar la resta'
			Leer num1
			Escribir 'indique el segundo numero para realizar la resta'
			Leer num2
			resultadoResta<-num1-num2
			Escribir 'el resultado de la resta es: ',resultadoResta
		3:
			Escribir 'indique el primer numero para realizar la multiplicacion'
			Leer num1
			Escribir 'indique el segundo numero para realizar la multiplicacion'
			Leer num2
			resultadoMultiplicacion<-num1*num2
			Escribir 'el resultado de la multiplicacion es: ',resultadoMultiplicacion
		4:
			Escribir 'indique el primer numero para realizar la division'
			Leer num1
			Escribir 'indique el segundo numero para realizar la division'
			Leer num2
			resultadoDivision<-num1/num2
			Escribir 'el resultado de la division es: ',resultadoDivision
		De Otro Modo:
			Escribir 'numero incorrecto'
	Fin Segun
	
FinAlgoritmo
