# Sequência de Fibonacci
n = int(input(" Digite Quantos termos você deseja: "))
t1 = 0
t2 = 1
t3 = 0

while n >= t3:
    print("{} ".format(t3), end="")
    t3 = t1 + t2
    t1 = t2
    t2 = t3