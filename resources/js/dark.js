document.addEventListener("DOMContentLoaded",() => { 
  if (sessionStorage.getItem("dark-mode") == "dark") {
    makeDark();
  }
  else {
    makeLight();
  }
});