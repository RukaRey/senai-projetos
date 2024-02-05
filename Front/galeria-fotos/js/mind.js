let images = ["img/awesome-pink-aesthetic-kirby.jpg","img/hd-adorable-kirby.jpg","img/hd-angry-kirby-artwork.jpg","img/polygon-pink-aesthetic-kirby.jpg"]
let cur_img = 0

window.onload = function() {first();};

function first(){
    cur_img = 0
    document.getElementById("main-image").src = images[0];
}

function last(){
    cur_img = images.length - 1
    document.getElementById("main-image").src = images[images.length - 1];
}

function anterior(){
    if (cur_img > 0){cur_img -= 1}
    document.getElementById("main-image").src = images[cur_img];
}

function next(){
    if (cur_img < images.length -1){cur_img += 1}
    document.getElementById("main-image").src = images[cur_img];
}