# 🕵️‍♂️ DNS Monitor com Pyshark

Um script simples e eficaz em Python para **monitorar requisições DNS em tempo real** usando a biblioteca [Pyshark](https://github.com/KimiNewt/pyshark) – um wrapper poderoso para o Wireshark/TShark.

---

## 📌 Funcionalidade

Este script captura pacotes DNS da rede e exibe:

- 🌐 O **domínio** requisitado (ex: `www.google.com`)
- 📥 O **IP de origem** (quem fez a requisição)
- 📤 O **IP de destino** (servidor DNS)
- 🕒 O **timestamp** de cada pacote

Exemplo de saída:

