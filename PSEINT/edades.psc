Algoritmo sin_titulo
	Definir edad1, edad2, edad3, edad4, edad5 Como numero
	intentos1 <- 5
	contador1 <- 0
	Escribir 'ingrese la primera edad'
	Leer edad1
	Mientras edad1<=0 Y contador1<4 Hacer
		intentos1 <- intentos1-1
		Escribir 'la primera edad es incorrecta, solo se pueden numeros postivos'
		Escribir 'tiene ', intentos1, ' intentos restantes'
		contador1 <- contador1+1
		Escribir 'ingrese la primera edad'
		Leer edad1
	FinMientras
	Si intentos1=1 Entonces
		Escribir 'intentos agotados, no puede seguir'
	SiNo
		intentos2 <- 5
		contador2 <- 0
		Escribir 'ingrese la segunda edad'
		Leer edad2
		Mientras edad2<=0 Y contador2<4 Hacer
			intentos2 <- intentos2-1
			Escribir 'la segunda edad es incorrecta, solo se pueden numeros postivos'
			Escribir 'tiene ', intentos2, ' intentos restantes'
			contador2 <- contador2+1
			Escribir 'ingrese la segunda edad'
			Leer edad2
		FinMientras
		Si intentos2=1 Entonces
			Escribir 'intentos agotados, no puede seguir'
		SiNo
			intentos3 <- 5
			contador3 <- 0
			Escribir 'ingrese la tercera edad'
			Leer edad3
			Mientras edad3<=0 Y contador3<4 Hacer
				intentos3 <- intentos3-1
				Escribir 'la tercera edad es incorrecta, solo se pueden numeros postivos'
				Escribir 'tiene ', intentos3, ' intentos restantes'
				contador3 <- contador3+1
				Escribir 'ingrese la tercera edad'
				Leer edad3
			FinMientras
			Si intentos3=1 Entonces
				Escribir 'intentos agotados, no puede seguir'
			SiNo
				intentos4 <- 5
				contador4 <- 0
				Escribir 'ingrese la cuarta edad'
				Leer edad4
				Mientras edad4<=0 Y contador4<4 Hacer
					intentos4 <- intentos4-1
					Escribir 'la cuarta edad es incorrecta, solo se pueden numeros postivos'
					Escribir 'tiene ', intentos4, ' intentos restantes'
					contador4 <- contador4+1
					Escribir 'ingrese la cuarta edad'
					Leer edad4
				FinMientras
				Si intentos4=1 Entonces
					Escribir 'intentos agotados, no puede seguir'
				SiNo
					contador5 <- 0
					intentos5 <- 5
					Escribir 'ingrese la quinta edad'
					Leer edad5
					Mientras edad5<=0 Y contador5<4 Hacer
						intentos5 <- intentos5-1
						Escribir 'la quinta edad es incorrecta, solo se pueden numeros postivos'
						Escribir 'tiene ', intentos5, ' intentos restantes'
						contador5 <- contador5+1
						Escribir 'ingrese la quinta edad'
						Leer edad5
					FinMientras
					Si intentos5=1 Entonces
						Escribir 'intentos agotados, no se puede mostrar el promedio'
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	resultadoSuma <- edad1+edad2+edad3+edad4+edad5
	promedio <- resultadoSuma/5
	si intentos5>1 Entonces
		Escribir 'el promedio de las edades es: ', promedio, ' años'
	FinSi
FinAlgoritmo
