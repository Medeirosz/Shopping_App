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

  VANTA.NET({
    el: "#vanta-bg",
    mouseControls: false,
    touchControls: false,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    scale: 1.0,
    scaleMobile: 1.0,
    color: 0xaaaaaa,            
    backgroundColor: 0x0a0a0a,  
    points: 8.0,
    maxDistance: 1.0,         
    spacing: 20.0
  })
  
  
  
  
