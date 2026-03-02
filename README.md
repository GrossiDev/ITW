<div align="center">

```
██╗████████╗██╗    ██╗
██║╚══██╔══╝██║    ██║
██║   ██║   ██║ █╗ ██║
██║   ██║   ██║███╗██║
██║   ██║   ╚███╔███╔╝
╚═╝   ╚═╝    ╚══╝╚══╝
```

**iPhone To Windows**

*Transferência de arquivos via Wi-Fi — sem cabos, sem apps, sem complicação.*

O ITW surgiu de uma necessidade real durante meu curso técnico de TI no SENAI. Enquanto no Android a transferência de arquivos via Bluetooth para o Windows é nativa e simples, no iPhone essa praticidade não existe.

Para resolver isso, desenvolvi esse servidor local em Python que permite enviar arquivos entre dispositivos via Wi-Fi em poucos segundos, sem precisar de cabos ou softwares de terceiros pesados.

</div>

---

## 🎯 Sobre o Projeto

Durante o curso técnico em TI no **SENAI**, surgiu um problema recorrente: transferir arquivos do iPhone para o Windows de forma rápida. No Android, o Bluetooth resolve. No iPhone, não existe essa praticidade nativa.

Depois de procurar alternativas sem sucesso, a solução foi **construir a própria**. O **ITW** é um servidor local que roda no computador e expõe uma interface web acessível por qualquer dispositivo na mesma rede Wi-Fi — basta escanear um QR Code.

> *Um problema real → uma solução real. Feito do zero.*

---

## ✨ Como Funciona

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   $ python main.py                                      │
│                                                         │
│   ██████  ←  QR Code gerado automaticamente no terminal │
│   ██  ██                                                │
│   ██████      http://192.168.X.X:8000                   │
│                                                         │
│   📱  Escaneie → Navegador abre → Selecione → Envie     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

1. **Inicia o servidor** — `python main.py`
2. **QR Code aparece** no terminal com o IP da máquina detectado automaticamente
3. **Escaneia com o celular** — qualquer câmera ou leitor de QR
4. **Interface abre no navegador** — seleciona os arquivos
5. **Upload via streaming** — o arquivo chega e é salvo na pasta `/uploads`

---

## 🚀 Funcionalidades

- 📡 **Detecção automática de IP** — identifica a interface Wi-Fi ativa via `psutil`
- 📷 **QR Code no terminal** — acesso imediato sem digitar URL
- 📦 **Upload em chunks** — streaming de 1MB por vez, sem sobrecarregar a memória
- 🔒 **Sanitização de path** — remove diretórios maliciosos do nome do arquivo
- 🌐 **Interface web responsiva** — funciona em qualquer navegador mobile
- ⚡ **Zero configuração** — rode e use

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|-----------|-----|
| **Python** | Linguagem principal |
| **FastAPI** | Framework web assíncrono |
| **Uvicorn** | Servidor ASGI |
| **Psutil** | Detecção de interfaces de rede |
| **PyQRCode** | Geração do QR Code no terminal |

---

## 📦 Instalação

### Pré-requisitos
- Python 3.10+
- Computador e celular na **mesma rede Wi-Fi**

### Passos

```bash
# 1. Clone o repositório
git clone https://github.com/GROSSIDEV/itw.git
cd itw

# 2. Instale as dependências
pip install fastapi uvicorn psutil pyqrcode

# 3. Execute
python main.py
```

> A pasta `/uploads` é criada automaticamente na primeira execução.

---

## 📁 Estrutura

```
itw/
├── main.py          # Servidor FastAPI + lógica de upload
├── static/
│   └── index.html   # Interface web do celular
└── uploads/         # Arquivos recebidos (criado automaticamente)
```

---

## ⚠️ Observações

- O servidor aceita conexões de **qualquer dispositivo na rede** (`host="0.0.0.0"`). Use em redes confiáveis.
- Desenvolvido e testado no **Windows**. O nome da interface `'Wi-Fi'` pode variar em outros sistemas operacionais.

---

## 👤 Autor

**GROSSIDEV**

[![GitHub](https://img.shields.io/badge/GitHub-GROSSIDEV-181717?style=flat-square&logo=github)](https://github.com/GROSSIDEV)
