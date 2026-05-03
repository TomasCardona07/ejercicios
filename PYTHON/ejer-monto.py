#ingreso de datos
edad = int(input("Ingrese su edad: "))
montoAnual = float(input("Ingrese su monto anual: "))
#proceso
#variables para mayor de 30 años
monto1=montoAnual*0.005
monto2=montoAnual*0.01
monto3=montoAnual*0.02
monto4=montoAnual*0.025
#variables para menor de 30 años
porcentaje1=monto1*0.20
porcentaje2=monto2*0.20
porcentaje3=monto3*0.20 
porcentaje4=monto4*0.20
total1=monto1+porcentaje1
total2=monto2+porcentaje2
total3=monto3+porcentaje3
total4=monto4+porcentaje4
#condicionales
if 10000>montoAnual and edad<=30:
    print('el aporte al sindicato es de: ',total1)
elif 10000>montoAnual and edad>30:
    print('el aporte al sindicato es de: ',monto1)
elif 10000<=montoAnual<20000 and edad<=30:
    print('el aporte al sindicato es de: ',total2)
elif 10000<=montoAnual<20000 and edad>30:
    print('el aporte al sindicato es de: ',monto2)
elif 20000<=montoAnual<30000 and edad<=30:
    print('el aporte al sindicato es de: ',total3)
elif 20000<=montoAnual<30000 and edad>30:
    print('el aporte al sindicato es de: ',monto3)
elif montoAnual>=30000 and edad<=30:
    print('el aporte al sindicato es de: ',total4) 
elif montoAnual>=30000 and edad>30:
    print('el aporte al sindicato es de: ',monto4)