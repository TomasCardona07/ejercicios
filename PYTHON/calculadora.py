print("esto es una calculadora booleana donde decides los pasos respondiendo(verdadero o falso)")
print("ingrese el primer numero para realizar la operacion")
num1=int(input())
print("ingrese el primer segundo para realizar la operacion")
num2=int(input())
resultadoSuma=num1+num2
print("desea hacer una suma?, responda (si o no)")
respuestaSuma=(input()).lower().strip()
hacerSuma=respuestaSuma in["si","sí","s"]
if hacerSuma:
    print("el resultado de la suma es :", resultadoSuma)
else:
    print("desea hacer una resta?")
    resultadoResta=num1-num2
    respuestaResta=input().lower().strip()
    hacerResta=respuestaResta in["sí","si","s"]
    if hacerResta:
        print("el resultado de la resta es: ", resultadoResta)
    else:
        print("desea hacer una multipliacion?")
        respuestaMultiplicacion=input().lower().strip()
        hacerMultiplicacion=respuestaMultiplicacion in["sí","si","s"]
        resultadoMultiplicacion=num1*num2
        if hacerMultiplicacion:
            print("el resultado de la multiplicacion es:", resultadoMultiplicacion)
        else:
            print("le toco hacer la division mijo porque no quizo elegir ninguna de las anteriores")
            resultadoDivision=num1/num2
            print("el resultado de la division es", resultadoDivision)

