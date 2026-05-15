Algoritmo selectivas3
	Definir lun, mart, mier, juev, viern, sab como numero
	Mostrar 'ingrese la cantidad de produccion en unidades del dia lunes'
	Leer lun
	Mostrar 'ingrese la cantidad de produccion en unidades del dia martes'
	Leer mart
	Mostrar 'ingrese la cantidad de produccion en unidades del dia miercoles'
	Leer mier
	Mostrar 'ingrese la cantidad de produccion en unidades del dia jueves'
	Leer juev
	Mostrar 'ingrese la cantidad de produccion en unidades del dia viernes'
	Leer viern
	Mostrar 'ingrese la cantidad de produccion en unidades del dia sabado'
	Leer sab
	cantidad <- (lun + mart + mier + juev + viern + sab) / 6
	si (cantidad >= 100) Entonces
		Mostrar 'el operario si recibe incentivos'
	SiNo
		Mostrar 'el operario no recibe incentivos'
	FinSi
FinAlgoritmo
