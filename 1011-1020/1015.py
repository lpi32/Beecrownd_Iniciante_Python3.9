distancias1 = input().split()
distancias2 = input().split()
x1, y1 = distancias1
x2, y2 = distancias2
distancia = (((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2)) ** 0.5
print(f"{distancia:.4f}")
