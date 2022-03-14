# 1009 - Salário com Bônus - python 3.8

NOME = str(input())
SALARIO = float(input())
VENDAS = float(input())

# calculo

COMISSAO = (VENDAS * 15)/100
TOTAL = SALARIO + COMISSAO

print(f"TOTAL = R$ {TOTAL:.2f}")