Algoritmo sin_titulo
	definir num1,num2 como numero
	definir operacion Como Caracter
	Escribir 'indique el primer numero para realizar la operacion'
	Leer num1
	Escribir 'indique el segundo numero para realizar la operacion'
	leer num2
	Escribir "indique el signo que representa la operacion que desea hacer, ejemplo:"
	Escribir '[+] suma'
	Escribir '[-] resta'
	Escribir '[*] multiplicacion'
	Escribir '[/] division'
	Leer operacion
	Segun operacion Hacer
		"+":
			resultadoSuma<-num1+num2
			Escribir 'el resultado de la suma es: ',resultadoSuma
		"-":
			resultadoResta<-num1-num2
			Escribir 'el resultado de la resta es: ',resultadoResta
		"*":
			resultadoMultiplicacion<-num1*num2
			Escribir 'el resultado de la multiplicacion es: ',resultadoMultiplicacion
		"/": si num1==0 o num2==0 Entonces
				Escribir 'no se puede dividir por cero'
			SiNo
				resultadoDivision<-num1/num2
				Escribir 'el resultado de la divison es: ',resultadoDivision
			finsi
	    De Otro Modo:
			Escribir 'indique los simbolos mostrados por favor'

	FinSegun
	
FinAlgoritmo
