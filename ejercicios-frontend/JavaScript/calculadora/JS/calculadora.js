import {suma,resta,multiplicacion,division} from "./funciones.js";
let operacion = Number(prompt(`ingresa el numero correspondiente a la operacion que deseas hacer:
    [1] = suma
    [2] = resta
    [3] = multiplicacion
    [4] = division`))
while (operacion != 1 && operacion != 2 && operacion != 3 && operacion != 4 ){
    alert('numero ingresado no valido, ingresa el numero correspondiente a la operacion nuevamente')
    operacion = Number(prompt(`ingresa el numero correspondiente a la operacion que deseas hacer:
    [1] = suma
    [2] = resta
    [3] = multiplicacion
    [4] = division`))
}
if (operacion == 1){
    let num1 = Number(prompt('ingrese el primer numero para realizar la suma'))
    let num2 = Number(prompt('ingrese el segundo numero para realizar la suma'))
    let resultadoSuma = suma(num1,num2)
    alert(`el resultado de la suma es: ${resultadoSuma}`)
}
else if (operacion == 2){
    let num1 = Number(prompt('ingrese el primer numero para realizar la resta'))
    let num2 = Number(prompt('ingrese el segundo numero para realizar la resta'))
    let resultadoResta = resta(num1,num2)
    alert(`el resultado de la resta es: ${resultadoResta}`)
}
else if (operacion == 3){
    let num1 = Number(prompt('ingrese el primer numero para realizar la multiplicacion'))
    let num2 = Number(prompt('ingrese el segundo numero para realizar la multiplicacion'))
    let resultadoMultiplicacion = multiplicacion(num1,num2)
    alert(`el resultado de la multiplicacion es: ${resultadoMultiplicacion}`)
}
else{
    let num1 = Number(prompt('ingrese el primer numero para realizar la division'))
    while (num1 == 0){
        alert('no se puede dividir por 0')
        num1 = Number(prompt('ingrese el primer numero nuevamente'))
    }
    let num2 = Number(prompt('ingrese el segundo numero para realizar la division'))
    while (num2 == 0){
        alert('no se puede dividir por 0')
        num2 = Number(prompt('ingrese el segundo numero nuevamente'))
    }
    let resultadoDivision = division(num1,num2)
    alert(`el resultado de la division es: ${resultadoDivision}`)
}