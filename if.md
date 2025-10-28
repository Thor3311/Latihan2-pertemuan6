# Praktikum_4: IF 
# Latihan 1: Menentukan Bilangan Terbesar dari 4 Bilangan (Python)

## Penjelasan Tugas
Tugas ini bertujuan untuk membuat program Python yang dapat menerima empat buah input bilangan bulat dan menentukan serta mencetak bilangan mana yang memiliki nilai terbesar.

## Kode Program (4bilangan_terbesar.py)

```python
A = int(input("bilangan 1: "))
B = int(input("bilangan 2: "))
C = int(input("bilangan 3: "))
D = int(input("bilangan 4: "))

# carilah bilangan terbesar dari empat bilangan tersebut


if A >= B and A >= C and A >= D:
    print("1 bilangan terbesar")
elif B >= A and B >= C and B >= D:
    print("2 bilangan terbesar")
elif C >= A and C >= B and C >= D:
    print("3 bilangan terbesar")
else:
    print("4 bilangan terbesar")
```

Penjelasan Kode Program:
1. Input Data: Program meminta 4 bilangan dari user (A, B, C, D)
2. Perbandingan Berurutan:
```
if A >= B and A >= C and A >= D: Cek apakah A terbesar
elif B >= A and B >= C and B >= D: Cek apakah B terbesar
elif C >= A and C >= B and C >= D: Cek apakah C terbesar
else: Jika bukan A, B, atau C, maka D pasti terbesar
```
Output: Menampilkan urutan bilangan mana yang terbesar
## Hasil OUTPUT 
<img width="1912" height="545" alt="image" src="https://github.com/user-attachments/assets/8545d3f0-669f-421e-b6ab-cc56806d8df5" />

---
# Latihan 2: Mengurutkan Data (Python)

## Penjelasan Tugas
Tugas ini bertujuan untuk membuat program Python yang dapat memproses string berisi angka yang dipisahkan koma (",") dan mengurutkannya.

## Kode Program (MengurutkanData.py)

```python
data = "25,16,6,10,3,5,"
angka = list(map(int, filter(None, data.split(','))))
angka_terurut = sorted(angka)
print("Bilangan terurut:", angka_terurut)

```
Penjelasan Kode Program:
- Data Awal: String "25,16,6,10,3,5,"

- Tahapan Proses:
  - Memisahkan string berdasarkan koma menjadi list string
  - Menghapus elemen kosong dari list
  - Mengubah setiap string menjadi integer
  - Mengurutkan bilangan dari terkecil ke terbesar
- Hasil Akhir: [3, 5, 6, 10, 16, 25]

- Fungsi Penting:
  - split(): memisahkan string
  - filter(): menghapus nilai kosong
  - map(): mengubah tipe data
  - sorted(): mengurutkan data

- Visualisasi Proses:
```
"25,16,6,10,3,5,"
     ↓ split(',')
['25','16','6','10','3','5',''] 
     ↓ filter(None)  
['25','16','6','10','3','5'] 
     ↓ map(int)
[25, 16, 6, 10, 3, 5] 
     ↓ sorted()
[3, 5, 6, 10, 16, 25]
```

## Hasil OUTPUT 
<img width="1919" height="543" alt="image" src="https://github.com/user-attachments/assets/6416d340-25d4-4df3-80bd-f5cb05334abf" />
