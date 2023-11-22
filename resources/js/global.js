// Toggles dark mode on click 
function darkModeToggle() {
  if (sessionStorage.getItem("dark-mode") == "dark") {
    makeLight();
    sessionStorage.setItem("dark-mode", "light");
  }
  else {
    makeDark();
    sessionStorage.setItem("dark-mode", "dark");
  }
} 

function makeDark() {
  document.getElementById("nav-icon").src = "data/icons/menu-wht.svg";
  
  document.body.classList.remove("animated");
  document.body.classList.add("dark");
  document.getElementById("nav-menu").classList.add("dark");
  
  document.getElementById("dark-mode-toggle").src = "data/icons/sun.svg";
  document.getElementById("dark-mode-toggle-mobile").src = "data/icons/sun.svg";
}

function makeLight() {
  document.body.classList.remove("animated");
  document.body.classList.remove("dark");
  document.getElementById("nav-menu").classList.remove("dark");

  document.getElementById("dark-mode-toggle").src = "data/icons/moon.svg";
  document.getElementById("dark-mode-toggle-mobile").src = "data/icons/moon.svg";
  document.getElementById("nav-icon").src = "data/icons/menu-blk.svg";
}

// Toggles mobile menu on click
function mobileDrop() {
  document.getElementById("nav-menu").classList.toggle("show");
}

// Closes mobile menu when clicking outside of it
window.onclick = function(event) {
  if (!event.target.matches('.nav-button')) {
    var dropdowns = document.getElementsByClassName("drop-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
} 

// Checks user theme preference
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
  makeDark();
}

// Open the Modal
function openModal() {
  document.getElementById("myModal").style.display = "flex";
  disableScroll();
}

// Close the Modal
function closeModal() {
  document.getElementById("myModal").style.display = "none";
  enableScroll();
}

document.onkeydown = function(evt) {
  evt = evt || window.event;
  if (evt.keyCode == 27 && document.getElementById("myModal").style.display == "flex") {
      closeModal();
  }
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "flex";
}

// No scroll
function preventDefault(e) {
  e.preventDefault();
}

function preventDefaultForScrollKeys(e) {
  if (keys[e.keyCode]) {
    preventDefault(e);
    return false;
  }
}

// modern Chrome requires { passive: false } when adding event
var supportsPassive = false;
try {
  window.addEventListener("test", null, Object.defineProperty({}, 'passive', {
    get: function () { supportsPassive = true; } 
  }));
} catch(e) {}

var wheelOpt = supportsPassive ? { passive: false } : false;
var wheelEvent = 'onwheel' in document.createElement('div') ? 'wheel' : 'mousewheel';

// call this to Disable
function disableScroll() {
  window.addEventListener('DOMMouseScroll', preventDefault, false); // older FF
  window.addEventListener(wheelEvent, preventDefault, wheelOpt); // modern desktop
  window.addEventListener('touchmove', preventDefault, wheelOpt); // mobile
  window.addEventListener('keydown', preventDefaultForScrollKeys, false);
}

// call this to Enable
function enableScroll() {
  window.removeEventListener('DOMMouseScroll', preventDefault, false);
  window.removeEventListener(wheelEvent, preventDefault, wheelOpt); 
  window.removeEventListener('touchmove', preventDefault, wheelOpt);
  window.removeEventListener('keydown', preventDefaultForScrollKeys, false);
}