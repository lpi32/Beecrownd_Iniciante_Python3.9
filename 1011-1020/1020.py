dias=int(input())
ano = dias // 365
mes = (dias % 365) //30
dia = (dias % 365) % 30
print(f"{ano} ano(s)\n{mes} mes(es)\n{dia} dia(s)")