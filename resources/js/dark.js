// Check user dark mode preference
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
  localStorage.setItem("dark-mode", "dark");
}

// Checks local storage for dark mode preference
if (localStorage.getItem("dark-mode")) {
  
} 
else {
  localStorage.setItem("dark-mode", "light");
}