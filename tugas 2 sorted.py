data = ('25,16,6,10,3,5')
angka = list(map(int, filter(None, data.split(','))))
angka_terurut = sorted(angka)
print("Bilangan terurut:", angka_terurut)