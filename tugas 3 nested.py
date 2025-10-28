
for i in range(1, 10):
    # Perulangan dalam (inner loop) untuk kolom
    for j in range(1, 10):
        # Menghitung hasil perkalian
        hasil = i + j
        # Mencetak hasil dengan format rata kanan
        print(f"{hasil:>4}", end="")
    
    # Pindah ke baris baru setelah perulangan dalam selesai
    print()
