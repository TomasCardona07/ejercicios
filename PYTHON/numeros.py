#programa que guarda 3 numeros, y dice cual es menor, mayor o si son iguales
print('ingresa el primer numero')
num1=float(input())
if num1<0:
    print('numero no valido')
else:
    print('ingresa el segundo numero')
num2=float(input())
if num2<0:
    print('numero no valido')
else:
    print('ingresa el tercer numero')
num3=float(input())
if num3<0:
    print('numero no valido')
else:
    if num1>num2 and num2>num3:
        print('el numero mas grande es: ',num1)
        print('el numero mas pequeño es :',num3)
    elif num1>num3 and num3>num2:
        print('el numero mas grande es: ',num1)
        print('el numero mas pequeño es :',num2)
    elif num2>num1 and num1>num3:
        print('el numero mas grande es: ',num2)
        print('el numero mas pequeño es :',num3)
    elif num2>num3 and num3>num1:
        print('el numero mas grande es: ',num2)
        print('el numero mas pequeño es :',num1)
    elif num3>num2 and num2>num1:
        print('el numero mas grande es: ',num3)
        print('el numero mas pequeño es :',num1)
    elif num3>num1 and num1>num2:
        print('el numero mas grande es: ',num3)
        print('el numero mas pequeño es :',num2)
    else:
        print('los numeros son iguales')