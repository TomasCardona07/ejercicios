#este programa guarda 5 edades y al final saca promedio de las mismas
print('ingrese la primera edad:')
edad1=float(input())
intentos1=5
while edad1<0 and intentos1>1:
    print('la edad no puede ser negativa')
    intentos1=intentos1-1
    print(f'tiene {intentos1} intentos restantes')
    print('ingrese la edad nuevamente:')
    edad1=float(input())
if intentos1==1:
    print('intentos agotados, no puede seguir')
else:
    print('ingrese la segunda edad:')
edad2=float(input())
intentos2=5
while edad2<0 and intentos2>1:
    print('la edad no puede ser negativa')
    intentos2=intentos2-1
    print(f'tiene {intentos2} intentos restantes')
    print('ingrese la edad nuevamente:')
    edad1=float(input())
if intentos2==1:
    print('intentos agotados, no puede seguir')
else:
    print('ingrese la tercera edad:')
edad3=float(input())
intentos3=5
while edad3<0 and intentos3>1:
    print('la edad no puede ser negativa')
    intentos3=intentos3-1
    print(f'tiene {intentos3} intentos restantes')
    print('ingrese la edad nuevamente:')
    edad4=float(input())
if intentos3==1:
    print('intentos agotados, no puede seguir')
else:
    print('ingrese la cuarta edad:')
edad4=float(input())
intentos4=5
while edad4<0 and intentos4>1:
    print('la edad no puede ser negativa')
    intentos4=intentos4-1
    print(f'tiene {intentos4} intentos restantes')
    print('ingrese la edad nuevamente:')
    edad4=float(input())
if intentos4==1:
    print('intentos agotados, no puede seguir')
else:
    print('ingrese la quinta edad:')
edad5=float(input())
intentos5=5
while edad5<0 and intentos5>1:
    print('la edad no puede ser negativa')
    intentos5=intentos5-1
    print(f'tiene {intentos5} intentos restantes')
    print('ingrese la edad nuevamente:')
    edad1=float(input())
if intentos5==1:
    print('intentos agotados, no se puede sacar el promedio')
promediosub=edad1+edad2+edad3+edad4+edad5
promedioTotal=promediosub/5
if  intentos5>1:
    print(f'el promedio de las edades es{promedioTotal} años')