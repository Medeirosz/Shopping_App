function toggleCarrinhoDropdown(event) {
    event.stopPropagation();
    const carrinho = document.getElementById("form-carrinho");
    if (carrinho) {
      carrinho.classList.toggle("hidden");
    }
  }