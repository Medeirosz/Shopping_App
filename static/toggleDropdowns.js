document.addEventListener("DOMContentLoaded", () => {
    const dropdownMap = {
      "profile-button": "profile-dropdown",
      "product-button": "product-dropdown",
      "carrinho-button": "carrinho-dropdown",
    };
  
    // Para cada par botão ↔ dropdown, atacha o listener
    Object.entries(dropdownMap).forEach(([btnId, menuId]) => {
      const btn  = document.getElementById(btnId);
      const menu = document.getElementById(menuId);
      if (!btn || !menu) return;
      btn.addEventListener("click", e => {
        e.stopPropagation();
        menu.classList.toggle("hidden");
      });
    });
  
    // fecha tudo ao clicar fora de qualquer dropdown-container
    window.addEventListener("click", e => {
      if (!e.target.closest(".dropdown-container")) {
        Object.values(dropdownMap).forEach(id => {
          const el = document.getElementById(id);
          if (el && !el.classList.contains("hidden")) {
            el.classList.add("hidden");
          }
        });
      }
    });
  });
  