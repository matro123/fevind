function myFunction(x) {
    x.classList.toggle("change");
  }
function burger() {
    var x = document.getElementById("menumobilcontainer"),
        y = getComputedStyle(menumobilcontainer).display;
    if (y === "none") {
        document.getElementById("menumobilcontainer").style.display = "flex";
    }else{
        document.getElementById("menumobilcontainer").style.display = "none";
    }
    }
