document.addEventListener("DOMContentLoaded", () => {
    const modalConfig = [
      { btn: "open-contact-btn",  modal: "contact-modal", close: "close-contact-btn" },
      { btn: "open-terms-btn",    modal: "terms-modal",   close: "close-terms-btn"   },
      { btn: "open-privacy-btn",  modal: "privacy-modal",  close: "close-privacy-btn" }
    ];
  
    modalConfig.forEach(({btn, modal, close}) => {
      const openEl  = document.getElementById(btn);
      const modalEl = document.getElementById(modal);
      const closeEl = document.getElementById(close);
      if (!openEl || !modalEl || !closeEl) return;
  
      openEl.addEventListener("click", e => {
        e.stopPropagation();
        modalEl.classList.remove("hidden");
      });
      closeEl.addEventListener("click", () => modalEl.classList.add("hidden"));
      modalEl.addEventListener("click", e => {
        if (e.target === modalEl) modalEl.classList.add("hidden");
      });
    });
  });
  