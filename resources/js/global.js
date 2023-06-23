function darkModeToggle() {

    if (localStorage.getItem("dark-mode") == "dark") {
        document.body.classList.add("animated");
        document.body.classList.remove("dark");
        localStorage.setItem("dark-mode", "light");
        document.getElementById("dark-mode-toggle").innerHTML = "Dark Mode";
    }
    else {
        document.body.classList.add("animated");
        document.body.classList.add("dark");
        localStorage.setItem("dark-mode", "dark");
        document.getElementById("dark-mode-toggle").innerHTML = "Light Mode";
    }
  } 