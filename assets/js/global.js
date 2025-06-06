// Get user dark mode preference, make sure dark mode has not been toggled by user
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches && localStorage.getItem("delta") == null) {
  localStorage.setItem("dark-mode", "dark");
  makeDark();
}

// Toggles dark mode on click 
function darkModeToggle() {
  if (localStorage.getItem("dark-mode") == "dark") {
    document.body.classList.add("animated");
    makeLight();
    document.body.classList.remove("animated");
    localStorage.setItem("dark-mode", "light");
    localStorage.setItem("delta", "true")
  }
  else {
    document.body.classList.add("animated");
    makeDark();
    document.body.classList.remove("animated");
    localStorage.setItem("dark-mode", "dark");
    localStorage.setItem("delta", "true")
  }
} 

// Toggles dark mode
function makeDark() {
  document.getElementById("nav-icon").src = "/assets/images/icons/menu-wht.svg";
  document.documentElement.classList.add("dark");
  document.querySelectorAll("dialog").forEach(item => {
    item.classList.add("dark");
  })
  document.getElementById("nav-menu").classList.add("dark");
  
  document.getElementById("dark-mode-toggle").src = "/assets/images/icons/sun.svg";
  document.getElementById("dark-mode-toggle-mobile").src = "/assets/images/icons/sun.svg";
}

// Toggles light mode
function makeLight() {
  document.documentElement.classList.remove("dark");
  document.getElementById("nav-menu").classList.remove("dark");
  document.querySelectorAll("dialog").forEach(item => {
    item.classList.remove("dark");
  })
  document.getElementById("dark-mode-toggle").src = "/assets/images/icons/moon.svg";
  document.getElementById("dark-mode-toggle-mobile").src = "/assets/images/icons/moon.svg";
  document.getElementById("nav-icon").src = "/assets/images/icons/menu-blk.svg";
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

// Modern Chrome requires { passive: false } when adding event
var supportsPassive = false;
try {
  window.addEventListener("test", null, Object.defineProperty({}, 'passive', {
    get: function () { supportsPassive = true; } 
  }));
} catch(e) {}

var wheelOpt = supportsPassive ? { passive: false } : false;
var wheelEvent = 'onwheel' in document.createElement('div') ? 'wheel' : 'mousewheel';

// Disable scroll 
function disableScroll() {
  window.addEventListener('DOMMouseScroll', preventDefault, false); // older FF
  window.addEventListener(wheelEvent, preventDefault, wheelOpt); // modern desktop
  window.addEventListener('touchmove', preventDefault, wheelOpt); // mobile
  window.addEventListener('keydown', preventDefaultForScrollKeys, false);
}

// Enable scroll
function enableScroll() {
  window.removeEventListener('DOMMouseScroll', preventDefault, false);
  window.removeEventListener(wheelEvent, preventDefault, wheelOpt); 
  window.removeEventListener('touchmove', preventDefault, wheelOpt);
  window.removeEventListener('keydown', preventDefaultForScrollKeys, false);
}