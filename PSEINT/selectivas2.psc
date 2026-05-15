Algoritmo selectivas2
	Definir edad1,edad2, aDiferencia,hMayor como numero
	Mostrar 'ingrese la edad del primer hermano'
	Leer edad1
	Mostrar 'ingrese la edad del segundo hermano'
	Leer edad2
	si (edad1 > edad2) Entonces
		aDiferencia<- (edad1 - edad2)
		hMayor<-edad1
		Mostrar 'el mayor tiene: ',hMayor, ' años'
		Mostrar 'la diferencia de edad es de: ',aDiferencia,' años'
	SiNo
		aDiferencia<- (edad2 - edad1)
		hMayor<-edad2
		Mostrar 'el mayor tiene: ',hMayor, ' años'
		Mostrar 'la diferencia de edad es de: ',aDiferencia,' años'
	FinSi
FinAlgoritmo
