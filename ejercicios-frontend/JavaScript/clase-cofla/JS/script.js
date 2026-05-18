import {validacion} from "./funciones.js";

//Declaracion de arrays y variables
let estudiantes = Number(prompt('ingresa cuantos estudiantes hay'))
let listNombres = []
let numAsistencias = []
let numInasistencias = []
let asistencias

//Si solo es un estudiante o mas
if (estudiantes >= 1){
    listNombres = [prompt(`ingresa el nombre del estudiante 1`)]
    numAsistencias.push(0)
    numInasistencias.push(0)
}

//Ciclo de iniciacion de valores en los arrays
for (let nombres = 2; nombres <= estudiantes; nombres++){
    listNombres.push(prompt(`ingresa el nombre del estudiante ${nombres}`))
    numAsistencias.push(0)
    numInasistencias.push(0)
}

//Contador y validacion de asitencias e inasistencias
for (let days = 1; days <= 30; days++){
    for (let i = 0; i < estudiantes; i++){
        asistencias = prompt(`${listNombres[i]} vino el dia ${days}?[S] o [N]`).toLowerCase()
        validacion(asistencias)
        if (asistencias == "s"){
            numAsistencias[i] = numAsistencias[i]+1
        }
        else{
            numInasistencias[i] = numInasistencias[i]+1
        }
    }
}

/*SALIDAS:
*si tiene el 10% de inasistencias queda reprobado*/
for (let contador = 0; contador < estudiantes; contador++){
    if (numInasistencias[contador] >= 30 * 0.10){
        alert(`${listNombres[contador]} tuvo
        ${numAsistencias[contador]} Asistencias
        ${numInasistencias[contador]} Inasistencias
        y quedo reprobado`)
    }
    else{
        alert(`${listNombres[contador]} tuvo
        ${numAsistencias[contador]} Asistencias
        ${numInasistencias[contador]} Inasistencias
        y fue aprobado`)
    }
}