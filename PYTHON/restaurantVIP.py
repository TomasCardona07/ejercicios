#contadores:
contDebito=0
contCredito=0
contEfectivo=0
contDiario=0
#informacion de la mesa numero 1:
print('mesa numero 1')
print('ingrese la cantidad de comensales de la primera mesa (maximo 4)')
comensales_1=int(input())
costoBase1=comensales_1*2000
#ciclo de la mesa 1 cuando el numero de personas es incorrecto
while comensales_1<1 or comensales_1>4:
    if comensales_1<1:
        print('el valor tiene que ser positvo')
        comensales_1=int(input())
    elif comensales_1>4:
        print('el valor supera el maximo permitido')
        comensales_1=int(input())
#metodo de pago de la mesa 1
print('ingrese el metodo de pago de la mesa 1(debito, credito o efectivo)')
pago_1=input().strip().lower()
while pago_1!='debito' and pago_1!='credito' and pago_1!='efectivo':
    print('metodo de pago incorrecto')
    print('ingrese correctamente el metodo de pago [debito, credito o efectivo]')
    pago_1=input().strip().lower()
#condicionales para elegir el metodo de pago y realizar sus respectivos valores
if 'debito' in pago_1:
    print('metodo de pago: debito')
    recargoDebito1=costoBase1*0.03
    print(f'el recargo es del 3%: {recargoDebito1}')
    totalDebito1=costoBase1+recargoDebito1
    print(f'el costo final de la mesa 1 es: {totalDebito1}')
    contDebito=contDebito+1
    contDiario=contDiario+totalDebito1
elif 'credito' in pago_1:
    contCredito=contCredito+1
    print('metodo de pago: credito')
    print('ingrese el numero de cuotas')
    cuotas_1=int(input())
    while cuotas_1<1 or cuotas_1>12:
        if cuotas_1<1:
            print('el valor tiene que ser positivo')
            cuotas_1=int(input())
        elif cuotas_1>12:
            print('el valor supera el maximo permitido')
            cuotas_1=int(input())
    if cuotas_1<=8:
        recargoCredito1=(costoBase1*0.025)*cuotas_1
    else:
        cuotas_1=8
        recargoCredito1=(costoBase1*0.025)*cuotas_1
    totalCredito1=recargoCredito1+costoBase1
    print(f'el recargo fue de: {recargoCredito1}')
    print(f'el costo final de la mesa 1 es: {totalCredito1}')
    contDiario=contDiario+totalCredito1
elif 'efectivo' in pago_1:
    print('metodo de pago: efectivo')
    print('no contiene recargos')
    totalEfectivo1=costoBase1
    print(f'el costo de la mesa 1 es: {totalEfectivo1}')
    contDiario=contDiario+totalEfectivo1
    contEfectivo=contEfectivo+1
#informacion de la mesa numero 2:
print('mesa numero 2')
print('ingrese la cantidad de comensales de la segunda mesa (maximo 4)')
comensales_2=int(input())
costoBase2=comensales_2*2000
#ciclo de la mesa 2 cuando el numero de personas es incorrecto
while comensales_2<1 or comensales_2>4:
    if comensales_2<1:
        print('el valor tiene que ser positvo')
        comensales_2=int(input())
    elif comensales_2>4:
        print('el valor supera el maximo permitido')
        comensales_2=int(input())
#metodo de pago de la mesa 2
print('ingrese el metodo de pago de la mesa 2(debito, credito o efectivo)')
pago_2=input().strip().lower()
while pago_2!='debito' and pago_2!='credito' and pago_2!='efectivo':
    print('metodo de pago incorrecto')
    print('ingrese correctamente el metodo de pago [debito, credito o efectivo]')
    pago_2=input().strip().lower()
#condicionales para elegir el metodo de pago y realizar sus respectivos valores
if 'debito' in pago_2:
    print('metodo de pago: debito')
    recargoDebito2=costoBase2*0.03
    print(f'el recargo es del 3%: {recargoDebito2}')
    totalDebito2=costoBase2+recargoDebito2
    print(f'el costo final de la mesa 1 es: {totalDebito2}')
    contDebito=contDebito+1
    contDiario=contDiario+totalDebito1
elif 'credito' in pago_2:
    contCredito=contCredito+1
    print('metodo de pago: credito')
    print('ingrese el numero de cuotas')
    cuotas_2=int(input())
    while cuotas_2<1 or cuotas_2>12:
        if cuotas_2<1:
            print('el valor tiene que ser positivo')
            cuotas_2=int(input())
        elif cuotas_2>12:
            print('el valor supera el maximo permitido')
            cuotas_2=int(input())
    if cuotas_2<=8:
        recargoCredito2=(costoBase2*0.025)*cuotas_2
    else:
        cuotas_2=8
        recargoCredito2=(costoBase2*0.025)*cuotas_2
    totalCredito2=recargoCredito2+costoBase2
    print(f'el recargo fue de: {recargoCredito2}')
    print(f'el costo final de la mesa 2 es: {totalCredito2}')
    contDiario=contDiario+totalCredito2
elif 'efectivo' in pago_2:
    print('metodo de pago: efectivo')
    print('no contiene recargos')
    totalEfectivo2=costoBase2
    print(f'el costo de la mesa 2 es: {totalEfectivo2}')
    contDiario=contDiario+totalEfectivo2
    contEfectivo=contEfectivo+1
#informacion de la mesa numero 3:
print('mesa numero 3')
print('ingrese la cantidad de comensales de la tercera mesa (maximo 4)')
comensales_3=int(input())
costoBase3=comensales_3*2000
#ciclo de la mesa 3 cuando el numero de personas es incorrecto
while comensales_3<1 or comensales_3>4:
    if comensales_3<1:
        print('el valor tiene que ser positvo')
        comensales_3=int(input())
    elif comensales_3>4:
        print('el valor supera el maximo permitido')
        comensales_3=int(input())
#metodo de pago de la mesa 3
print('ingrese el metodo de pago de la mesa 3(debito, credito o efectivo)')
pago_3=input().strip().lower()
while pago_3!='debito' and pago_3!='credito' and pago_3!='efectivo':
    print('metodo de pago incorrecto')
    print('ingrese correctamente el metodo de pago [debito, credito o efectivo]')
    pago_3=input().strip().lower()
#condicionales para elegir el metodo de pago y realizar sus respectivos valores
if 'debito' in pago_3:
    print('metodo de pago: debito')
    recargoDebito3=costoBase3*0.03
    print(f'el recargo es del 3%: {recargoDebito3}')
    totalDebito3=costoBase3+recargoDebito3
    print(f'el costo final de la mesa 3 es: {totalDebito3}')
    contDebito=contDebito+1
    contDiario=contDiario+totalDebito3
elif 'credito' in pago_3:
    contCredito=contCredito+1
    print('metodo de pago: credito')
    print('ingrese el numero de cuotas')
    cuotas_3=int(input())
    while cuotas_3<1 or cuotas_3>12:
        if cuotas_3<1:
            print('el valor tiene que ser positivo')
            cuotas_3=int(input())
        elif cuotas_3>12:
            print('el valor supera el maximo permitido')
            cuotas_3=int(input())
    if cuotas_3<=8:
        recargoCredito3=(costoBase3*0.025)*cuotas_3
    else:
        cuotas_3=8
        recargoCredito3=(costoBase3*0.025)*cuotas_3
    totalCredito3=recargoCredito3+costoBase3
    print(f'el recargo fue de: {recargoCredito3}')
    print(f'el costo final de la mesa 3 es: {totalCredito3}')
    contDiario=contDiario+totalCredito3
elif 'efectivo' in pago_3:
    print('metodo de pago: efectivo')
    print('no contiene recargos')
    totalEfectivo3=costoBase3
    print(f'el costo de la mesa 3 es: {totalEfectivo3}')
    contDiario=contDiario+totalEfectivo3
    contEfectivo=contEfectivo+1
#informacion de la mesa numero 4:
print('mesa numero 4')
print('ingrese la cantidad de comensales de la cuarta mesa (maximo 4)')
comensales_4=int(input())
costoBase4=comensales_4*2000
#ciclo de la mesa 4 cuando el numero de personas es incorrecto
while comensales_4<1 or comensales_4>4:
    if comensales_4<1:
        print('el valor tiene que ser positvo')
        comensales_4=int(input())
    elif comensales_4>4:
        print('el valor supera el maximo permitido')
        comensales_4=int(input())
#metodo de pago de la mesa 4
print('ingrese el metodo de pago de la mesa 4(debito, credito o efectivo)')
pago_4=input().strip().lower()
while pago_4!='debito' and pago_4!='credito' and pago_4!='efectivo':
    print('metodo de pago incorrecto')
    print('ingrese correctamente el metodo de pago [debito, credito o efectivo]')
    pago_4=input().strip().lower()
#condicionales para elegir el metodo de pago y realizar sus respectivos valores
if 'debito' in pago_4:
    print('metodo de pago: debito')
    recargoDebito4=costoBase4*0.03
    print(f'el recargo es del 3%: {recargoDebito4}')
    totalDebito4=costoBase4+recargoDebito4
    print(f'el costo final de la mesa 4 es: {totalDebito4}')
    contDebito=contDebito+1
    contDiario=contDiario+totalDebito4
elif 'credito' in pago_4:
    contCredito=contCredito+1
    print('metodo de pago: credito')
    print('ingrese el numero de cuotas')
    cuotas_4=int(input())
    while cuotas_4<1 or cuotas_4>12:
        if cuotas_4<1:
            print('el valor tiene que ser positivo')
            cuotas_4=int(input())
        elif cuotas_4>12:
            print('el valor supera el maximo permitido')
            cuotas_4=int(input())
    if cuotas_4<=8:
        recargoCredito4=(costoBase4*0.025)*cuotas_4
    else:
        cuotas_4=8
        recargoCredito4=(costoBase4*0.025)*cuotas_4
    totalCredito4=recargoCredito4+costoBase4
    print(f'el recargo fue de: {recargoCredito4}')
    print(f'el costo final de la mesa 4 es: {totalCredito4}')
    contDiario=contDiario+totalCredito4
elif 'efectivo' in pago_4:
    print('metodo de pago: efectivo')
    print('no contiene recargos')
    totalEfectivo4=costoBase4
    print(f'el costo de la mesa 4 es: {totalEfectivo4}')
    contDiario=contDiario+totalEfectivo4
    contEfectivo=contEfectivo+1
#informacion de la mesa numero 5:
print('mesa numero 5')
print('ingrese la cantidad de comensales de la quinta mesa (maximo 4)')
comensales_5=int(input())
costoBase5=comensales_5*2000
#ciclo de la mesa 5 cuando el numero de personas es incorrecto
while comensales_5<1 or comensales_5>4:
    if comensales_5<1:
        print('el valor tiene que ser positvo')
        comensales_5=int(input())
    elif comensales_5>4:
        print('el valor supera el maximo permitido')
        comensales_5=int(input())
#metodo de pago de la mesa 5
print('ingrese el metodo de pago de la mesa 5(debito, credito o efectivo)')
pago_5=input().strip().lower()
while pago_5!='debito' and pago_5!='credito' and pago_5!='efectivo':
    print('metodo de pago incorrecto')
    print('ingrese correctamente el metodo de pago [debito, credito o efectivo]')
    pago_5=input().strip().lower()
#condicionales para elegir el metodo de pago y realizar sus respectivos valores
if 'debito' in pago_5:
    print('metodo de pago: debito')
    recargoDebito5=costoBase5*0.03
    print(f'el recargo es del 3%: {recargoDebito5}')
    totalDebito5=costoBase5+recargoDebito5
    print(f'el costo final de la mesa 5 es: {totalDebito5}')
    contDebito=contDebito+1
    contDiario=contDiario+totalDebito5
elif 'credito' in pago_5:
    contCredito=contCredito+1
    print('metodo de pago: credito')
    print('ingrese el numero de cuotas')
    cuotas_5=int(input())
    while cuotas_5<1 or cuotas_5>12:
        if cuotas_5<1:
            print('el valor tiene que ser positivo')
            cuotas_5=int(input())
        elif cuotas_5>12:
            print('el valor supera el maximo permitido')
            cuotas_5=int(input())
    if cuotas_5<=8:
        recargoCredito5=(costoBase5*0.025)*cuotas_5
    else:
        cuotas_5=8
        recargoCredito5=(costoBase5*0.025)*cuotas_5
    totalCredito5=recargoCredito5+costoBase5
    print(f'el recargo fue de: {recargoCredito5}')
    print(f'el costo final de la mesa 5 es: {totalCredito5}')
    contDiario=contDiario+totalCredito5
elif 'efectivo' in pago_5:
    print('metodo de pago: efectivo')
    print('no contiene recargos')
    totalEfectivo5=costoBase5
    print(f'el costo de la mesa 5 es: {totalEfectivo5}')
    contDiario=contDiario+totalEfectivo5
    contEfectivo=contEfectivo+1
#informacion de la mesa numero 6:
print('mesa numero 6')
print('ingrese la cantidad de comensales de la sexta mesa (maximo 4)')
comensales_6=int(input())
costoBase6=comensales_6*2000
#ciclo de la mesa 6 cuando el numero de personas es incorrecto
while comensales_6<1 or comensales_6>4:
    if comensales_6<1:
        print('el valor tiene que ser positvo')
        comensales_6=int(input())
    elif comensales_6>4:
        print('el valor supera el maximo permitido')
        comensales_6=int(input())
#metodo de pago de la mesa 6
print('ingrese el metodo de pago de la mesa 6(debito, credito o efectivo)')
pago_6=input().strip().lower()
while pago_6!='debito' and pago_6!='credito' and pago_6!='efectivo':
    print('metodo de pago incorrecto')
    print('ingrese correctamente el metodo de pago [debito, credito o efectivo]')
    pago_6=input().strip().lower()
#condicionales para elegir el metodo de pago y realizar sus respectivos valores
if 'debito' in pago_6:
    print('metodo de pago: debito')
    recargoDebito6=costoBase6*0.03
    print(f'el recargo es del 3%: {recargoDebito6}')
    totalDebito6=costoBase6+recargoDebito6
    print(f'el costo final de la mesa 6 es: {totalDebito6}')
    contDebito=contDebito+1
    contDiario=contDiario+totalDebito6
elif 'credito' in pago_6:
    contCredito=contCredito+1
    print('metodo de pago: credito')
    print('ingrese el numero de cuotas')
    cuotas_6=int(input())
    while cuotas_6<1 or cuotas_6>12:
        if cuotas_6<1:
            print('el valor tiene que ser positivo')
            cuotas_6=int(input())
        elif cuotas_6>12:
            print('el valor supera el maximo permitido')
            cuotas_6=int(input())
    if cuotas_6<=8:
        recargoCredito6=(costoBase6*0.025)*cuotas_6
    else:
        cuotas_6=8
        recargoCredito6=(costoBase6*0.025)*cuotas_6
    totalCredito6=recargoCredito6+costoBase6
    print(f'el recargo fue de: {recargoCredito6}')
    print(f'el costo final de la mesa 6 es: {totalCredito6}')
    contDiario=contDiario+totalCredito6
elif 'efectivo' in pago_6:
    print('metodo de pago: efectivo')
    print('no contiene recargos')
    totalEfectivo6=costoBase6
    print(f'el costo de la mesa 6 es: {totalEfectivo6}')
    contDiario=contDiario+totalEfectivo6
    contEfectivo=contEfectivo+1
#informacion de la mesa numero 7:
print('mesa numero 7')
print('ingrese la cantidad de comensales de la septima mesa (maximo 4)')
comensales_7=int(input())
costoBase7=comensales_7*2000
#ciclo de la mesa 7 cuando el numero de personas es incorrecto
while comensales_7<1 or comensales_7>4:
    if comensales_7<1:
        print('el valor tiene que ser positvo')
        comensales_7=int(input())
    elif comensales_7>4:
        print('el valor supera el maximo permitido')
        comensales_7=int(input())
#metodo de pago de la mesa 7
print('ingrese el metodo de pago de la mesa 7(debito, credito o efectivo)')
pago_7=input().strip().lower()
while pago_7!='debito' and pago_7!='credito' and pago_7!='efectivo':
    print('metodo de pago incorrecto')
    print('ingrese correctamente el metodo de pago [debito, credito o efectivo]')
    pago_7=input().strip().lower()
#condicionales para elegir el metodo de pago y realizar sus respectivos valores
if 'debito' in pago_7:
    print('metodo de pago: debito')
    recargoDebito7=costoBase7*0.03
    print(f'el recargo es del 3%: {recargoDebito7}')
    totalDebito7=costoBase7+recargoDebito7
    print(f'el costo final de la mesa 7 es: {totalDebito7}')
    contDebito=contDebito+1
    contDiario=contDiario+totalDebito7
elif 'credito' in pago_7:
    contCredito=contCredito+1
    print('metodo de pago: credito')
    print('ingrese el numero de cuotas')
    cuotas_7=int(input())
    while cuotas_7<1 or cuotas_7>12:
        if cuotas_7<1:
            print('el valor tiene que ser positivo')
            cuotas_7=int(input())
        elif cuotas_7>12:
            print('el valor supera el maximo permitido')
            cuotas_7=int(input())
    if cuotas_7<=8:
        recargoCredito7=(costoBase7*0.025)*cuotas_7
    else:
        cuotas_7=8
        recargoCredito7=(costoBase7*0.025)*cuotas_7
    totalCredito7=recargoCredito7+costoBase7
    print(f'el recargo fue de: {recargoCredito7}')
    print(f'el costo final de la mesa 7 es: {totalCredito7}')
    contDiario=contDiario+totalCredito7
elif 'efectivo' in pago_7:
    print('metodo de pago: efectivo')
    print('no contiene recargos')
    totalEfectivo7=costoBase7
    print(f'el costo de la mesa 7 es: {totalEfectivo7}')
    contDiario=contDiario+totalEfectivo7
    contEfectivo=contEfectivo+1
#informacion de la mesa numero 8:
print('mesa numero 8')
print('ingrese la cantidad de comensales de la octava mesa (maximo 4)')
comensales_8=int(input())
costoBase8=comensales_8*2000
#ciclo de la mesa 8 cuando el numero de personas es incorrecto
while comensales_8<1 or comensales_8>4:
    if comensales_8<1:
        print('el valor tiene que ser positvo')
        comensales_8=int(input())
    elif comensales_8>4:
        print('el valor supera el maximo permitido')
        comensales_8=int(input())
#metodo de pago de la mesa 8
print('ingrese el metodo de pago de la mesa 8(debito, credito o efectivo)')
pago_8=input().strip().lower()
while pago_8!='debito' and pago_8!='credito' and pago_8!='efectivo':
    print('metodo de pago incorrecto')
    print('ingrese correctamente el metodo de pago [debito, credito o efectivo]')
    pago_8=input().strip().lower()
#condicionales para elegir el metodo de pago y realizar sus respectivos valores
if 'debito' in pago_8:
    print('metodo de pago: debito')
    recargoDebito8=costoBase8*0.03
    print(f'el recargo es del 3%: {recargoDebito8}')
    totalDebito8=costoBase8+recargoDebito8
    print(f'el costo final de la mesa 8 es: {totalDebito8}')
    contDebito=contDebito+1
    contDiario=contDiario+totalDebito8
elif 'credito' in pago_8:
    contCredito=contCredito+1
    print('metodo de pago: credito')
    print('ingrese el numero de cuotas')
    cuotas_8=int(input())
    while cuotas_8<1 or cuotas_8>12:
        if cuotas_8<1:
            print('el valor tiene que ser positivo')
            cuotas_8=int(input())
        elif cuotas_8>12:
            print('el valor supera el maximo permitido')
            cuotas_8=int(input())
    if cuotas_8<=8:
        recargoCredito8=(costoBase8*0.025)*cuotas_8
    else:
        cuotas_8=8
        recargoCredito8=(costoBase8*0.025)*cuotas_8
    totalCredito8=recargoCredito8+costoBase8
    print(f'el recargo fue de: {recargoCredito8}')
    print(f'el costo final de la mesa 8 es: {totalCredito8}')
    contDiario=contDiario+totalCredito8
elif 'efectivo' in pago_8:
    print('metodo de pago: efectivo')
    print('no contiene recargos')
    totalEfectivo8=costoBase8
    print(f'el costo de la mesa 8 es: {totalEfectivo8}')
    contDiario=contDiario+totalEfectivo8
    contEfectivo=contEfectivo+1
#resumen del dia:
print('resumen del dia')
print(f'el total recaudado en el dia fue de: {contDiario} pesos')
print(f'el metodo de pago mas utilizado fue: ', end='')
if contDebito >= contCredito and contDebito >= contEfectivo:
    print('debito')
elif contCredito >= contDebito and contCredito >= contEfectivo:
    print('credito')
else:
    print('efectivo')
print(f'y tuvo un total de {contDebito} ventas con debito, {contCredito} ventas con credito y {contEfectivo} ventas con efectivo')