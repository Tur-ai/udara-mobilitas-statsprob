# PERAN 2 — Data Engineer
*(Pembersihan missing values & penanganan outlier)*

## Kamu di proyek ini
Kamu **koki persiapan**: sebelum chef (analis) memasak, kamu mencuci, memilah, dan membuang bagian yang rusak. Kalau datanya kotor, semua hasil teman-temanmu ikut salah. Pekerjaanmu juga yang **paling ditunggu** orang lain — **targetnya selesai paling lambat Hari 3** dari 14 hari (idealnya Hari 2).

## Hasil akhir yang harus kamu serahkan
| File | Untuk siapa |
|---|---|
| `data/Kelompok_12_data_bersih.csv` ← **paling penting** | semua orang |
| `outputs/tables/01_skala_pengukuran.csv` | laporan |
| `outputs/tables/01_missing_values.csv` | laporan |
| `outputs/tables/01_outlier_iqr.csv` | laporan |
| `outputs/tables/01_perbandingan_sebelum_sesudah.csv` | laporan |
| `outputs/tables/01_log_pembersihan.txt` | Peran 6 (metodologi) |
| `outputs/figures/01_boxplot_sebelum.png`, `01_boxplot_sesudah.png` | laporan, poster |
| `notebooks/01_Data_Engineer.ipynb` (sudah terisi alasan keputusan) | file kerja yang dikumpulkan |

## Langkah demi langkah

### Tahap 1
1. Buka & jalankan `00_Kenalan_Dengan_Data` (10 menit). Pahami arti tiap kolom.
2. Buka `01_Data_Engineer` di Colab. Jalankan **satu sel per satu**. Setelah tiap sel, tanyakan ke diri sendiri: *"apa yang baru saja terjadi pada datanya?"*
3. **Skala pengukuran:** baca tabel usulan & alasannya. Pastikan kamu bisa menjelaskan kenapa suhu = **interval** sementara volume kendaraan = **rasio**.
4. **Missing values:** lihat berapa dan di baris mana. Putuskan: hapus atau isi? **Tulis alasannya** di sel ✏️ (jangan kosong).
5. **Cek konsistensi** `Status_Udara` vs `Indeks_PM25` — ini jebakan yang tidak diminta dosen tapi sangat penting.
6. **Outlier IQR:** baca tabel batas; lihat boxplot *sebelum*; putuskan per variabel: biarkan / winsorize / hapus; tulis alasannya.
7. Jalankan sel simpan (data bersih + log) dan sel `unduh_hasil`.
8. **Upload ke GitHub** (lihat `docs/02_panduan_github_colab.md` Bagian 5): seret folder `data` dan `outputs` hasil unzip. Simpan juga notebook-nya (Bagian 6).
9. **Kabari grup:** "Data bersih sudah ada di GitHub, semua mulai sesi baru & jalankan ulang."
10. Kirim ke Peran 6: isi `outputs/tables/01_log_pembersihan.txt` + alasan keputusanmu.

### Tahap 2–3 (buddy check Peran 3)
11. Ambil **1–2 angka kunci** dari hasil Peran 3 dan hitung ulang di **Excel** (lihat resep di bawah). Kalau cocok → catat "sesuai" di log rapat. Kalau tidak → diskusikan, jangan langsung menyalahkan.

### Tahap 4 (uji reproducibility)
12. Buka tiap notebook di sesi Colab baru → *Runtime → Restart session and run all*. Catat notebook mana yang error. Laporkan ke pemiliknya.

## Konsep yang harus kamu pahami
**Skala pengukuran** (urutan: Nominal < Ordinal < Interval < Rasio). Kuncinya: *nol sungguhan?* (rasio) *jarak sama?* (interval) *ada urutan?* (ordinal) *hanya nama?* (nominal).

**Missing value:** sel kosong. Pilihan penanganan dan kapan dipakai:
| Opsi | Cocok jika | Risiko |
|---|---|---|
| Hapus baris | sedikit (<5%), acak, atau di variabel respons | kehilangan data |
| Isi mean | data simetris, tanpa outlier | mean tertarik outlier |
| Isi median | data miring / ada outlier | variasi data mengecil sedikit |

*Kenapa PM2.5 kosong sebaiknya dihapus, bukan diisi?* Karena PM2.5 adalah variabel yang kita teliti & prediksi. Mengisinya dengan "tebakan" berarti kita memasukkan angka buatan ke variabel utama.

**Outlier & aturan pagar IQR:** Q1 = 25% data di bawahnya, Q3 = 75%, IQR = Q3 − Q1. Pagar: `Q1 − 1.5×IQR` dan `Q3 + 1.5×IQR`. Di luar pagar = *dicurigai* outlier.
**Pertanyaan kunci:** outlier ini **salah input** (buang/koreksi) atau **kejadian nyata yang jarang** (jangan dibuang seenaknya; boleh winsorize atau dibiarkan)?
- **Winsorizing:** nilai ekstrem dipotong ke batas pagar → ukuran data tetap, pengaruh ekstrem berkurang.

## Resep Excel untuk buddy check (dipakai juga oleh peran lain)
| Mau menghitung | Rumus Excel |
|---|---|
| Rata-rata kolom H | `=AVERAGE(H2:H351)` |
| Median / simpangan baku | `=MEDIAN(H2:H351)` · `=STDEV.S(H2:H351)` |
| Q1 / Q3 | `=QUARTILE.INC(H2:H351,1)` · `=QUARTILE.INC(H2:H351,3)` |
| Jumlah baris Jam Sibuk = "Ya" | `=COUNTIF(D2:D351,"Ya")` |
| P(Tidak Sehat \| Jam Sibuk) | `=COUNTIFS(D2:D351,"Ya",I2:I351,"Tidak Sehat")/COUNTIF(D2:D351,"Ya")` |
| Uji-t | tab *Data* → *Data Analysis* → *t-Test: Two-Sample Assuming Equal Variances* (aktifkan add-in Analysis ToolPak bila belum muncul) |
*(Sesuaikan huruf kolom dengan file; gunakan file bersih.)*

## Kesalahan umum
- **Mengubah file data asli.** Selalu simpan ke file baru.
- Menghapus outlier "supaya cantik" tanpa alasan.
- Mengisi missing di variabel respons dengan mean.
- Mengulang-ulang penghapusan outlier sampai tidak ada lagi (praktik buruk — outlier baru akan muncul terus).
- Mengubah `Kelompok_12_data_bersih.csv` **setelah** teman-teman mulai memakainya tanpa memberi tahu. Kalau terpaksa mengubah: kabari grup, catat di log, semua jalankan ulang.
- Lupa upload ke GitHub.

## Pertanyaan yang mungkin ditanya dosen
1. Kenapa baris PM2.5 yang kosong dihapus tetapi kecepatan angin diisi median?
2. Apa bedanya outlier dan kesalahan input? Bagaimana kamu membedakannya di data ini?
3. Kenapa memakai median dan bukan mean untuk imputasi?
4. Apa yang terjadi pada hasil analisis kalau outlier dibiarkan?
5. Apa skala pengukuran suhu, dan kenapa bukan rasio?

## Kerja sama
- **Memberi ke:** semua (data bersih), Peran 6 (log metodologi).
- **Menerima dari:** — (kamu titik awal).
- **Diperiksa oleh:** Peran 4. **Memeriksa:** Peran 3 (Tahap 2–3) dan uji reproducibility (Tahap 4).

## ✅ Checklist
- [ ] Skala 9 kolom + alasan
- [ ] Jumlah missing + keputusan beralasan (ditulis sendiri di notebook)
- [ ] Tabel IQR + boxplot sebelum & sesudah
- [ ] `Kelompok_12_data_bersih.csv` di GitHub dan grup sudah dikabari
- [ ] Log pembersihan diberikan ke Peran 6
- [ ] Notebook tersimpan ke GitHub
- [ ] Buddy check Peran 3 (angka cocok) tercatat
- [ ] Uji "Restart & Run all" semua notebook (Tahap 4)
