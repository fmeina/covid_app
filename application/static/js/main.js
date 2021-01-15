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

function loadXMLDoc()
    {
        var req = new XMLHttpRequest()
        req.onreadystatechange = function()
        {
            if (req.readyState == 4)
            {
                if (req.status != 200)
                {
                    //error handling code here
                }
                else
                {
                    var response = JSON.parse(req.responseText)
                    document.getElementById('myDiv').innerHTML = response.username
                }
            }
        }

        req.open('POST', '/ajax')
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
        var age = document.getElementById('age').value
        var swh = document.getElementById('swh')
        var swhChecked = swh.checked
        var gov = document.getElementById('gov')
        var govChecked = gov.checked
        var sick = document.getElementById('sick')
        var sickChecked = sick.checked
        var group = 0
        if (age > 60) {
            group = 1
        } else {
            if (swhChecked == 1) {
                group = 1
            } else if (govChecked == 1) {
                group = 1
            } else if (sickChecked == 1) {
                group = 2
            } else {
                group = 3
            }
        }

        var postVars = 'username='+group
        req.send(postVars)

        return false
    }