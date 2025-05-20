function abrirModalEdicao(id, nome, preco) {
    document.getElementById("modal-edicao").classList.remove("hidden");
    document.getElementById("edit-produto-id").value = id;
    document.getElementById("edit-nome").value = nome;
    document.getElementById("edit-preco").value = preco;
    document.getElementById("form-edicao").action = `/produtos/${id}/editar`;
  }
  
  function fecharModalEdicao() {
    document.getElementById("modal-edicao").classList.add("hidden");
  }
  