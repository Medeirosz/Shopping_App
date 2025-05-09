document.addEventListener('DOMContentLoaded', () => {
    const botao = document.getElementById('btn-chamar-api');
    const respostaEl = document.getElementById('resposta');
  
    botao.addEventListener('click', async () => {
      try {
        const res = await fetch('http://localhost:8000/');
        if (!res.ok) throw new Error(`Status ${res.status}`);
        const data = await res.json();
        respostaEl.innerText = data.mensagem;
      } catch (err) {
        console.error('Erro ao chamar API:', err);
        respostaEl.innerText = 'Erro: ' + err.message;
      }
    });
  });
  