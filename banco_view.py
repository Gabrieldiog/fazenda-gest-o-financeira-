import sqlite3 as sql
import pandas as pd

#conexao
con = sql.connect("gestao.db")

# inserir categoria

def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query,i)
        

#inserir receitas
def inserir_receitas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query,i)

#inserir Gastos
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query,i)

#funcoes para deletar
#deletar receitas

def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, (i,))


def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query, (i,))

#funcoes para ver dados

#ver categorial
def ver_categoria():

    listas_itens = []

    with con:
        cun = con.cursor()
        cun.execute("SELECT * FROM Categoria")
        linha = cun.fetchall()
        for l in linha:
            listas_itens.append(l)
    return listas_itens


#receitas
def ver_receitas():

    listas_itens = []

    with con:
        cun = con.cursor()
        cun.execute("SELECT * FROM Receitas")
        linha = cun.fetchall()
        for l in linha:
            listas_itens.append(l)
    return listas_itens


#ver gastos
def ver_Gastos():

    listas_itens = []

    with con:
        cun = con.cursor()
        cun.execute("SELECT * FROM Gastos")
        linha = cun.fetchall()
        for l in linha:
            listas_itens.append(l)
    return listas_itens

def tabela():
    gastos = ver_Gastos()
    receitas = ver_receitas()

    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista

def bar_valores():
    #receitas total
    receitas = ver_receitas()
    receistas_lista = []

    for i in receitas:
        receistas_lista.append(i[3])
    
    receita_total = sum(receistas_lista)

    #gastos totais
    gastos = ver_Gastos()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3])
    
    gastos__total = sum(gastos_lista)

    #saldo total
    saldo_total = receita_total - gastos__total
    return[receita_total, gastos__total, saldo_total]



def grafico_pizza():
    # Obtém os dados de gastos
    gastos = ver_Gastos()
    tabela_lista = []

    # Organiza os dados em uma lista
    for i in gastos:
        tabela_lista.append(i)
    
    # Cria o dataframe
    dataframe = pd.DataFrame(tabela_lista, columns=['id', 'categoria', 'Data', 'valor'])

    # Agrupa os dados por categoria e soma os valores
    dataframe = dataframe.groupby('categoria')['valor'].sum()

    # Cria uma lista de valores (quantias)
    lista_quantias = dataframe.values.tolist()

    # Cria uma lista de categorias
    lista_categoria = dataframe.index.tolist()  # Usando .tolist() diretamente aqui
    
    return [lista_categoria, lista_quantias]

def porcentagem_valor():
        # Obtém os dados de gastos
    receitas = ver_receitas()
    receistas_lista = []

    for i in receitas:
        receistas_lista.append(i[3])
    
    receita_total = sum(receistas_lista)

    #gastos totais
    gastos = ver_Gastos()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3])
    
    gastos__total = sum(gastos_lista)

    #porcentagem total
    total = ((receita_total - gastos__total) / receita_total) * 100
    return[total]




