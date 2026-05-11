let num1
let num2

const resultSuma = () => {
    num1 = Number(document.getElementById("num1").value)
    num2 = Number(document.getElementById("num2").value)
    suma = num1 + num2
    document.getElementById("resultado").textContent = (`el resultado de la suma es: ${suma}`)
}
const resultResta = () => {
    num1 = Number(document.getElementById("num1").value)
    num2 = Number(document.getElementById("num2").value)
    if (num1 < 0 || num2 < 0){
    }
    resta = num1 - num2
    document.getElementById("resultado").textContent = (`el resultado de la resta es: ${resta}`)
}
const resultMulti = () => {
    num1 = Number(document.getElementById("num1").value)
    num2 = Number(document.getElementById("num2").value)
    multiplicacion = num1 * num2
    document.getElementById("resultado").textContent = (`el resultado de la multiplicacion es: ${multiplicacion}`)
}
const resultDiv = () => {
    num1 = Number(document.getElementById("num1").value)
    num2 = Number(document.getElementById("num2").value)
    if (num1 == 0 && num2 == 0 || num1 == 0 && num2 > 0 || num1 > 0 && num2 == 0){
        alert('no se puede dividir por 0')
    }
    else{
        division = num1 / num2
        document.getElementById("resultado").textContent = (`el resultado de la division es: ${division}`)
    }
}