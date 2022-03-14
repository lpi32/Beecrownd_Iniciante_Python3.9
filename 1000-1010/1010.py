# 1010 calculo simples - Python 3.9

peca1 = input().split(" ")
peca2 = input().split(" ")

codigo1, quantidade1, preco_unitario1 = peca1
codigo2, quantidade2, preco_unitario2 = peca2

TOTAL = (int(quantidade1) *float(preco_unitario1)) + (int(quantidade2) * float(preco_unitario2))

print(f'VALOR A PAGAR: R$ {TOTAL:.2f}')

