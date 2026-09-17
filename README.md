# Pertemuan 03 Seleksi Python

Nama: Herfi Maulidya
NIM: 2225250129
Kelas: 3A

## Tujuan

Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.

## Cara Menjalankan

python3 tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas

1. Masukkan koefisien a, b, dan c.
2. Periksa apakah a sama dengan 0.
3. Jika a sama dengan 0, tampilkan bahwa bukan persamaan kuadrat.
4. Jika a tidak sama dengan 0, hitung diskriminan D = b² - 4ac.
5. Jika D > 0, hitung dan tampilkan dua akar real.
6. Jika D = 0, hitung dan tampilkan satu akar real kembar.
7. Jika D < 0, tampilkan bahwa tidak ada akar real.

## Hasil Pengujian

| Input (a, b, c) | Keluaran yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|
| (1, -5, 6) | D = 1.00; x1 = 3.00, x2 = 2.00 | D = 1.00; x1 = 3.00, x2 = 2.00 | Lulus |
| (1, 2, 1) | D = 0.00; x = -1.00 | D = 0.00; x = -1.00 | Lulus |
| (1, 0, 1) | D = -4.00; tidak ada akar real | D = -4.00; tidak ada akar real | Lulus |
| (0, 2, 3) | Bukan persamaan kuadrat | Bukan persamaan kuadrat | Lulus |

## Refleksi

Saya belajar bahwa penggunaan kondisi if harus memperhatikan urutan dan batas kondisi agar setiap kasus dapat diproses dengan benar. Pada tugas persamaan kuadrat, kondisi a = 0 harus diperiksa terlebih dahulu sebelum menghitung diskriminan.