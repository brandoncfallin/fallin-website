// Wait for DOM to be fully loaded before removing 'hidden' class
document.addEventListener("DOMContentLoaded", () => {
  // Check local storage for dark mode immediately
  if (sessionStorage.getItem("dark-mode") == "dark") {
    makeDark();
  } else {
    makeLight();
  }
  document.documentElement.classList.remove("hidden");
});