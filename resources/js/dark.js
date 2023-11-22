// Waits for page to load
document.addEventListener("DOMContentLoaded",() => { 
  // Check local storage for dark mode. Gets rid of white flash on load 
  if (sessionStorage.getItem("dark-mode") == "dark") {
    makeDark();
  }
  else {
    makeLight();
  }
});