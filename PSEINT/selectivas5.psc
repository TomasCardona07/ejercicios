Algoritmo selectivas5
	Definir A,B,C como numero
	Mostrar 'ingrese el  primer lado'
	Leer A
	Mostrar 'ingrese el  segundo lado'
	Leer B
	Mostrar 'ingrese el  tercer lado'
	Leer C
	si (A <> B Y B <> C Y A <> C) Entonces
		Mostrar 'es un tringulo escaleno'
	SiNo
		si  (A = B Y B = C ) Entonces
			Mostrar 'es un triangulo equilatero'
		SiNo
			Mostrar 'es un triangulo isoceles'
		FinSi
	FinSi
FinAlgoritmo
