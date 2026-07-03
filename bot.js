const fetch = require("node-fetch");

const TOKEN = process.env.TOKEN;

// canais
const canais = [
  "@robinairdraktutoriais",
  "@canal2"
];

// produtos
const produtos = [
  "https://s.shopee.com.br/6ffHxillyX"
];

function montarMensagem(link) {
  return `🔥 OFERTA RELÂMPAGO 🔥

🛒 Produto na Shopee

🔗 ${link}

⚠️ Corre antes que acabe!`;
}

async function enviar(mensagem) {
  for (let canal of canais) {
    await fetch(`https://api.telegram.org/bot${TOKEN}/sendMessage`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        chat_id: canal,
        text: mensagem
      })
    });

    console.log("Enviado para", canal);
  }
}

async function rodar() {
  for (let link of produtos) {
    const msg = montarMensagem(link);
    await enviar(msg);
  }
}

rodar();