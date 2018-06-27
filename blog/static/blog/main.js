var accordion = document.getElementsByClassName("accordion");

for (var i = 0; i < accordion.length; i++) {
    accordion[i].onclick = function () {
        this.classList.toggle('status-open');
        var content = this.nextElementSibling;
        if (content.style.maxHeight) {
            content.style.maxHeight = null;   
        }
        else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    }
}

var upButton = document.getElementById("up-button");
upButton.onclick = function () {
    window.scrollTo(0,0);
}

/*var btn = document.getElementById("accordion");

btn.addEventListener("click", function() {
    var myRequest = new XMLHttpRequest();
    myRequest.open('GET', 'static/blog/data.json');
    myRequest.onload = function() {
        var dataVar = JSON.parse(myRequest.responseText);
        console.log(dataVar[0].name)
    };
    myRequest.send();
});

function buttonFunction() {
    "use strict";
    document.getElementById('accordion').innerText = '';
}

*/
