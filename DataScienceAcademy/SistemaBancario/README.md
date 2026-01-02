# Aplicação Full-Stack de Sistema Bancário em Python (POO)**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-%20Finalizado-yellow)
![Licença](https://img.shields.io/badge/Licença-MIT-green)
![POO](https://img.shields.io/badge/Paradigma-POO-purple)

Este mini-projeto implementa um sistema bancário simples utilizando **Python** e **Programação Orientada a Objetos (POO)**.  
A aplicação é modularizada para garantir organização, clareza e separação de responsabilidades.  
A interação com o usuário ocorre via **CLI (Command Line Interface)**.

---

## 📌 **Descrição dos Diretórios**

### **📂 entidades/**
Contém as classes que representam as entidades principais do sistema:
- `Cliente`
- `Conta`

### **📂 operacoes/**
Responsável pela **lógica de negócio**, incluindo:
- `Banco`: gerencia clientes, contas e operações bancárias.

### **📂 utilitarios/**
Contém utilitários, como:
- Exceções personalizadas (`exceptions.py`)

### **📄 sistema_Bancario.py**
Arquivo principal da aplicação.  
É o **ponto de entrada** do sistema e implementa a interface CLI utilizada pelo usuário.

---

## ▶️ **Como Executar o Projeto**

1. Abra o **terminal** ou **prompt de comando**  
2. Navegue até a pasta do projeto  
3. Execute o comando:

`python sistema_Bancario.py`
