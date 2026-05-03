/*definicion de las variables de los helados */
const paloHelAgua = 0.6
const paloHelCrema = 1
const bombonHeladix = 1.6
const bombonHeladovich = 1.7
const bombonHelardo = 1.8
const poteHelConfites = 2.9
const poteUnCuarto = 2.9
/*funcion que dice al usuario cual es el helado mas caro para el que le alcanza segun su presupuesto */
function helados(plataUsuario){
    if (plataUsuario >= paloHelAgua && plataUsuario < paloHelCrema){
        return(alert(`le alcanza para el helado de agua y le sobran ${plataUsuario - 0.6}`))}
    else if (plataUsuario >= paloHelCrema && plataUsuario < bombonHeladix){
        return(alert(`le alcanza para el helado de crema y le sobran ${plataUsuario - 1}`))}
    else if (plataUsuario >= bombonHeladix && plataUsuario < bombonHeladovich){
        return(alert(`le alcanza para el bombon heladix y le sobran ${plataUsuario - 1.6}`))}
    else if (plataUsuario >= bombonHeladovich && plataUsuario < bombonHelardo){
        return(alert(`le alcanza para el heladovich y le sobran ${plataUsuario - 1.7}`))}
    else if (plataUsuario >= bombonHelardo && plataUsuario < poteHelConfites){
        return(alert(`le alcanza para el helardo y le sobran ${plataUsuario - 1.8}`))}
    else if (plataUsuario>=poteHelConfites){
        return(alert(`le alcanza para el pote de helado de confites o el otro y le sobran ${plataUsuario - 2.9}`))}
    else{
        return(alert('no le alcanza para ningun helado'))
    }
}
/*variables de los nombres de los clientes */
let nombre1 = prompt('ingrese el nombre del primer usuario')
let nombre2 = prompt('ingrese el nombre del segundo usuario')
let nombre3 = prompt('ingrese el nombre del tercer usuario')
/* ingresos de cada pelao */
let dinero1 = parseFloat(prompt(`de cuanto es el dinero disponible de ${nombre1}`))
plataUsuario1 = helados(dinero1) 
let dinero2 = parseFloat(prompt(`de cuanto es el dinero disponible de ${nombre2}`))
plataUsuario2 = helados(dinero2)
let dinero3 = parseFloat(prompt(`de cuanto es el dinero disponible de ${nombre3}`))
plataUsuario3 = helados(dinero3)