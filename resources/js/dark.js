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