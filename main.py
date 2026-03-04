#!/home/isq/projects/books/.venv/bin/python3

import os

books = {
    'ge': '/home/isq/Documents/TI/ge_geometria-euclidiana/geometria-euclidiana.pdf',
    'me': '/home/isq/Documents/TI/me_matematica-elementar/notas-de-aula-me.pdf',
    'ppc': '/home/isq/Documents/TI/curso/ppc.pdf',
}

hooks = {
    'sioyek': 'sioyek',
    'default': 'sioyek',
}

import typer


def check_existence(entity: str, entities: dict, name: str):
    if entity not in entities:
        typer.echo(f'{name} not found. Available options: [{', '.join(entities.keys())}]')
        return False

    return True


def main(book: str, hook: str | None = None) -> None:
    if not check_existence(book, books, 'Book'):
        return

    if hook is not None:
        if not check_existence(hook, hooks, 'Hook'):
            return
    else:
        hook = hooks['default']

    os.system(hook + ' ' + books[book])

if __name__ == "__main__":
    typer.run(main)
