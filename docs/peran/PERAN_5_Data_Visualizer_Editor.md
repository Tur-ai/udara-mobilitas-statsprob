# PERAN 5 — Data Visualizer & Editor
*(Visualisasi grafik, laporan teknis & poster infografis)*

## Kamu di proyek ini
Kamu **penerjemah visual**. Angka yang benar tapi sulit dibaca tidak akan sampai ke dosen dan peer-reviewer. Kamu membuat grafik yang bisa dipahami dalam 5 detik, dan kelak memimpin **tata letak laporan PDF (maks 10 halaman)** dan **poster** (bagian laporan & poster dikerjakan belakangan, menunggu arahan tim).

## Hasil akhir yang harus kamu serahkan
| Minggu | File | Isi |
|---|---|---|
| 1 | `notebooks/04_Data_Visualizer.ipynb` | tabel deskriptif + 3 grafik wajib |
| 1 | `outputs/tables/01_statistik_deskriptif.csv`, `01_frekuensi_kategori.csv` | tabel |
| 1 | `outputs/figures/01_histogram_numerik.png`, `01_boxplot_per_kelompok.png`, `01_grouped_bar_status_zona.png`, `01_grouped_bar_status_jamsibuk.png` | grafik |
| 4 | `outputs/figures/04_scatter_tren.png`, `04_scatter_volume_per_zona.png` | scatter + garis tren |
| 4 | `outputs/figures/04_poster_*.png` | grafik siap poster |
| 4+ | Laporan PDF & poster | (menyusul) |

## Langkah demi langkah

### Minggu 1
1. Jalankan `00_Kenalan_Dengan_Data`; buka `04_Data_Visualizer`. Sambil menunggu data bersih resmi, jalankan dengan draf untuk memahami alurnya.
2. Setelah data bersih resmi ada: mulai sesi baru & jalankan ulang.
3. **Bagian A (tabel deskriptif):** baca arti tiap ukuran. Perhatikan catatan ⚠️ soal **modus** pada variabel kontinu.
4. **Bagian B (3 grafik):** histogram, boxplot, grouped bar chart. Untuk tiap grafik tulis **satu kalimat pesan utama** (✏️) — itu calon judul/caption.
5. Upload hasil + simpan notebook. Minta **Peran 6** memeriksa angka & judul (buddy check).

### Minggu 2–3 (ringan)
6. Tentukan **palet warna & gaya** yang konsisten (sudah ada di `WARNA_STATUS`, `WARNA_ZONA`; jangan ganti-ganti).
7. Lihat grafik dari Peran 3 (`outputs/figures/02_*`, `03_*`) dan Peran 4. **Pilih** mana yang masuk laporan — ingat batas **10 halaman**; lebih baik 8–10 grafik terbaik daripada 25 grafik.
8. Buat **kerangka halaman laporan** (kosong) dan **sketsa poster** di kertas / Canva / PowerPoint: judul, 3 pesan utama, alur baca (kiri-atas → kanan-bawah).

### Minggu 4
9. **Bagian C (scatter + garis tren)** — pastikan r sama dengan tabel Peran 4.
10. **Bagian D (grafik poster):** cek tiap judul grafik sesuai kenyataan angka. Ubah kalimatnya bila perlu.
11. **Laporan & poster** (menyusul): Peran 5 memimpin tata letak; Peran 6 memimpin teks; Peran 1 memastikan pesan utama.

## Konsep yang harus kamu pahami

**Memilih jenis grafik**
| Pertanyaan | Grafik |
|---|---|
| Bagaimana sebaran satu variabel angka? | Histogram |
| Bandingkan sebaran antar kelompok? | Boxplot (atau violin) |
| Bandingkan hitungan/proporsi antar kategori? | Grouped / stacked bar chart |
| Hubungan dua variabel angka? | Scatter plot + garis tren |
| Perbandingan rata-rata + ketidakpastian? | Bar/dot chart dengan error bar (CI) |

**Cara membaca boxplot:** kotak = Q1–Q3 (50% data tengah); garis tengah = median; kumis = jangkauan wajar (sampai batas pagar IQR); titik = outlier.

**Prinsip desain:** satu grafik = satu pesan · judul berupa kesimpulan · sumbu berlabel + satuan · warna konsisten · hilangkan elemen tak perlu · font cukup besar untuk poster (≥ 14 pt di grafik) · hindari 3D & warna pelangi.
**Warna dan aksesibilitas:** jangan memakai hanya merah-hijau untuk membedakan sesuatu yang penting; pakai juga label angka.

## Kesalahan umum
- Sumbu y dipotong (tidak mulai dari 0 untuk bar chart) sehingga selisih tampak berlebihan.
- Judul yang tidak sesuai data (mis. "hampir semua … ") — **selalu cek ke angka**.
- Terlalu banyak grafik, terlalu sedikit pesan.
- Warna berubah-ubah antar grafik untuk kategori yang sama.
- Menempel gambar buram (selalu pakai png hasil notebook, `dpi=200`).
- Membaca modus variabel kontinu apa adanya.

## Pertanyaan yang mungkin ditanya dosen
1. Kenapa memilih jenis grafik ini untuk pertanyaan ini?
2. Apa yang ditunjukkan boxplot ini? Apa arti titik di luar kumis?
3. Dari tabel deskriptif, apa arti mean ≠ median? Apa arti skewness positif?
4. Apa arti garis tren pada scatter plot dan angka r?
5. Pesan utama poster kalian apa?

## Kerja sama
- **Menunggu dari:** Peran 2 (data bersih), Peran 3 & 4 (angka untuk grafik tambahan).
- **Memberi ke:** Peran 6 (grafik + caption), Peran 1 (pesan utama poster).
- **Diperiksa oleh:** Peran 6.

## ✅ Checklist
- [ ] Tabel deskriptif lengkap (7 ukuran) + frekuensi kategori
- [ ] Histogram, boxplot, grouped bar chart + pesan utama tiap grafik
- [ ] Scatter + garis tren (r sama dengan Peran 4)
- [ ] Grafik poster dicek ke angka
- [ ] Hasil & notebook di GitHub
- [ ] Palet warna konsisten di semua gambar
