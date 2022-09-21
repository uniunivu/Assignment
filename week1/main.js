// 點漢堡選單即顯示，點選其他地方即關閉

var hamburger_menu = document.getElementsByClassName("item")[4];
// console.log(hamburger_menu);
var hamburger_nav = document.getElementById("hamburger_nav");

hamburger_menu.addEventListener("click", show);
// console.log(hamburger_nav);

function show() {
    // console.log(1);
    hamburger_nav.style.display = "block";
}

document.addEventListener("click", hide);
// console.log(document);

function hide(e) {
    // console.log("hide");
    let clickArea = e.target;
    let nav = document.querySelector(".hamburger_menu");
    // console.log(e);
    if(nav == clickArea || nav.contains(clickArea)) {
        hamburger_nav.style.display = "block";
        console.log("wow");
    } else {    
        hamburger_nav.style.display = "none";
    }
}