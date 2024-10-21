// Wait for DOM to be fully loaded before removing 'hidden' class
document.addEventListener("DOMContentLoaded", () => {
  // Check local storage for dark mode immediately
  if (localStorage.getItem("dark-mode") == "dark") {
    makeDark();
  } else {
    makeLight();
  }
  document.documentElement.style.visibility = "visible";
  document.documentElement.style.opacity = "1";
});