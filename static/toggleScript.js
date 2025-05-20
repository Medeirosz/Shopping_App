// abre/fecha perfil
function toggleProfileDropdown(e) {
  e.stopPropagation();
  document.getElementById("profile-dropdown").classList.toggle("hidden");
}

// abre/fecha produto
function toggleProductDropdown(e) {
  e.stopPropagation();
  document.getElementById("product-dropdown").classList.toggle("hidden");
}

// abre/fecha carrinho
function toggleCarrinhoDropdown(e) {
  e.stopPropagation();
  document.getElementById("carrinho-dropdown").classList.toggle("hidden");
}

// fecha tudo ao clicar fora
function closeAll(e) {
  if (!e.target.closest(".dropdown-container")) {
    ["profile-dropdown","product-dropdown","carrinho-dropdown"]
      .forEach(id => {
        const el = document.getElementById(id);
        if (el && !el.classList.contains("hidden")) {
          el.classList.add("hidden");
        }
      });
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("profile-button")
          .addEventListener("click", toggleProfileDropdown);

  document.getElementById("product-button")
          .addEventListener("click", toggleProductDropdown);

  document.getElementById("carrinho-button")
          .addEventListener("click", toggleCarrinhoDropdown);

  window.addEventListener("click", closeAll);
});

document.addEventListener('DOMContentLoaded', () => {
  const btn  = document.getElementById('carrinho-button');
  const menu = document.getElementById('carrinho-dropdown');
  if (!btn || !menu) return;

  btn.addEventListener('click', e => {
  e.stopPropagation();
  menu.classList.toggle('hidden');
  });

  document.addEventListener('click', () => {
  menu.classList.add('hidden');
  });
});