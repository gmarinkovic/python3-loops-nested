# Дата је реч и природан број n. Напиши програм који исписује све њене подречи (сегменте узастопних карактера)
# дужине n.
#
# Улаз: Први ред стандардног улаза садржи реч састављену од малих слова енглеског алфабета, а други садржи
# број n.
#
# Излаз: На стандардни излаз исписати све тражене подречи, с лева на десно, сваку у посебном реду.
#
# Пример
# Улаз
# abcdef
# 3
# Излаз
# abc
# bcd
# cde
# def

rec = input("Unesi rec: ")
n = int(input("Unesi broj slova unutar podreci: "))

for i in range(0, len(rec) - n + 1):        # poslednja slova zadate reci ne mogu da grade pod rec u trazenoj duzini
    for j in range(0, n):                   # definise duzinu podreci   
        print(rec[i+j], end=" ", sep="")
    print()
