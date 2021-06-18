var sidenav = document.getElementById("sideNav");
var main = document.getElementById("main");
var menu = document.getElementById('menuBtn');
var footer = document.getElementById('footer');
var bg = document.getElementById("bg");

function openNav() {
    sidenav.style.width = "250px"
    main.style.transform = "translateX(-250px)"
    bg.style.transform = "translateX(-250px)"
    main.style.transition = "transform 1s"
    bg.style.transition = "transform 1s"
    footer.style.transform = "translateX(-250px)"
    footer.style.transition = "transform 1s"
    menu.onclick = function () {
        closeNav();
    };

    menu.className = "far fa-times-circle"
}

function closeNav() {
    sidenav.style.width = "0"
    main.style.transform = "translateX(0)"
    main.style.transition = "transform 0.3s"
    bg.style.transform = "translateX(0)"
    bg.style.transition = "transform 0.3s"
    footer.style.transform = "translateX(0)"
    footer.style.transition = "transform 0.3s"
    menu.onclick = function () {
        openNav();
    }
    menu.className = "fas fa-bars"
}

var scroll = new SmoothScroll('a[href*="#"]', {
    speed: 500,
    speedAsDuration: true
});

var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("top-navbar").style.top = "0";
    } else {
        document.getElementById("top-navbar").style.top = "-80px";
    }
    prevScrollpos = currentScrollPos;
}

//Dark mode
function toggleDarkLight() {
    var body = document.getElementById("body");
    var currentClass = body.className;
    body.className = currentClass == "dark-mode" ? "light-mode" : "dark-mode";
}

var tilt = $('.js-tilt').tilt();
