# За унету реч исписати све подречи у редоследу опадајуће дужине и растућих левих граница за речи исте
# дужине.
# Улаз: Са стандардног улаза се уноси једна реч састављена само од малих слова енглеске абецеде.
# Излаз: На стандардни излаз исписати тражене подречи, сваку у посебном реду.
# Пример
# Улаз
# abc
# Излаз
# abc
# ab
# bc
# a
# b
# c

rec = input("Unesi izabranu rec: ")

for d in range(len(rec), 0, -1):                      # sa -1 idemo unazad
    for i in range(len(rec) - d + 1):
        for j in range(i, i+d):
            print(rec[j], end="")
        print()
