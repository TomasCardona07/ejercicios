Algoritmo sin_titulo
	definir monto Como Entero
	Escribir 'esto es un programa donde ingresas un monto en dinero y te responde con cuantos billetes se paga ese monto'
	escribir "digite el monto total a pagar"
	leer monto
	definir b100,b50,b20,b10,b5,b2 Como Entero
	b100<- trunc(monto/100)
	monto <- monto%100
	b50<- trunc(monto/50)
	monto <- monto%50
	b20<- trunc(monto/20)
	monto <- monto%20
	b10<- trunc(monto/10)
	monto <- monto%10
	b5<- trunc(monto/5)
	monto <- monto%5
	b2<- trunc(monto/2)
	monto <- monto%2
	escribir"billetes de 100 :",b100
	escribir"billetes de 50 :",b50
	escribir"billetes de 20 :",b20
	escribir"billetes de 10 :",b10
	escribir"billetes de 5 :",b5
	escribir"billetes de 2 :",b2
	Escribir'billete de 1: ' monto
	FinAlgoritmo
