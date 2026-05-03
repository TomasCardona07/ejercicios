Algoritmo ejercicio6
	Definir ladoA, ladoB, ladoC, semiperimetro, area como numero
	Escribir 'ingrese el primer lado del triangulo'
	Leer ladoA
	Escribir 'ingrese el segundo lado del triangulo'
	Leer ladoB
	Escribir 'ingrese el tercer lado del triangulo'
	Leer ladoC
	semiperimetro<-(ladoA+ladoB+ladoC)/2
	area<- RC (semiperimetro*(semiperimetro-ladoA)*(semiperimetro-ladoB)*(semiperimetro-ladoC))
	Escribir 'el area del triangulo es: ', area
FinAlgoritmo
