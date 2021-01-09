'use strict';
function userMenuDropdown() {
  document.getElementById("user-dropdown").classList.toggle("show");
}

window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) {
        let myDropdown = document.getElementById("user-dropdown");
        if (myDropdown.classList.contains('show')) {
            myDropdown.classList.remove('show');
        }
    }
}

function swapStyleSheet(sheet){
    document.getElementById('pagestyle').setAttribute('href', sheet);
    localStorage.setItem('currentStyleSheet', sheet);
}
window.onload = function() {
     document.getElementById('pagestyle').setAttribute('href', localStorage.getItem('currentStyleSheet'));
}