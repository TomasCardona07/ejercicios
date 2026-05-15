Algoritmo selectivas1
	Definir sijp,segurSocial como texto
	Definir aNaci como numero
	Mostrar 'ingrese su año de nacimiento'
	Leer aNaci
	Mostrar '¿Pertenece al sistema integrado de jubilacion y pensiones? [S] or [N]'
	Leer sijp
	Mostrar '¿Gestiona alguna prestacion o servicio de seguridad social [S] or [N]?'
	Leer segurSocial
	aActual<-2026
	edadUsuario<- (aActual - aNaci)
	si (edadUsuario >= 18 Y (sijp = "S" O segurSocial = "S")) Entonces
		Mostrar 'Si debe sacar el CUIL'
	SiNo
		Mostrar 'no debe sacar el CUIL'
	FinSi
FinAlgoritmo
