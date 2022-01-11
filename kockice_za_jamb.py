# Исписати све резултате бацања три коцкице за јамб у којима је збир бројева једнак задатом броју X
# (природан број од 3 до 18) ако је редослед коцкица битан (на пример, 2, 2, 3 није исто као 2, 3, 2).
#
# Улаз: У једној линији стандардног улаза наводи се природан број X (3 ≤ X ≤ 18) који представља збир
# бројева на којима су се зауставиле коцкице.
#
# Излаз: У свакој линији стандардног излаза исписују се три природна броја (бројеви од 1 до 6)
# који представљају резултат бацања три коцкице. Резултате приказати сортиране лексикографски (у растућем редоследу
# троцифрених бројева који се формирају од три цифре на коцкицама).
#
# Пример
# Улаз
# 5
# Излаз
# 1 1 3
# 1 2 2
# 1 3 1
# 2 1 2
# 2 2 1
# 3 1 1

ocekivani_zbir_kockica = int(input("Unesi ocekivani zbir kockica za jamb (izmedju 3 i 18: "))
for a in range(1, 6 + 1):                                   # vrednost na prvoj kockici
    for b in range(1, 6 + 1):                               # vrednost na drugoj kockici
        for c in range(1, 6 + 1):                           # vrednost na trecoj kockici
            if a + b + c == ocekivani_zbir_kockica :        # ako je zbir jednak datom
                print(a, b, c)                              # ispisujemo resenje
