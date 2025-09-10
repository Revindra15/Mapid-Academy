# Input 2 bilangan
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))

# Bandingkan
if a > b:
    print("Bilangan terbesar adalah:", a)
elif b > a:
    print("Bilangan terbesar adalah:", b)
else:
    print("Kedua bilangan sama besar:", a)