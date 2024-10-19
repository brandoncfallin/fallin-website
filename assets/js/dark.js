// Check local storage for dark mode immediately
if (sessionStorage.getItem("dark-mode") == "dark") {
  makeDark();
} else {
  makeLight();
}

// Wait for DOM to be fully loaded before removing 'hidden' class
document.addEventListener("DOMContentLoaded", () => {
  document.documentElement.classList.remove("hidden");
});