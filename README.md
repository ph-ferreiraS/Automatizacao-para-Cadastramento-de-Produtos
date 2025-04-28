
# 🐍 Automação de Cadastro de Produtos com Python

Este projeto demonstra como automatizar o cadastro de produtos em um sistema web utilizando Python. A automação controla o mouse e o teclado para preencher formulários, economizando horas de trabalho manual e reduzindo erros humanos.

---

## 🚀 **Funcionalidades**
- **Automatização completa**: Abre o navegador, faz login e cadastra produtos automaticamente.
- **Leitura de dados**: Importa informações de um arquivo CSV (`produtos.csv`) com 264 produtos.
- **Preenchimento inteligente**: Navega entre campos usando `Tab` e valida campos opcionais (como observações).
- **Controle de tempo**: Define pausas entre ações para garantir a execução correta.

---

## ⚙️ **Tecnologias Utilizadas**
- **Python**: Linguagem principal para scripts de automação.
- **Pandas**: Biblioteca para importar e manipular dados do CSV.
- **PyAutoGUI**: Controla o mouse e o teclado para simular ações humanas.
- **Time**: Define intervalos de espera entre ações.

---

## 📂 **Estrutura do Projeto**
```
automatizacao-cadastro/
├── produtos.csv          # Base de dados dos produtos
├── pegar_posição.py      # Script auxiliar para capturar coordenadas do mouse
└── codigo.py          # Script principal de automação
```

---

## 🔧 **Como Executar**
1. **Instale as dependências**:
   ```bash
   pip install pandas pyautogui
   ```

2. **Prepare o ambiente**:
   - Coloque `produtos.csv` na mesma pasta do script.
   - Use `pegar_posição.py` para obter as coordenadas do mouse no seu monitor.

3. **Execute o script principal**:
   ```bash
   python automacao.py
   ```

---

## 📋 **Etapas da Automação**
1. **Abre o navegador**:
   ```python
   pyautogui.press("win")
   pyautogui.write("chrome")
   pyautogui.press("enter")
   ```

2. **Faz login no sistema**:
   - Preenche e-mail e senha automaticamente.

3. **Cadastra produtos**:
   - Percorre cada linha do CSV.
   - Preenche campos como código, marca, preço e observações (se houver).
   - Envia o formulário e repete até finalizar todos os registros.

---

## 💡 **Resultados Esperados**
- **Economia de tempo**: Cadastro de 264 produtos em minutos, sem intervenção manual.
- **Redução de erros**: Dados são inseridos diretamente do CSV, evitando digitação incorreta.
- **Escalabilidade**: Adaptável para outras tarefas repetitivas (ex: relatórios, extração de dados).

---

## 📌 **Notas Importantes**
- **Coordenadas do mouse**: Ajuste as posições `(x, y)` conforme seu monitor usando `pegar_posição.py`.
- **Tempo de espera**: Ajuste `pyautogui.PAUSE` conforme a velocidade do seu sistema.

---

✨ **Inspiração**: Projeto desenvolvido durante a aula *Python Power UP* da [Jornada Python](https://www.youtube.com/@hashtagprogramacao).  
``` 


