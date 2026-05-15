Algoritmo selectivas7
	Definir monto,bonificacion como numero
	Mostrar 'Ingrese el monto de venta'
	Leer monto
	si (monto < 1000) Entonces
		Mostrar 'no recibe porcentaje de bonificacion'
	SiNo
		si (monto >= 1000  Y monto < 5000) Entonces
			bonificacion <- (monto * 0.03)
			Mostrar 'su porcentaje de su bonificacion es del 3%'
			Mostrar 'su bonificacion es de: ', bonificacion
		SiNo
			si (monto >= 5000 Y monto < 20000) Entonces
				bonificacion <- (monto * 0.05)
				Mostrar 'su porcentaje de su bonificacion es del 5%'
				Mostrar 'su bonificacion es de: ', bonificacion
			SiNo
				bonificacion <- (monto * 0.08)
				Mostrar 'su porcentaje de bonificacion es del 8%'
				Mostrar 'su bonificacion es de: ', bonificacion
			FinSi
		FinSi
	FinSi
FinAlgoritmo
