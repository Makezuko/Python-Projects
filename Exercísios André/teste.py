total = 0
numero_anterior = None
quantidade_zeros = 0

while True:
    try:
        numero = float(input("Insira um número (positivo para adicionar, 0 para tirar o último número adicionado e negativo para parar): "))
        
        if numero > 0:
            total += numero
            numero_anterior = numero
            quantidade_zeros = 0
        elif numero == 0:
            if numero_anterior is not None and quantidade_zeros < 3:
                total -= numero_anterior
                numero_anterior = None
                quantidade_zeros += 1
        else:  # número negativo
            break
    except ValueError:
        print("Por favor, digite um número válido.")

print("O resultado é:", total)