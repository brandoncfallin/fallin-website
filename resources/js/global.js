function darkModeToggle() {
    var element = document.body;
    element.classList.toggle("dark");

    var change = document.getElementById("dark-mode-toggle");
    if (change.innerHTML === "Dark Mode") {
        change.innerHTML = "Light Mode";
    }
    else {
        change.innerHTML = "Dark Mode";
    }
  } 