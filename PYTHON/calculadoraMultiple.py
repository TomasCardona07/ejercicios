print('esto es una claculadora que solo suma,resta,multiplicion y division, ademas de calcular el promedio y el porcentaje')
operacion = input('ingrese la operacion que desea realizar: ').lower().strip()
if 'suma' in operacion:
    num1 = float(input('ingrese el primer numero para realizar la suma: '))
    num2 = float(input('ingrese el segundo numero para realizar la suma: '))
    resultadoSuma= num1 + num2
    print('el resultado de la suma es: ',resultadoSuma)
if 'resta' in operacion:
    num1 = float(input('ingrese el primer numero para realizar la resta: '))
    num2 = float(input('ingrese el segundo numero para realizar la resta: '))
    resultadoResta = num1 - num2
    print('el resultado de la resta es: ',resultadoResta)
if 'multiplicacion' in operacion:
    num1 = float(input('ingrese el primer numero para realizar la multiplicacion: '))
    num2 = float(input('ingrese el segundo numero para realizar la multiplicacion: '))
    resultadoMultiplicacion = num1 * num2
    print('el resultado de la multiplicacion es: ',resultadoMultiplicacion)
if 'division' in operacion:
    num1 = float(input('ingrese el primer numero para realizar la division: '))
    num2 = float(input('ingrese el segundo numero para realizar la division: '))
    resultadoDivision = num1 / num2
    print('el resultado de la division es: ',resultadoDivision)
if 'promedio' in operacion:
    num1 = float(input('ingrese el  primer numero para calcular el promedio: '))
    num2 = float(input('ingrese el segundo numero para calcular el promedio: '))
    resultadoPromedio = (num1 + num2) / 2
    print('el resultado del promedio es: ',resultadoPromedio)
if 'porcentaje' in operacion:
    num1=float(input('ingrese el numero para calcular el porcentaje: '))
    num2=float(input('ingrese el porcentaje a calcular: '))
    resultadoPorcentaje = (num1*num2)/100
    print('el resultado del porcentaje es: ',resultadoPorcentaje)

