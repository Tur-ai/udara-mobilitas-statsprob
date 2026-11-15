# Jadwal 4 Minggu & Alur Kerja

> Hari di bawah adalah **usulan**. Sesuaikan dengan tanggal deadline dosen — hitung mundur dari tanggal pengumpulan lalu geser semua. **Sisakan minimal 3 hari terakhir** untuk laporan, poster, dan latihan presentasi.

## Ringkasan beban per peran per minggu
✅ = beban utama · ◻ = ringan (belajar/menyiapkan/mereview)

| Peran | M1 | M2 | M3 | M4 |
|---|---|---|---|---|
| 1 Project Lead | ✅ setup + rumusan masalah | ◻ koordinasi, cek progres | ◻ koordinasi | ✅ kesimpulan & rekomendasi |
| 2 Data Engineer | ✅ **pembersihan** | ◻ cek silang angka Peran 3 | ◻ cek silang angka Peran 3 | ◻ uji "jalankan dari nol" semua notebook |
| 3 Probability & Inference | ◻ belajar konsep, coba dengan draf | ✅ peluang, Normal, Binomial | ✅ CI + 3 uji hipotesis | ◻ bantu jelaskan ke Peran 6 |
| 4 Regression & Modeling | ◻ cek hasil Peran 2, mulai belajar & jalankan draf korelasi | ◻ lanjut persiapan | ◻ siap regresi | ✅ regresi final + asumsi |
| 5 Data Visualizer | ✅ tabel deskriptif + 3 grafik | ◻ siapkan palet/kerangka poster | ◻ pilih grafik untuk laporan | ✅ scatter + grafik poster + layout |
| 6 Technical Writer | ◻ draf latar belakang & metodologi | ✅ interpretasi Minggu 2 | ✅ interpretasi Minggu 3 | ✅ rekomendasi + naskah presentasi |

Peran 3 paling berat di Minggu 2–3, sedangkan Peran 4 paling berat di Minggu 4. Gunakan jeda Peran 4 di Minggu 1–3 untuk **membantu cek silang** (lihat "Buddy check" di bawah).

## Jadwal rinci

### Minggu 1 — Eksplorasi & pembersihan
| Hari | Siapa | Apa |
|---|---|---|
| 1 | Peran 1 | Buat repo, upload, ganti placeholder, undang anggota. Kumpul 30 menit (kick-off): pembagian peran, ketentuan, jadwal. |
| 1–2 | Semua | Baca ketentuan + panduan peran; jalankan `00_Kenalan_Dengan_Data`. |
| 2–4 | **Peran 2** | `01_Data_Engineer` → upload `data/Kelompok_12_data_bersih.csv` + hasil, **kabari grup**. |
| 2–5 | Peran 5 | `04_Data_Visualizer` bagian A–B (setelah data bersih tersedia; sebelumnya latihan dengan draf). |
| 2–5 | Peran 1 | Isi `reports/draft/01_latar_belakang_dan_rumusan_masalah.md`. |
| 4–6 | Peran 4 | **Buddy check** pembersihan Peran 2. |
| 5–6 | Peran 6 | Tulis `02_metodologi_pembersihan_data.md` dari log Peran 2. |
| 7 | Semua | Rapat 30 menit: review Minggu 1. |

### Minggu 2 — Probabilitas
| Hari | Siapa | Apa |
|---|---|---|
| 1–4 | Peran 3 | `02a_...` (A, B, C) + isi bagian ✏️ |
| 4–5 | Peran 2 | Cek silang 1–2 angka kunci (mis. P(Tidak Sehat \| Jam Sibuk) hitung manual di Excel). |
| 4–6 | Peran 6 | Isi bagian Minggu 2 di `03_interpretasi_hasil_per_uji.md`. |
| 7 | Semua | Rapat 30 menit. |

### Minggu 3 — Inferensi
| Hari | Siapa | Apa |
|---|---|---|
| 1–5 | Peran 3 | `02b_...` (CI, t-test, ANOVA, Chi-Square) |
| 4–6 | Peran 2 | Cek silang minimal 1 uji dengan alat lain (Excel Data Analysis / Jamovi). |
| 4–6 | Peran 6 | Interpretasi Minggu 3 (H0, H1, keputusan dalam bahasa awam). |
| 7 | Semua | Rapat 30 menit. |

### Minggu 4 — Regresi, rekomendasi, finalisasi
| Hari | Siapa | Apa |
|---|---|---|
| 1–3 | Peran 4 | `03_Regression_Modeling` selesai + interpretasi ✏️ |
| 1–3 | Peran 5 | scatter + grafik poster (`04_..` bagian C–D) |
| 3–4 | Peran 1 | Rumuskan **≥ 3 rekomendasi** di `04_kesimpulan_dan_rekomendasi.md` |
| 3–4 | Peran 6 | Haluskan rekomendasi; tulis naskah presentasi 5 menit |
| 4 | Peran 2 | Uji **"Restart & Run all"** pada semua notebook (reproducibility) |
| 5–7 | Semua | **Susun laporan PDF & poster** (menyusul — Peran 5 memimpin tata letak, Peran 6 memimpin teks), latihan Gallery Walk, isi halaman pengesahan & tanda tangan. |

## Buddy check (saling periksa)
Seperti *code review* di proyek open source: setiap hasil diperiksa orang lain sebelum dianggap final.

| Yang diperiksa | Pemeriksa | Cek apa |
|---|---|---|
| Pembersihan data (Peran 2) | Peran 4 | Keputusan punya alasan statistik? Jumlah baris di log = jumlah baris di file bersih? |
| Tabel & grafik deskriptif (Peran 5) | Peran 6 | Angka di grafik = angka di tabel? Judul sesuai kenyataan data? |
| Peluang & inferensi (Peran 3) | Peran 2 | Hitung ulang 1–2 angka dengan Excel/Jamovi; hasilnya sama? |
| Regresi (Peran 4) | Peran 3 | Persamaan, R², p-value sesuai ringkasan? Asumsi ditulis jujur? |
| Narasi & interpretasi (Peran 6) | Peran 3 | Istilah statistik benar (mis. tidak menulis "H0 diterima")? |
| Rekomendasi (Peran 1) | Peran 4 | Setiap rekomendasi punya **angka pendukung** dari hasil? |

Cara mencatat: tulis di `reports/draft/05_log_rapat_dan_review.md` ("Peran X sudah cek Y, hasil: sesuai / ada koreksi …").

## Siapa memiliki file apa (supaya tidak tabrakan)
| File / folder | Pemilik |
|---|---|
| `data/Kelompok_12_data_bersih.csv`, `notebooks/01_*`, dan di `outputs/`: `01_boxplot_sebelum`, `01_boxplot_sesudah`, `01_missing*`, `01_outlier*`, `01_perbandingan*`, `01_skala*`, `01_log*` | Peran 2 |
| `notebooks/02a_*`, `02b_*`, `outputs/*/02_*`, `outputs/*/03_*` | Peran 3 |
| `notebooks/03_*`, `outputs/*/04_korelasi*`, `04_regresi*`, `04_uji_asumsi*`, `04_vif*`, `04_asumsi*`, `04_heatmap*`, `04_persamaan*`, `04_perbandingan*` | Peran 4 |
| `notebooks/04_*`, `outputs/*/01_statistik*`, `01_histogram*`, `01_boxplot_per*`, `01_grouped*`, `01_frekuensi*`, `04_scatter*`, `04_poster*` | Peran 5 |
| `reports/draft/00_*`, `01_*`, `04_*`, `05_*` | Peran 1 |
| `reports/draft/02_*`, `03_*` | Peran 6 (dengan masukan Peran 2 & 3) |
| `README.md`, `docs/`, `src/helpers.py` | Peran 1 |

## Format rapat mingguan (30 menit)
1. (5 mnt) Tiap orang: *apa yang sudah selesai · apa yang macet · apa yang butuh dari siapa.*
2. (10 mnt) Review hasil minggu ini (tampilkan notebook/grafik).
3. (10 mnt) Keputusan yang perlu diambil bersama (mis. cara menangani outlier).
4. (5 mnt) Tugas minggu depan + siapa yang menunggu siapa.
Catat singkat di `reports/draft/05_log_rapat_dan_review.md`.

## Penamaan file hasil (sudah otomatis oleh notebook)
`<minggu>_<isi>.csv|png` — contoh `03_ttest_hasil.csv`, `04_scatter_tren.png`. Jangan ganti nama manual.
