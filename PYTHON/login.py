#creacion de correo y contraseña
print('cree su correo electronico')
CORREO=str(input())
print('cree su contraseña')
CONTRASEÑA=str(input())
print('ingrese el correo electronico para ingresar')
correo=str(input())
print('ingrese la contraseña para continuar')
contraseña=str(input())
#Login
#si correo y contraseña son incorrectos:
contraseña_and_correo=True
if correo!=CORREO and contraseña!=CONTRASEÑA:
    contraseña_and_correo=False
if correo!=CORREO and contraseña!=CONTRASEÑA and contraseña_and_correo==False:
    intentos_correo=4
    print('el correo electronico y la contraseñan son incorrectos')
    print('ingrese su correo electronico nuevamente')
    correo=str(input())
    #bucle de ingresar el correo nuevamente(tiene 5 intentos en total):
    while correo!=CORREO and intentos_correo>1:
        intentos_correo=intentos_correo-1
        print(f'correo incorrecto, le quedan {intentos_correo} intentos restantes')
        print('ingrese su correo electronico nuevamente')
        correo=str(input())
        #si no ingresa el correo correctamente los intentos llegan a "1" y no puede segur con la contraseña:
    if intentos_correo==1 and correo!=CORREO:
        print('intentos agotados, no puede seguir')
    else:
        #si ingresa bien el correo, puede entrar a ingresar la contraseña:
        print('correo electronico correcto, pero la contraseña sigue siendo incorrecta')
        print('ingrese su contraseña nuevamente')
        contraseña=str(input())
        intentos_contraseña=4
        #bucle de ingresar la contraseña nuevamente(tiene 5 intentos en total):
        while contraseña!=CONTRASEÑA:
            intentos_contraseña=intentos_contraseña-1
            print(f'contraseña incorrecta le quedan {intentos_contraseña} intentos restantes')
            print('ingrese su contraseña nuevamente')
            contraseña=str(input())
            #si no ingresa la contraseña correctamente los intentos llegan a "1 y no puede seguir"
            if intentos_contraseña==1 and contraseña!=CONTRASEÑA:
                print('intentos agotados, no puede seguir')
                contraseña_and_correo=False
            else:
                print('contraseña correcta, puede ingresar')
#si tiene el correo bien, pero la contraseña incorrecta entra a este condicional:
if contraseña!=CONTRASEÑA and contraseña_and_correo==True:
    intentos_contraseña2=4
    print('contraseña incorrecta')
    print('ingrese su contraseña nuevamente')
    contraseña=str(input())
    #bucle de ingresar contraseña nuevamente(tiene 5 intentos en total)
    while contraseña!=CONTRASEÑA and intentos_contraseña2>1:
        intentos_contraseña2=intentos_contraseña2-1
        print(f'contraseña incorrecta, tiene {intentos_contraseña2} intentos restantes')
        print('ingrese su contraseña nuevamente')
        contraseña=str(input())
    if intentos_contraseña2==1 and contraseña!=CONTRASEÑA:
        print('intentos agotados, no puede ingresar')
    else:
        print('contraseña correcta, si puedes ingresar')
#si tiene la contraseña correcta pero el correo incorrecto entra a este condicional:
if correo!=CORREO and contraseña_and_correo==True:
    intentos_correo2=4
    print('correo electronico incorrecto')
    print('ingrese su correo electronico nuevamente')
    correo=str(input())
    while correo!=CORREO and intentos_correo2>1: 
        intentos_correo2=intentos_correo2-1
        print(f'correo electronico incorrecto, tiene {intentos_correo2} intentos restantes')
        print('ingrese su correo electronico nuevamente')
        correo=str(input())
    if intentos_correo2==1 and correo!=CORREO:
        print('intentos agotados, no puede ingresar')
    else:
        print('correo electronico correcto, puede ingresar al programa')
if correo==CORREO and contraseña==CONTRASEÑA:
    print('bienvenido al programa')
    print('elije el programa al que quieres acceder')