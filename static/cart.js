// cart.js
document.addEventListener("DOMContentLoaded", () => {
    document.addEventListener("submit", async e => {
      const form = e.target;
      const action = form.getAttribute("action");
  
      // adicionar ao carrinho
      if (action === "/carrinho/adicionar") {
        e.preventDefault();
        await fetch(action, {
          method: "POST",
          body: new FormData(form),
        });
        return atualizarCarrinho();
      }
  
      // remover item
      if (action && action.startsWith("/carrinho/remover")) {
        e.preventDefault();
        await fetch(action, { method: "POST" });
        return atualizarCarrinho();
      }
  
      // esvaziar carrinho
      if (action === "/carrinho/limpar") {
        e.preventDefault();
        await fetch(action, { method: "POST" });
        return atualizarCarrinho();
      }
    });
  });
  
  // recarrega somente o HTML interno do dropdown do carrinho
  async function atualizarCarrinho() {
    const resp = await fetch("/carrinho/partial");
    const html = await resp.text();
    document.getElementById("carrinho-dropdown").innerHTML = html;
  }
  