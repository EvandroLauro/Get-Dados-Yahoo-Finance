import urllib
import requests
import time

def testaConexão():
    restart = True
    while restart:
        conectado = conecta()
        if conectado == True:
            break
        elif conectado == False:
            print("Não Conectado ou Yahoo Finance esta fora do ar temporariamente")
            time.sleep(5)
            print("Aguarde... Estamos tentando restabelecer a conexão")
            time.sleep(10)
            continue

def conecta(host="https://finance.yahoo.com/"):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

