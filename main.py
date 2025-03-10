import sqlite3


def conectar_banco():
    return sqlite3.connect('banco.db')

def consultar(consulta):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(consulta)
    conexao.commit()
    cursor.close()
    conexao.close()

def lista():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM estoque;")
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)


def add_forncedor(nome:str):
    consultar(f"INSERT INTO fornecedores (nome) VALUES ('{nome}');")

def add_produto(nome:str):
    consultar(f"INSERT INTO produtos (nome) VALUES ('{nome}') ")

def add_estoque(produtoID, fornecedorID, quantidade, data):
    consultar(f"INSERT INTO estoque (produtoID, fornecedorID, quantidade, data) VALUES ('{produtoID}','{fornecedorID}','{quantidade}','{data}') ")



"""GROUP BY serve para agrupar dados com base em uma ou mais colunas e aplicar funções como COUNT, SUM, AVG, a DEF aseguir é um exemplo utilizando SUM"""
def group_by():
     conexao = conectar_banco()
     cursor = conexao.cursor()
     cursor.execute(
     ("SELECT produtoID, SUM(quantidade) AS total_estoque FROM estoque GROUP BY produtoID;"))
     registros = cursor.fetchall()
     print('lista de produtos')
     for registro in registros:
         print(registro)


"""esta funçao tem somente o objetivo de adicionar coluna como um exemplo de 'ALTER TALBE'."""
def alter_table(tabela:str, coluna:str, tipo:str):
    consultar(f"ALTER TABLE {tabela} ADD COLUMN {coluna} {tipo};")


"""No SQLite, FULL OUTER JOIN não é suportado, mas podemos simular essa operação usando LEFT JOIN + RIGHT JOIN + UNION"""
def outer_join():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""SELECT Produtos.ProdutoID, Produtos.Nome, Estoque.Quantidade, Estoque.Data
    FROM Produtos
    LEFT JOIN Estoque ON Produtos.ProdutoID = Estoque.ProdutoID

    UNION

    SELECT Estoque.ProdutoID, Produtos.Nome, Estoque.Quantidade, Estoque.Data
    FROM Estoque
    LEFT JOIN Produtos ON Estoque.ProdutoID = Produtos.ProdutoID;""")
    lista = cursor.fetchall()
    for item in lista:
        print(item)
    cursor.close()
    conexao.close()

fornecedor1 = add_forncedor('hugo')
fornecedor2 = add_forncedor('luisa')
fornecedor3 = add_forncedor('victoria') 
fornecedor4 = add_forncedor('hudson')

produto1 = add_produto('teclado')
produto2 = add_produto('mouse')
produto3 = add_produto('monitor')
produto4 = add_produto('computador')

estoque1 = add_estoque(3, 1, 20, 2025-3-6)
estoque2 = add_estoque(1, 3, 22, 2025)
estoque3 = add_estoque(2, 4, 18, 2023)


"""opcao1 = alter_table('estoque', 'preco_unit', 'REAL')"""
"""opcao2 = group_by()"""
"""opcao3 = outer_join()"""

lista()