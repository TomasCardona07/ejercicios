Algoritmo sin_titulo
	definir hora Como entero
	Escribir 'indique la hora en formato 24 horas (0-24) (SOLO LA HORA, NO MINUTOS)'
	leer hora
	si 0<=hora & hora<=5 Entonces
		Escribir 'el momento del dia es: madrugada'
	SiNo
		si 6<=hora & hora<=11 Entonces
			Escribir 'el momento del dia es: mañana'
		SiNo
			si 12<=hora & hora<=13 Entonces
				Escribir 'el momento del dia es: mediodia'
			sino
				si 14<=hora & hora<=19 Entonces
					Escribir 'el momento del dia es: tarde'
				SiNo
					si 20<=hora & hora<=23 Entonces
						Escribir 'el momento del dia es: noche'
					SiNo
						Escribir 'error, no se indicaron los parametros correctamente'
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
