//Funciones importadas:
import {desicion,validacion,horaIngreso,acompañantes,nombre} from "./funciones.js";
//acompañantes del usuario y validacion de datos (no puede tener mas de 5 acompañantes):
let numPersonas = prompt(`¿Con cuantos acompañantes deseas entrar?
(si no tiene acompañantes indique "0")`)
acompañantes(numPersonas)
let i = 0
let entradaGratis 
bucleIngreso:
for (i; i <= numPersonas; i++){
    if (i == 0){
        let nombre1 = prompt('ingresa tu nombre')
        nombre1 = nombre(nombre1,"ingrese su nombre nuevamente")
        let edad1 = prompt('ingresa tu edad')
        edad1 = validacion(edad1,'ingrese su edad nuevamente')
        if (edad1 < 18){
            alert('no puedes ingresar, eres menor de edad')
            let desciAcompa = prompt(`¿tus acompañantes aun quieren entrar?(si no tiene acompañantes, indique "2")
                [1] = Si
                [2] = No`)
            if (desciAcompa != 1 && desciAcompa != 2){
                desciAcompa = desicion(desciAcompa,`¿tus acompañantes aun quieren entrar?(si no tiene acompañantes, indique "2")
                [1] = Si
                [2] = No`)
            }
            else if (desciAcompa == 2){
                break bucleIngreso
            }
            else{
                alert('tus acompañantes no pueden ingresar si tu no entras')
                break bucleIngreso
            }
        }
        else{
            let horario1 = prompt(`¿ingresaras en la noche o en la madrugada?
                [1] = noche
                [2] = madrugada`)
            desicion(horario1,`¿ingresaras en la noche o en la madrugada?
                [1] = noche
                [2] = madrugada`)
            if (horario1 == 2){
                let horaIngreso1 = prompt(`ingresa hora de ingreso en la madrugada
                [1] = 1:00
                [2] = 2:00
                [3] = 3:00
                [4] = 4:00 `)
                horaIngreso1 = horaIngreso(horaIngreso1,`ingresa hora de ingreso en la madrugada
                [1] = 1:00
                [2] = 2:00
                [3] = 3:00
                [4] = 4:00 `)
                if (horaIngreso1 < 3){
                    alert(`tu entrada es gratis ya que fuiste el primer usuario en entrar antes de las 3`)
                    entradaGratis = nombre1
                }
            }
            alert(`bienvenido a la discoteca ${nombre1}`)
        }
    }
    else{
        let nombreA = prompt(`ingrese el nombre del ${i} acompañante`)
        nombreA = nombre(nombreA,"ingrese el nombre nuevamente")
        let edad = prompt(`ingrese la edad de ${nombreA}`)
        edad = validacion(edad,"ingrese la edad nuevamente")
        if (edad < 18){
            alert(`${nombreA} es menor de edad, no puede ingresar`)
            let desciU = prompt(`¿Aun quieren entrar?
                [1] = Si
                [2] = No`)
            if (desciU != 1 && desciU != 2){
                desciU = desicion(desciU,`¿Aun quieren entrar?
                [1] = Si
                [2] = No`)
                if (desciU == 2){
                    break bucleIngreso
                }
            }
        }
        else{
            let horarioA = prompt(`${nombreA} ingresará en la noche o en la madrugada?
                [1] = noche
                [2] = madrugada`)
            desicion(horarioA,`¿${nombreA} en la noche o en la madrugada?
                [1] = noche
                [2] = madrugada`)
            if (horarioA == 2){
                let horaIngresoA = prompt(`ingresa hora de ingreso en la madrugada
                [1] = 1:00
                [2] = 2:00
                [3] = 3:00
                [4] = 4:00 `)
                horaIngresoA = horaIngreso(horaIngresoA,`ingresa hora de ingreso en la madrugada
                [1] = 1:00
                [2] = 2:00
                [3] = 3:00
                [4] = 4:00 `)
                if (horaIngresoA < 3 && entradaGratis == undefined){
                    alert(`${nombreA} entra gratis ya que fue el primer usuario en entrar antes de las 3`)
                    entradaGratis = nombreA
                }
            }
            alert(`bienvenid@ a la discoteca ${nombreA}`)
        }
    }
}