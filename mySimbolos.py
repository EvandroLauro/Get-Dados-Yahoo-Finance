import sqlite3

def requisitandoSimbolos():
    simbolos = selectSimbolosBD()
    resultado = deletaSimbolosDuplicados(simbolos)
    return resultado

def selectSimbolosBD():
    con = sqlite3.connect('ativos-existente.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ativos;")
    resultado = cursor.fetchall()
    con.commit()
    con.close()
    return resultado

def deletaSimbolosDuplicados(rowsSimbolos):
    resultado = []
    for i in rowsSimbolos:
        listNumbers = list(i)
        for ii in listNumbers:
            resultado.append(ii)
        resultado = sorted(set(resultado))
    return resultado


