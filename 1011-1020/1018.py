#1018 cedulas
dinheiro=int(input())

nota100 = dinheiro // 100
nota50 = (dinheiro % 100) // 50
nota20 = ((dinheiro % 100) % 50) //20
nota10 = (((dinheiro % 100) % 50) % 20) // 10
nota5=((((dinheiro % 100) % 50) % 20) % 10) // 5
nota2=(((((dinheiro % 100) % 50) % 20) % 10) % 5) //2
nota1=((((((dinheiro % 100) % 50) % 20) % 10) % 5) %2) //1

print(f"{dinheiro}\n{nota100} nota(s) de R$ 100,00\n{nota50} nota(s) de R$ 50,00\n{nota20} nota(s) de R$ 20,00\n{nota10} nota(s) de R$ 10,00\n{nota5} nota(s) de R$ 5,00\n{nota2} nota(s) de R$ 2,00\n{nota1} nota(s) de R$ 1,00")

