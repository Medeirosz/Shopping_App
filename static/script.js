// // Fundo animado com Vanta.js
VANTA.NET({
  el: "#vanta-bg",
  mouseControls: false,
  touchControls: false,
  gyroControls: false,
  minHeight: 200.0,
  minWidth: 200.0,
  scale: 1.0,
  scaleMobile: 1.0,
  color: 0xaaaaaa,
  backgroundColor: 0x0a0a0a,
  points: 8.0,
  maxDistance: 1.0,
  spacing: 20.0
});

// Ativa o toggle do formulário
window.addEventListener("DOMContentLoaded", () => {
  const toggleBtn = document.querySelector("button[data-toggle='form-produto']");
  const form = document.getElementById("form-produto");

  if (toggleBtn && form) {
    toggleBtn.addEventListener("click", () => {
      form.classList.toggle("hidden");
    });
  }
});

function toggleDropdown() {
  const dropdown = document.getElementById("dropdown");
  dropdown.classList.toggle("hidden");
}

// fecha dropdown se clicar fora
window.addEventListener("click", function(e) {
  const dropdown = document.getElementById("dropdown");
  if (!e.target.closest(".relative")) {
    dropdown.classList.add("hidden");
  }
});
