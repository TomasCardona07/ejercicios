Algoritmo sin_titulo
	definir precioU,monto,montoTotal Como Real	
	definir cantidad, contador Como Entero
	Definir producto, desicion Como Caracter
	contador=0
	Repetir
		contador<-contador+1
		Escribir 'ingrese el nombre del producto ',contador
		Leer producto
		Escribir 'ingrese la cantidad del producto: ',producto
		Leer cantidad
		Escribir 'ingrese el precio unitario del producto ',producto
		leer precioU
		Escribir "desea agregar otro producto?, responda con [S] para afirmar o [N] para negar"
		Leer desicion
		monto<-cantidad*precioU
		montoTotal<-montoTotal+monto
		contadorP<-producto+', '+contadorP
		Mientras desicion<>'s' y desicion<>'S' y desicion<>'n' y desicion<>'N' Hacer
			Escribir 'desicion incorrecta, por favor ingrese unicamente [S/N]'
			Leer desicion
		FinMientras
	Hasta Que desicion='N' o desicion='n'
	Escribir 'productos comprados: ',contadorP
	Escribir 'el monto total de los productos es de: ',montoTotal,' pesos'
FinAlgoritmo
