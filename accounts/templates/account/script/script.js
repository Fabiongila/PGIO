const hour = () =>{
            const date = new Date();
            let hora = date.getHours()
            let minuto = date.getMinutes()
            let segundo = date.getSeconds()
            document.getElementById("hour").innerHTML=`${hora}:${minuto}:${segundo}`
        }
        setInterval(hour,1000)

//IMAGENS
var i = 0;

let imagens = [
    '/static/ui/1.png',
    '/static/img-index/4.jpg',
    '/static/img-index/2.jpg',
    '/static/img-index/10.jpg'
]

function mostrarFirstImg(){
    let exibirFoto = document.getElementById("foto").src = imagens[i];
}
mostrarFirstImg()

function next(){
    if(i >= 3){
        i = i - 1
    }
    i = i + 1
    let exibirFoto = document.getElementById("foto").src = imagens[i];
}

function anterior(){
    if(i <= 0){
        i = i + 1
    }
    i = i - 1
    let exibirFoto = document.getElementById("foto").src = imagens[i];
}

function change(){
    if(i >= 3){
        i = -1
    }
    i = i + 1
    let exibirFoto = document.getElementById("foto").src = imagens[i];
}
setInterval(change,7000)

/*FUNÇÃO FAZER APARECER LINKS DEPARTAMENTOS||MEMBRO*/
function botaodep(){
    document.getElementById("hidden").classList.remove("hidden")
}



