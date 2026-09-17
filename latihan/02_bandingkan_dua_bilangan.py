# Input
a = float(input("Bilangan pertama: "))
b = float(input("Bilangan kedua: "))

# Proses keputusan dengan nested if
if a >= b:
    if a == b:
        print("Kedua bilangan sama.")
    else:
        print("Bilangan pertama lebih besar.")
else:
    print("Bilangan pertama lebih kecil.")