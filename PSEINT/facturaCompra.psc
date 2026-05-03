Algoritmo facturaCompra
	definir codigoProd, cantCompra, valorProd,precioNormal,valorTotal,subTotal como numero
	definir detalleProd,valorMedida Como Caracter
	Escribir "indique el codigo del producto"
	leer codigoProd
	Escribir "indique la cantidad que desea comprar"
	leer cantCompra
	escribir"indique el detalle del producto"
	Leer detalleProd
	Escribir "indique el valor del producto"
	Leer valorProd
	Escribir "indique las medidas del producto como KG, LB, GR, etc.."
	Leer valorMedida
	precioNormal<- cantCompra*valorProd
	subTotal<-precioNormal*0.19
	valorTotal<-precioNormal+subTotal
	Escribir "el codigo del producto es: " codigoProd
	Escribir "la cantidad de productos comprada es: " cantCompra
	Escribir "el detalle del producto que compro es :" detalleProd
	Escribir "el valor de producto es: " valorProd
	Escribir "las medidas del producto son: " valorMedida
	Escribir "el valor total de la compra es: " valorTotal
	
	
FinAlgoritmo
