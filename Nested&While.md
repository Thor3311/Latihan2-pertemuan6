# Praktikum_4: Looping
# Latihan 1: perulangan bertingkat (nested loop) (Python)

## Penjelasan Tugas
Tugas ini bertujuan untuk membuat program Python yang dapat perulangan bertingkat (nested loop) untuk membuat pola angka.

## Kode Program (Perulangan.py)

```python
for i in range(1, 10):
    # Perulangan dalam (inner loop) untuk kolom
    for j in range(1, 10):
        # Menghitung hasil perkalian
        hasil = i + j
        # Mencetak hasil dengan format rata kanan
        print(f"{hasil:>4}", end="")
    
    # Pindah ke baris baru setelah perulangan dalam selesai
    print()                # Pindah ke baris berikutnya

```
Penjelasan Kode Program:
Struktur Perulangan:
- Loop luar (for i in range(10)): mengontrol baris (0 sampai 9)
- Loop dalam (for j in range(10)): mengontrol kolom (0 sampai 9)

Proses yang terjadi:
1. i = 0 (baris pertama):
```
j = 0 → print 0 + 0 = 0
j = 1 → print 0 + 1 = 1
j = 2 → print 0 + 2 = 2
... sampai j = 9 → print 0 + 9 = 9
```

2. print() pindah baris
```
i = 1 (baris kedua):
j = 0 → print 1 + 0 = 1
j = 1 → print 1 + 1 = 2
... dan seterusnya
```

- print(i + j, end=' '): Mencetak hasil penjumlahan dengan spasi (bukan enter)
- print(): Pindah ke baris baru setelah selesai satu baris lengkap

## Hasil OUTPUT 
<img width="1919" height="549" alt="image" src="/img/Nested.png" />

---

# Latihan 2: Menghasilkan dan mencetak angka acak (Python)

## Penjelasan Tugas
Tugas ini bertujuan untuk membuat program Python yang dapat Menghasilkan dan mencetak angka acak antara 0-1 sebanyak n kali, tetapi hanya angka yang kurang dari 0.5 yang dihitung dan dicetak.

## Kode Program (NilaiN.py)

```python
import random

# Meminta input dari pengguna untuk menentukan jumlah bilangan (n)
while True:
    try:
        n_input = input("Masukkan jumlah bilangan acak yang ingin ditampilkan (n): ")
        # Mengubah input menjadi integer
        n = int(n_input)
        # Memastikan n adalah bilangan positif
        if n > 0:
            break
        else:
            print("Masukkan bilangan bulat positif.")
    except ValueError:
        # Menangani jika input bukan angka
        print("Input tidak valid. Harap masukkan bilangan bulat.")

print(f"\nMenampilkan {n} bilangan acak yang lebih kecil dari 0.5:")

# Menggunakan loop for untuk mengulang sebanyak n kali
for i in range(n):
    # Menggunakan loop while untuk memastikan bilangan yang dihasilkan < 0.5
    bilangan_acak = random.random()
    while bilangan_acak >= 0.5:
        bilangan_acak = random.random()
    print(f"Bilangan acak ke-{i + 1}: {bilangan_acak:.4f}")

```
Penjelasan Kode Program:
1. Input: Meminta user memasukkan jumlah n
2. Inisialisasi: Variabel jumlah di-set ke 0 sebagai counter
3. Perulangan While:
- Loop berjalan selama jumlah < n
- Setiap iterasi menghasilkan angka acak antara 0-1 menggunakan random.random()
- Jika angka < 0.5, maka:
  - Angka dicetak
  - Counter jumlah bertambah 1
- Jika angka ≥ 0.5, loop terus berjalan tanpa mencetak dan tanpa menambah counter
  
## Hasil OUTPUT 
<img width="1918" height="548" alt="image" src="/img/While.png" />
