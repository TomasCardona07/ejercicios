#creacion de correo y contraseña
print('cree su correo electronico')
CORREO=str(input())
print('cree su contraseña')
PASSWORD=str(input())
print('ingrese el correo electronico para ingresar')
correo=str(input())
print('ingrese la contraseña para continuar')
password=str(input())
intentos=4
if password==PASSWORD and correo==CORREO:
    print('si puede ingresar')
else:
    print('las credenciales no coinciden')
    while correo!=CORREO and intentos>1  or password!=PASSWORD and intentos>1:
        intentos=intentos-1
        print(f'tiene {intentos} intentos restantes')
        print('ingrese sus credenciales nuevamente:')
        correo=(input('correo:'))
        password=(input('contraseña:'))
        if password==PASSWORD and correo==CORREO:
            print('si puede ingresar')
            break
        else:
            print('credenciales incorrectas')
if intentos==1 and correo!=CORREO or password!=PASSWORD:
    print('intentos agotados, no puede ingresar')
