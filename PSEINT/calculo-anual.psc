Algoritmo sin_titulo
	definir edad,montoAnual,aporteSindic1,aportesindic2,aportesindic3,aportesindic4,porcent1,porcent2,porcent3,porcent4,aporteSindic1_1,aporteSindic2_2,aporteSindic3_3,aporteSindic4_4 Como numero
	Escribir 'indique su edad'
	Leer edad
	Escribir 'indique su sueldo anual'
	Leer montoAnual
	porcent1<-montoAnual*0.005
	porcent2<-montoAnual*0.01
	porcent3<-montoAnual*0.02
	porcent4<-montoAnual*0.025
	aporteSindic1_1<-porcent1*0.20
	aporteSindic2_2<-porcent2*0.20
	aporteSindic3_3<-porcent3*0.20
	aporteSindic4_4<-porcent4*0.20
	si montoAnual<10000 Y edad<=30 Entonces
		Escribir 'su aporte al sindicato es de: ', aporteSindic1_1, ' dolares'
	SiNo
		si montoAnual<10000 Y edad>30 Entonces
			aporteSindic1<-porcent1
			Escribir 'su aporte al sindicado es de: ', aporteSindic1, ' dolares'
		SiNo
			si 10000<=montoAnual Y montoAnual<30000 Y edad<=30 Entonces
				Escribir 'su aporte al sindicato es de: ', aporteSindic2_2, ' dolares'
			SiNo
				si 10000<=montoAnual Y montoAnual<20000 Y edad>30 Entonces
				 aportesindic2<-porcent2
					Escribir 'su aporte al sindicato es de: ',aportesindic2, ' dolares'
				SiNo
					si 20000<=montoAnual Y montoAnual<30000 Y edad<=30 Entonces
						Escribir 'su aporte al sindicato es de: ', aporteSindic3_3, ' dolares'
					SiNo 
						si 20000<=montoAnual Y montoAnual<30000 Y edad>30 Entonces
							aportesindic3<-porcent3
							Escribir 'su aporte al sindicato es de: ', aportesindic3, ' dolares'
						sino
							si montoAnual>30000 Y edad<=30 Entonces
								Escribir 'su aporte al sindicato es de: ', aporteSindic4_4, ' dolares'
							SiNo
								si montoAnual>30000 Y edad>30 Entonces
									aportesindic4<-porcent4
									Escribir 'su aporte al sindicato es de: ',aportesindic4, ' dolares'
								SiNo
									Escribir 'entonces no haga nada'
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
