Algoritmo calculadora
	escribir"esto es una calculadora donde se multiplica, se divide,se suma y se resta a base de logica (verdadero o falso)"
	definir suma, resta, multiplicacion, division, resultadoSuma, num1, num2, resultadoResta, resultadoMultiplicacion Como Entero
	definir resultadoDivision Como Real
	escribir"indique el primer numero para realizar la operacion"
	leer num1
	escribir"indique el segundo numero para realizar la operacion"
	leer num2
	definir tipoOperacion1, tipoOperacion2, tipoOperacion3, tipoOperacion4 Como Logico
	escribir"desea hacer una suma?, responda con (verdadero o falso)"
	leer tipoOperacion1
	si tipoOperacion1 Entonces
		resultadoSuma <- num1 + num2
		escribir"el resultado de la suma es :" resultadoSuma
	SiNo
		Escribir"desea hacer una resta?, responda con (verdadero o falso)"
		leer tipoOperacion2
		si tipoOperacion2 Entonces
			resultadoResta <- num1 - num2
			Escribir "el resultado de la resta es :" resultadoResta
		sino
			escribir"desea hacer una multiplicacion?, responda con (verdadero o falso)"
			leer tipoOperacion3
			si tipoOperacion3 Entonces
				resultadoMultiplicacion <- num1 * num2
				Escribir "el resultado de la multiplicacion es :" resultadoMultiplicacion
			sino
				resultadoDivision <- num1/num2
				Escribir "el rsultado de la division es: " resultadoDivision
			FinSi
		FinSi
	FinSi
FinAlgoritmo


