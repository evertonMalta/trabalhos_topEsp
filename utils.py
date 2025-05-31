import os
from datetime import datetime


def Clear():
    os.system('cls' if os.name=='nt' else 'clear')

def Error():
    input("\n\nComando Não identificado!\n")

def TryParseOpcInput(opc):
    try:
        opc = int(opc)
    except:
        opc = -1
    
    return opc

def parse_datetime(value):
    try:
        return datetime.fromisoformat(value)
    except (TypeError, ValueError):
        return value  

