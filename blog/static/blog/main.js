var btn = document.getElementById("accordion");

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

