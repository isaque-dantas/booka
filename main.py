#!/home/isq/projects/books/.venv/bin/python3

import os

import typer
from rich.console import Console
from rich.table import Table
import sqlite3

connection = sqlite3.connect('database.db')

app = typer.Typer()
console = Console()


@app.command()
def ls(hook: bool = False):
    """Obtém todos os livros ou hooks cadastrados."""
    table_name = "hooks" if hook else "books"
    table_title = "Hooks" if hook else "Livros"

    result = connection.execute(f"SELECT name, path FROM {table_name}")
    rows = result.fetchall()
    if len(rows) == 0:
        console.print(f"Não há {table_title} cadastrados.")
        return

    table = Table("Nome", "Caminho", title=table_title)
    for row in rows:
        table.add_row(row[0], row[1])
    console.print(table)


@app.command()
def add(name: str, path: str, hook: bool = False):
    """Adiciona um livro ou hook"""
    table_name = "hooks" if hook else "books"

    connection.execute(
        f"INSERT INTO {table_name} (name, path) VALUES (?, ?)",
        (name, path)
    )
    connection.commit()


@app.command()
def rm(name: str, hook: bool = False):
    """Exclui um livro ou hook."""
    table_name = "hooks" if hook else "books"

    connection.execute(
        f"DELETE FROM {table_name} WHERE name = ?",
        (name,)
    )


@app.command()
def o(name: str, hook: str | None = None):
    """Abre um livro (ou documento qualquer), selecionando ou não um hook específico para isso."""

    if hook is None:
        hook_row = connection.execute("SELECT path FROM hooks WHERE is_default = ?", (1,)).fetchone()
        if hook_row is None:
            console.print("O hook padrão não foi escolhido. Execute 'bk --default_hook <nome>' para escolher um.",
                          style='red')
            return
    else:
        hook_row = connection.execute("SELECT path FROM hooks WHERE name = ?", (hook,)).fetchone()
        if hook_row is None:
            console.print(
                f"O hook '{hook}' não foi encontrado. Execute 'bk ls --hook' para obter os hooks disponíveis.",
                style='red')
            return

    hook_path = hook_row[0]

    book_row = connection.execute("SELECT path FROM books WHERE name = ?", (name,)).fetchone()
    if book_row is None:
        console.print(f"O livro '{name}' não foi encontrado. Execute 'bk ls' para obter os livros disponíveis.",
                      style='red')
        return

    book_path = book_row[0]

    os.system(f"{hook_path} {book_path}")


def check_existence(entity: str, entities: dict, name: str):
    if entity not in entities:
        typer.echo(f'{name} not found. Available options: [{', '.join(entities.keys())}]')
        return False

    return True


@app.callback(invoke_without_command=True)
def main(
        default_hook: str = typer.Option(None, "--default-hook", help="Escolha o hook padrão")
):
    if default_hook is not None:
        connection.execute("UPDATE hooks SET is_default = 0")
        result = connection.execute("UPDATE hooks SET is_default = 1 WHERE name = ?", (default_hook,))
        if result.rowcount == 0:
            console.print(f"O Hook '{default_hook}' não foi encontrado.", style='red')
            return

        connection.commit()
        console.print(f"Hook '{default_hook}' escolhido com sucesso!")


if __name__ == "__main__":
    app()
