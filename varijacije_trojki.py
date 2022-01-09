# Сваки од три другара има одређени број јабука, али никоја два од њих немају исти број јабука. Ако се зна
# највећи могући број јабука који сваки од другара може да има, напиши програм који исписује све могуће
# тројке бројева јабука које они могу да имају.
#
# Улаз: Са стандардног улаза се уноси број n (1 ≤ n ≤ 20) - највећи број јабука које сваки од другара може
# да има.
#
# Излаз: На стандардни излаз исписати све могуће бројеве јабука које другови могу да имају, уређене лексикографски.
#
# Пример
# Улаз
# 2
# Излаз
# 0 1 2
# 0 2 1
# 1 0 2
# 1 2 0
# 2 0 1
# 2 1 0

n = int(input("Unesi maksimalni broj jabuka koje pojedinac moze da ima: "))
for d1 in range(n + 1):                     # broj jabuka prvog
    for d2 in range(n + 1):                 # broj jabuka drugog
        if d1 != d2:
            for d3 in range(n + 1):         # broj jabuka treceg
                if d1 != d3 and d2 != d3:
                    print(d1, d2, d3)
