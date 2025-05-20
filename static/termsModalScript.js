document.addEventListener("DOMContentLoaded", () => {
    const openBtn  = document.getElementById("open-terms-btn");
    const closeBtn = document.getElementById("close-terms-btn");
    const modal    = document.getElementById("terms-modal");
  
    openBtn.addEventListener("click", e => {
      e.stopPropagation();
      modal.classList.remove("hidden");
    });
  
    closeBtn.addEventListener("click", () => {
      modal.classList.add("hidden");
    });
  
    // fechar ao clicar fora da caixa branca
    modal.addEventListener("click", e => {
      if (e.target === modal) {
        modal.classList.add("hidden");
      }
    });
  });
  