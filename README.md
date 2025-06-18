# Projeto de Processamento Digital de Imagens (PDI)

Este projeto foi desenvolvido como trabalho final da disciplina de **Processamento Digital de Imagens**, cursada na **Universidade Feevale**. O objetivo era desenvolver uma aplicação interativa para manipulação de imagens, com **filtros utilizados na área de PDI** e transformações geométricas, tudo aplicado em uma interface gráfica feita com **Python, Tkinter e Pillow**.

---

## 🖼️ Descrição do Projeto

A aplicação permite carregar, visualizar, salvar e manipular imagens por meio de diversos filtros, tanto de uso geral (como brilho, contraste, escala, rotação) quanto específicos da área de PDI (como filtros de Passa Baixa, Passa Alta, Threshold, Morfologia Matemática, etc).

Como uma entrega final, um **desafio prático** foi proposto: identificar comprimidos em uma imagem. Esses comprimidos podem assumir três formas:
- 💊 Cápsulas
- ⚪ Comprimidos redondos
- ❌ Comprimidos quebrados (que nesse caso, não podem ser aproveitados)

A aplicação então realiza automaticamente a leitura de uma imagem exemplo contendo essas pílulas, aplica os filtros necessários e retorna estatísticas precisas sobre os elementos detectados.

---

## ⚙️ Tecnologias utilizadas

- **Python 3.10+**
- **Tkinter** – interface gráfica
- **Pillow** – manipulação de imagens
- Algoritmos manuais de:
  - Filtros espaciais (média, Sobel, Threshold)
  - Morfologia matemática (Erosão, Dilatação, Abertura, Fechamento)
  - Análise de componentes conectados

---

## 📦 Como rodar o projeto?

### ✅ Pré-requisitos

Certifique-se de ter o Python instalado. Use `python --version` ou `python3 --version` no terminal.

### 💻 Instruções por sistema operacional

#### 🪟 Windows

1. Instale as dependências:
   
```bash
pip install pillow
pip install tk
```

2. Acesse a pasta do projeto:
```bash
cd src
```

3. Rode o App:
```bash
python main.py
```

#### 🐧 Linux
1. Crie um Ambiente Virtual (Opcional):
```bash
python3 -m venv venv
source venv/bin/activate
pip install pillow
```

2. Acesse a pasta do projeto:
```bash
cd src
```

3. Rode o App:
```bash
python main.py
```

---

## ⚠️ Atenção para usuários Linux:
Por alguma limitação de compatibilidade com o tkinter.filedialog, pode ocorrer erro ao utilizar o filtro de arquivos na função open_image(), na classe Menu:
```python
# Substitua esta linha:
filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])  # Windows

# Por esta:
filepath = filedialog.askopenfilename()  # Linux
```
Essa modificação está comentada no próprio código.

---

## 👩‍🏫 Professora responsável

Profa. Dra. Marta Rosecler Bez
Professora da disciplina de Processamento Digital de Imagens
Universidade Feevale
