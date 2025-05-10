// Fundo animado com Vanta.js
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

// document.addEventListener("DOMContentLoaded", () => {
//   const toggleButton = document.querySelector("button[data-toggle='form-produto']");
//   const formProduto = document.getElementById("form-produto");

//   if (toggleButton && formProduto) {
//     toggleButton.addEventListener("click", () => {
//       formProduto.classList.toggle("hidden");
//     });
//   } else {
//     console.warn("Botão ou formulário não encontrado para toggle.");
//   }
// });
