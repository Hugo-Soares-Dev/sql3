import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE produtos(
               produtoID INTEGER PRIMARY KEY
               ,nome TEXT NOT NULL)
    """)
cursor.execute("""CREATE TABLE fornecedores(
               fornecedorId INTEGER PRIMARY KEY
               ,nome TEXT NOT NULL)""")

cursor.execute("""CREATE TABLE estoque(
               estoqueID INTEGER PRIMARY KEY
               ,produtoID INTEGER NOT NULL
               ,fornecedorID INTEGER NOT NULL
               ,quantidade INTEGER NOT NULL
               ,data DATE NOT NULL
               ,FOREIGN KEY (produtoID) REFERENCES produtos(produtoID)
               ,FOREIGN KEY (fornecedorID) REFERENCES fornecedores(fornecedorID)
               )""")

conexao.commit()
cursor.close()
conexao.close()