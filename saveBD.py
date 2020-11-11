import sqlite3

def salvando(cotações):
    print("Salvando cotações, aguarde.")
    con = sqlite3.connect('banco-de-dados.db', timeout=160.0)
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for simbolo in cotações:
        for cotação in cotações[simbolo]:
            cursor.execute("create table if not exists'" + simbolo + "' (Id, Open, High, Low, Close, Volume)")
            cursor.execute("INSERT INTO'" + simbolo + "'(Id, Open, High, Low, Close, Volume) " "VALUES(?,?,?,?,?,?)",(cotação))
    con.commit()
    con.close()
    print("Cotações salvada com sucesso") ##########################################################################################

