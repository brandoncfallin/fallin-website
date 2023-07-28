// Toggles dark mode on click 
function darkModeToggle() {
  if (localStorage.getItem("dark-mode") == "dark") {
    document.body.classList.add("animated");
    document.body.classList.remove("dark");
    document.getElementById("nav-menu").classList.remove ("dark");
    localStorage.setItem("dark-mode", "light");
    
    document.getElementById("dark-mode-toggle").src = "data/icons/moon.svg";
    document.getElementById("dark-mode-toggle-mobile").src = "data/icons/moon.svg";
    document.getElementById("nav-icon").src = "data/icons/menu-blk.svg";
  }
  else {
    document.body.classList.add("animated");
    document.body.classList.add("dark");
    document.getElementById("nav-menu").classList.add("dark");
    localStorage.setItem("dark-mode", "dark");
    
    document.getElementById("dark-mode-toggle").src = "data/icons/sun.svg";
    document.getElementById("dark-mode-toggle-mobile").src = "data/icons/sun.svg";
    document.getElementById("nav-icon").src = "data/icons/menu-wht.svg";
  }
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
  document.getElementById("nav-icon").src = "data/icons/menu-wht.svg";
          
  document.body.classList.remove("animated");
  document.body.classList.add("dark");
  document.getElementById("nav-menu").classList.add("dark");
  
  document.getElementById("dark-mode-toggle").src = "data/icons/sun.svg";
  document.getElementById("dark-mode-toggle-mobile").src = "data/icons/sun.svg";
}


// Checks local storage for dark mode preference
var darkMode;
if (localStorage.getItem("dark-mode")) {
  darkMode = localStorage.getItem("dark-mode");
} 
else {
  darkMode = "light";
}

localStorage.setItem("dark-mode", darkMode);

if (localStorage.getItem("dark-mode") == "dark") {
  document.getElementById("nav-icon").src = "data/icons/menu-wht.svg";
  
  document.body.classList.remove("animated");
  document.body.classList.add("dark");
  document.getElementById("nav-menu").classList.add("dark");
  
  document.getElementById("dark-mode-toggle").src = "data/icons/sun.svg";
  document.getElementById("dark-mode-toggle-mobile").src = "data/icons/sun.svg";
}
if (localStorage.getItem("dark-mode") == "light") {
  document.body.classList.remove("animated");
  document.body.classList.remove("dark");
  document.getElementById("nav-menu").classList.remove("dark");
  
  document.getElementById("dark-mode-toggle").src = "data/icons/moon.svg";
  document.getElementById("dark-mode-toggle-mobile").src = "data/icons/moon.svg";
  document.getElementById("nav-icon").src = "data/icons/menu-blk.svg";
}

// Open the Modal
function openModal() {
  document.getElementById("myModal").style.display = "flex";
  document.body.style.overflow = "hidden";
}

// Close the Modal
function closeModal() {
  document.getElementById("myModal").style.display = "none";
  document.body.style.overflow = "auto";
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