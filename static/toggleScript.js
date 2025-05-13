// Abre o dropdown do perfil do header
function toggleDropdown() {
    const dropdown = document.getElementById("dropdown");
    dropdown.classList.toggle("hidden");
  }

// Fecha dropdown se clicar fora
window.addEventListener("click", function(e) {
  const dropdown = document.getElementById("dropdown");
  if (!e.target.closest(".relative")) {
    dropdown.classList.add("hidden");
  }
});


// Abre o dropdown do addprodutos do header
function toggleProdutoDropdown() {
  const formDropdown = document.getElementById("form-produto");
  formDropdown.classList.toggle("hidden");
}

// Fecha dropdown se clicar fora
window.addEventListener("click", function(e) {
  const formDropdown = document.getElementById("form-produto");
  if (!e.target.closest(".relative") && !formDropdown.classList.contains("hidden")) {
    formDropdown.classList.add("hidden");
  }
});
