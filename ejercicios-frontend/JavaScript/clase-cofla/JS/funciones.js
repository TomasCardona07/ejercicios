//Funcion validacion de datos
export const validacion = (asistencias) =>{
    while (asistencias != "s" && asistencias != "n"){
        alert('caracter incorrecto')
        asistencias = prompt(`ingresalo nuevamente
        [S] = SI
        [N] = NO`).toLowerCase()
    }
    return asistencias
}