let max_cap = 1000
let cur_cap = 1000
let min_cap = 100
let interval;


function iniciarTimer() {
    if (!interval) {
        interval = setInterval(baba, 1000);
    }
}

function pararTimer() {
    if (interval) {
        clearInterval(interval);
        interval = null;
    }
}

function baba(){
    console.log(cur_cap);
    if (cur_cap <= 0){
        console.log("Vazio")
    }else{
        document.getElementById("liquido").style.height -= (parseInt(document.getElementById("liquido").style.height) - 100) + "px";
        cur_cap -= 10
        console.log("Esvaziando")
    }
}


