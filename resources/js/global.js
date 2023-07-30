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
  disableScroll();
}

// Close the Modal
function closeModal() {
  document.getElementById("myModal").style.display = "none";
  enableScroll();
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

// left: 37, up: 38, right: 39, down: 40,
// spacebar: 32, pageup: 33, pagedown: 34, end: 35, home: 36
var keys = {37: 1, 38: 1, 39: 1, 40: 1};

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

const pinchZoom = (imageElement) => {
  let imageElementScale = 1;

  let start = {};

  // Calculate distance between two fingers
  const distance = (event) => {
    return Math.hypot(event.touches[0].pageX - event.touches[1].pageX, event.touches[0].pageY - event.touches[1].pageY);
  };

  imageElement.addEventListener('touchstart', (event) => {
    console.log('touchstart', event);
    if (event.touches.length === 2) {
      event.preventDefault(); // Prevent page scroll

      // Calculate where the fingers have started on the X and Y axis
      start.x = (event.touches[0].pageX + event.touches[1].pageX) / 2;
      start.y = (event.touches[0].pageY + event.touches[1].pageY) / 2;
      start.distance = distance(event);
    }
  });

  imageElement.addEventListener('touchmove', (event) => {
    console.log('touchmove', event);
    if (event.touches.length === 2) {
      event.preventDefault(); // Prevent page scroll
      let scale;

      // Safari provides event.scale as two fingers move on the screen
      // For other browsers just calculate the scale manually
      if (event.scale) {
        scale = event.scale;
      } else {
        const deltaDistance = distance(event);
        scale = deltaDistance / start.distance;
      }

      imageElementScale = Math.min(Math.max(1, scale), 4);

      // Calculate how much the fingers have moved on the X and Y axis
      const deltaX = (((event.touches[0].pageX + event.touches[1].pageX) / 2) - start.x) * 2; // x2 for accelarated movement
      const deltaY = (((event.touches[0].pageY + event.touches[1].pageY) / 2) - start.y) * 2; // x2 for accelarated movement

      // Transform the image to make it grow and move with fingers
      const transform = `translate3d(${deltaX}px, ${deltaY}px, 0) scale(${imageElementScale})`;
      imageElement.style.transform = transform;
      imageElement.style.WebkitTransform = transform;
      imageElement.style.zIndex = "9999";
    }
  });

  imageElement.addEventListener('touchend', (event) => {
    console.log('touchend', event);
    // Reset image to it's original format
    imageElement.style.transform = "";
    imageElement.style.WebkitTransform = "";
    imageElement.style.zIndex = "";
  });
}