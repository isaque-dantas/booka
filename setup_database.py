import sqlite3
import os
import sys


def main():
    if os.path.exists('database.db'):
        print('O arquivo database.db já existe. Remova-o para atualizar o banco de dados.')
        sys.exit(0)

    with sqlite3.connect('database.db') as connection:
        connection.execute('''
                           CREATE TABLE IF NOT EXISTS books
                           (
                               name VARCHAR UNIQUE NOT NULL,
                               path VARCHAR UNIQUE NOT NULL
                           );
        ''')
        connection.execute('''
                           CREATE TABLE IF NOT EXISTS hooks
                           (
                               name VARCHAR UNIQUE NOT NULL,
                               path VARCHAR UNIQUE NOT NULL
                           );
        ''')

    print('Banco de dados inicializado com sucesso!')


if __name__ == '__main__':
    main()
