# Programa em python para verificar se todos os dados de uma lista são pares. Caso sejam todos pares devolver True e caso contrario False.

import random

def sãoPares():
    list = [2, 4, 6, 9]
    print(list)
    while list:
        if list[0]%2 != 0:
            verifier = False
            break
        else:
            verifier = True
            list.pop(0)
        
    print(verifier)
        
sãoPares()