# Booka

---

### 🇺🇸 EN_US &nbsp;|&nbsp; 🇧🇷 PT_BR

---

This is a simple CLI script where you can define books and their paths. You can define hooks, too, trough what you can associate your preferred PDF reader to Booka.

Este é um simples 'script' CLI onde você pode definir livros e os seus caminhos (diretórios). Você também pode definir hooks, através dos quais é possível associar o seu leitor de PDF preferido ao Booka.

---

## Usage / Como utilizar

#### 🇺🇸 EN_US

To customize this application to your usage, edit contents of dictionaries in main.py. Hooks and books identifiers are based on dictionaries keys.

For example, there are three books/documents here. To open the first one I can simply type `bk ge`. To select a hook, I can use `bk ge --hook sioyek`. Options can be changed to fit your needs.
```py
books = {
    'ge': '/home/isq/Documents/TI/ge_geometria-euclidiana/geometria-euclidiana.pdf',
    'me': '/home/isq/Documents/TI/me_matematica-elementar/notas-de-aula-me.pdf',
    'ppc': '/home/isq/Documents/TI/curso/ppc.pdf',
}
```

#### 🇧🇷 PT_BR

Para personalizar a aplicação ao seu uso, edite o conteúdo dos dicionários em `main.py`. Os identificadores de hooks e livros são baseados nas chaves dos dicionários.

Por exemplo, há três livros/documentos aqui. Para abrir o primeiro, basta digitar `bk ge`. Para selecionar um hook, use `bk ge --hook sioyek`. As opções podem ser alteradas conforme a sua necessidade.
```py
books = {
    'ge': '/home/isq/Documents/TI/ge_geometria-euclidiana/geometria-euclidiana.pdf',
    'me': '/home/isq/Documents/TI/me_matematica-elementar/notas-de-aula-me.pdf',
    'ppc': '/home/isq/Documents/TI/curso/ppc.pdf',
}
```

---

## Installation / Instalação

#### 🇺🇸 EN_US

This is a Python project that uses `uv` instead of `pip`. Install it [here](https://docs.astral.sh/uv/getting-started/installation/).

This project was tested using Python 3.13, but dependencies are compatible with Python 3.10 and above.

If you are in Linux, you can simply install `uv` and run `install.sh`. It will create a symbolic link that points to `main.py` and makes Booka available through your whole system.

#### 🇧🇷 PT_BR

Este é um projeto Python que usa `uv` ao invés de `pip`. Instale-o [aqui](https://docs.astral.sh/uv/getting-started/installation/).

Este projeto foi testado com Python 3.13, mas as dependencias são compatíveis com Python 3.10 ou superior.

Se você estiver no Linux, basta instalar o `uv` e executar `install.sh`. Ele criará um link simbólico que aponta para `main.py` e torna o Booka disponível em todo o sistema.