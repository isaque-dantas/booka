# Booka 📚

🇺🇸 A minimal CLI to manage and open books/documents via configurable hooks (PDF readers).

🇧🇷 Um CLI minimalista para gerenciar e abrir livros/documentos via hooks configuráveis (leitores de PDF).

---

## Installation / Instalação

🇺🇸 Requires [`uv`](https://docs.astral.sh/uv/getting-started/installation/) and Python 3.10+.

🇧🇷 Requer [`uv`](https://docs.astral.sh/uv/getting-started/installation/) e Python 3.10+.

```bash
# Linux only / somente Linux
bash install.sh
```

🇺🇸 This creates a symlink making `bk` available system-wide.

🇧🇷 Isso cria um link simbólico que disponibiliza o `bk` em todo o sistema.

---

## Usage / Uso

### Open a book / Abrir um livro
```bash
bk o <n>                   # open with default hook / abrir com o hook padrão
bk o <n> --hook <hook>     # open with a specific hook / abrir com um hook específico
```

### Manage books / Gerenciar livros
```bash
bk add <n> <path>          # add a book / adicionar um livro
bk rm <n>                  # remove a book / remover um livro
bk ls                      # list all books / listar todos os livros
```

### Manage hooks / Gerenciar hooks
```bash
bk add <n> <path> --hook   # add a hook / adicionar um hook
bk rm <n> --hook           # remove a hook / remover um hook
bk ls --hook               # list all hooks / listar todos os hooks
bk --default-hook <n>      # set the default hook / definir o hook padrão
```

---

## Example / Exemplo

```bash
bk add geb "/home/user/books/geb.pdf"
bk add zathura "/usr/bin/zathura" --hook
bk --default-hook zathura
bk o geb
```