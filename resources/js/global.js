function darkModeToggle() {

    if (localStorage.getItem("dark-mode") == "dark") {
        document.body.classList.add("animated");
        document.body.classList.remove("dark");
        document.getElementById("nav-menu").classList.remove ("dark");
        localStorage.setItem("dark-mode", "light");
        document.getElementById("dark-mode-toggle").innerHTML = "Dark Mode";
        document.getElementById("dark-mode-toggle-mobile").innerHTML = "Dark Mode";
    }
    else {
        document.body.classList.add("animated");
        document.body.classList.add("dark");
        document.getElementById("nav-menu").classList.add("dark");
        localStorage.setItem("dark-mode", "dark");
        document.getElementById("dark-mode-toggle").innerHTML = "Light Mode";
        document.getElementById("dark-mode-toggle-mobile").innerHTML = "Light Mode";
    }
  } 

function mobileDrop() {
    document.getElementById("nav-menu").classList.toggle("show");
}

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