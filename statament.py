from mySimbolos import *
from processador import *
from workers import *
from saveBD import *

if __name__ == "__main__":
    cotações = controlaMultiplosProcess(requisitandoSimbolos(), downloadCotações)
    salvando(cotações)
