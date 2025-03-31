document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("theme-toggle");
    const body = document.getElementById("theme");

    // Cargar el tema guardado en localStorage
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
        body.className = savedTheme;
    } else {
        body.className = "bg-light text-dark"; // Tema claro por defecto
    }

    // Alternar entre temas claro y oscuro
    themeToggle.addEventListener("click", function () {
        if (body.classList.contains("bg-light")) {
            body.className = "bg-dark text-light"; // Cambiar a tema oscuro
            localStorage.setItem("theme", "bg-dark text-light");
        } else {
            body.className = "bg-light text-dark"; // Cambiar a tema claro
            localStorage.setItem("theme", "bg-light text-dark");
        }
    });
});