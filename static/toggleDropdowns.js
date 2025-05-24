// static/js/toggleDropdowns.js
document.addEventListener("DOMContentLoaded", () => {
  const dropdowns = [
    { btnId: "profile-button", menuId: "profile-dropdown" },
    { btnId: "product-button", menuId: "product-dropdown" },
    { btnId: "carrinho-button", menuId: "carrinho-dropdown" },
  ];

  dropdowns.forEach(({ btnId, menuId }) => {
    const btn  = document.getElementById(btnId);
    const menu = document.getElementById(menuId);
    if (!btn || !menu) return;
    btn.addEventListener("click", e => {
      e.stopPropagation();
      menu.classList.toggle("hidden");
    });
  });

  // Fecha tudo ao clicar fora
  document.addEventListener("click", e => {
    if (!e.target.closest(".dropdown-container")) {
      dropdowns.forEach(({ menuId }) => {
        const m = document.getElementById(menuId);
        if (m && !m.classList.contains("hidden")) {
          m.classList.add("hidden");
        }
      });
    }
  });
});
