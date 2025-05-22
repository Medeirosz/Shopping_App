document.addEventListener("DOMContentLoaded", () => {
    const openBtn  = document.getElementById("open-privacy-btn");
    const closeBtn = document.getElementById("close-privacy-btn");
    const modal    = document.getElementById("privacy-modal");
  
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
  