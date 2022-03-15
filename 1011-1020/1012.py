#1012
lervalores=input().split()
A, B, C  = lervalores
pi = 3.14159
TRIANGULO = (float(A) * float(C))/2
CIRCULO = pi * (float(C)**2)
TRAPEZIO = ((float(A) + float(B))* float(C) )/2
QUADRADO = float(B) ** 2
RETANGULO = (float(A) * float(B))

print(f'TRIANGULO: {TRIANGULO:.3f}\nCIRCULO: {CIRCULO:.3f}\nTRAPEZIO: {TRAPEZIO:.3f}\nQUADRADO: {QUADRADO:.3f}\nRETANGULO: {RETANGULO:.3f}')
