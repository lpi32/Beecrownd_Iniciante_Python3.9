# 1019

segundos=int(input())
seg = (segundos % 60)
min = (segundos // 60) %60
hor = ((segundos // 60) // 60) % 60
print(f"{hor}:{min}:{seg}")

