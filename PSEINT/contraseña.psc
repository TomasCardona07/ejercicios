Algoritmo sin_titulo
	definir contraseña1,contraseña2 como texto
	Definir contador, intentos como numero
	intentos<-5
	contador=0
	contraseña1<-'PR4765AtP'
	Escribir 'indique su contraseña'
	leer contraseña2
	Mientras contraseña1<>contraseña2 y contador<4 Hacer
		Escribir 'contraseña incorrecta'
		contador<-contador+1
		intentos<-intentos-1
		Escribir 'le quedan ',intentos,' intentos restantes'
		Escribir 'ingrese su contraseña nuevamente'
		leer contraseña2
	FinMientras
	si contador=4 y contraseña1<>contraseña2 Entonces
		Escribir 'intentos agotados intente de nuevo mas tarde'
	FinSi
	si contraseña1=contraseña2 Entonces
		Escribir 'su contraseña es correcta, puede ingresar'
	FinSi
FinAlgoritmo
