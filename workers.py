import yfinance as yf
from verificaConexão import *

def downloadCotações(simbolos, collection):
    for simbolo in simbolos:
        testaConexão()
        data = yf.download(simbolo, period='max')
        access = data[['Open', 'High', 'Low', 'Close', 'Volume']]
        collection[simbolo] = getValues(access)

def formataId(getId):
    resultado = []
    for id in getId:
        idStr = str(id)
        idFormatado = idStr[0:10]
        resultado.append(idFormatado)
    return resultado

def getValues(access):
    cotações = access.values.tolist()
    id = access.index.tolist()
    resultado = organizaResultado(formataId(id), cotações)
    return resultado

def organizaResultado(idFormatado, cotações):
    resultado = []
    for id, cotação in zip(idFormatado, cotações):
        cotação.insert(0, id)
        resultado.append(cotação)
    return resultado



