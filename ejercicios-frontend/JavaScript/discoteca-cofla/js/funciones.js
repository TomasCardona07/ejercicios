//funcion para cuando se requiera resultado 1 O 2
export function desicion(desicion,mensaje){
    while (desicion === null || desicion.trim() === "" || isNaN(desicion) || Number(desicion <= 0) || Number(desicion > 2)){
        if (desicion === null){
        alert('ingresa un numero por favor')
        }
        else if (desicion.trim() === ""){
        alert('no puede dejar vacio, ingresa un numero porfavor')
        }
        else if (isNaN(desicion)){
        alert('no puedes ingresar caracteres, ingresa un numero porfavor')
        }
        else if (desicion >2 || desicion == 0){
            alert('numero incorrecto')
        }
        else{
        alert('el numero no puede ser negativo')
        }
        desicion = prompt(mensaje)
        }
    return Number(desicion)
}
//funcion para cuando se requiera un numero positivo
export function validacion(edad,mensaje){
    while (edad === null || edad.trim() === "" || isNaN(edad) || Number(edad <= 0 )){
        if (edad === null){
            alert('ingresa un numero por favor')
        }
        else if (edad.trim() === ""){
            alert('no puede dejar vacio, ingresa un numero porfavor')
        }
        else if (isNaN(edad)){
            alert('no puedes ingresar caracteres, ingresa un numero porfavor')
        }
        else if (edad == 0){
            alert('numero incorrecto')
        }
        else{
            alert('el numero no puede ser negativo')
        }
        edad = prompt(mensaje)
    }
    return Number(edad)
}
//Funcion para la hora de ingreso de los usuarios
export function horaIngreso (horaIngreso,mensaje){
    while (horaIngreso === null || horaIngreso.trim() === "" || isNaN(horaIngreso) || Number(horaIngreso <= 0) || Number(horaIngreso > 4)){
        if (horaIngreso === null){
            alert('ingresa un numero por favor')
        }
        else if (horaIngreso.trim() === ""){
            alert('no puede dejar vacio, ingresa un numero porfavor')
        }
        else if (isNaN(horaIngreso)){
            alert('no puedes ingresar caracteres, ingresa un numero porfavor')
        }
        else if (horaIngreso > 4 || horaIngreso == 0){
            alert('numero incorrecto')
        }
        else{
            alert('el numero no puede ser negativo')
        }
        horaIngreso = prompt(mensaje)
    }
    return Number(horaIngreso)
}
//Funcion para validar los acompañantes del usuario principal
export function acompañantes (numPersonas){
    while (numPersonas === null || numPersonas.trim() === "" || isNaN(numPersonas) || Number(numPersonas < 0) || Number (numPersonas > 5)){
        if (numPersonas === null){
            alert('ingresa un numero por favor')
        }
        else if (numPersonas.trim() === ""){
            alert('no puede dejar vacio, ingresa un numero porfavor')
        }
        else if (isNaN(numPersonas)){
            alert('no puedes ingresar caracteres, ingresa un numero porfavor')
        }
        else if (numPersonas < 0){
            alert('el numero no puede ser negativo')
        }
        else{
            alert('no puedes ingresar con mas de 5 acompañantes')
        }
        numPersonas = prompt(`¿Con cuantos acompañantes deseas entrar?
        (si no tiene acompañantes indique "0")`)
    }
    return Number(numPersonas)
}
//Funcion para validar el nombre
export function nombre(nombre,mensaje){
    while (nombre === null || nombre.trim() === ""){
        if (nombre === null){
            alert('ingrese el nombre porfavor')
        }
        else{
            alert('no puede dejar vacio')
        }
        nombre = prompt(mensaje)
    }
    return (nombre)
}