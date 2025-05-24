// /static/js/cart.js
document.addEventListener("DOMContentLoaded", () => {
    // capturar todos os botões de "Adicionar ao Carrinho"
    document.querySelectorAll("form[action='/carrinho/adicionar']").forEach(form => {
      form.addEventListener("submit", async e => {
        e.preventDefault();
        const fd = new FormData(form);
        const resp = await fetch(form.action, { method: "POST", body: fd });
        const data = await resp.json();
        if (data.ok) {
          // aqui você pode chamar uma função para recarregar só o dropdown do carrinho
          atualizarCarrinho();
        } else {
          alert(data.error || "Erro ao adicionar");
        }
      });
    });
  
    // mesmos para remover item
    document.querySelectorAll("form[action^='/carrinho/remover']").forEach(form => {
      form.addEventListener("submit", async e => {
        e.preventDefault();
        const resp = await fetch(form.action, { method: "POST" });
        const data = await resp.json();
        if (data.ok) atualizarCarrinho();
        else alert(data.error || "Erro ao remover");
      });
    });
  
    // e para esvaziar
    const limparForm = document.querySelector("form[action='/carrinho/limpar']");
    if (limparForm) {
      limparForm.addEventListener("submit", async e => {
        e.preventDefault();
        const resp = await fetch(limparForm.action, { method: "POST" });
        const data = await resp.json();
        if (data.ok) atualizarCarrinho();
        else alert(data.error || "Erro ao esvaziar");
      });
    }
  });
  
  // Função que busca o HTML parcial do carrinho e injeta ele dentro do dropdown
  async function atualizarCarrinho() {
    const resp = await fetch("/carrinho/partial");     // vea etapa 4: crie esta rota
    const html = await resp.text();
    document.getElementById("carrinho-dropdown").innerHTML = html;
  }
  