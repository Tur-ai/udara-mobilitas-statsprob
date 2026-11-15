# Jadwal 2 Minggu (14 Hari) & Alur Kerja

> Waktu pengerjaan hanya **2 minggu**, jadi pekerjaan harus **berjalan paralel**. Hari di bawah adalah usulan: **hitung mundur dari tanggal deadline dosen** (Hari 14 = hari pengumpulan / Gallery Walk), lalu geser semuanya. **Sisakan minimal 3 hari terakhir** untuk laporan, poster, dan latihan presentasi.

## Istilah: "Tahap" bukan "Minggu"
Checklist dosen membagi analisis menjadi 4 bagian (dulu bernama Minggu 1–4). Karena waktunya sekarang 2 minggu, bagian itu kita sebut **Tahap 1–4**:

| Tahap | Isi | Siapa utama | Hari |
|---|---|---|---|
| **1** | Eksplorasi & pembersihan data | Peran 2 (data), Peran 5 (grafik deskriptif) | **1–3** |
| **2** | Pemodelan probabilitas | Peran 3 (`02a`) | **3–6** |
| **3** | Inferensi: CI + 3 uji hipotesis | Peran 3 (`02b`) | **5–9** |
| **4** | Korelasi, regresi, rekomendasi | Peran 4 (regresi), Peran 1 & 6 (rekomendasi) | **4–10** |
| Final | Laporan PDF + poster + latihan Gallery Walk | semua | **11–14** |

**Kunci kecepatan:** Tahap 4 (regresi) **tidak bergantung** pada Tahap 2–3, hanya butuh data bersih. Jadi Peran 4 mulai begitu data bersih ada (Hari ~3), **bukan** menunggu Peran 3 selesai.
**Titik kritis:** Peran 2 harus mengunggah data bersih paling lambat **Hari 3** (idealnya Hari 2). Semua orang menunggunya.

## Beban per peran (✅ utama · ◻ ringan/membantu)
| Peran | Hari 1–3 | Hari 4–7 | Hari 8–10 | Hari 11–14 |
|---|---|---|---|---|
| 1 Project Lead | ✅ setup + rumusan masalah | ◻ koordinasi | ✅ kesimpulan & rekomendasi | ✅ finalisasi laporan, pengesahan |
| 2 Data Engineer | ✅ **pembersihan data** | ◻ cek silang Peran 3 | ◻ uji "Run all" semua notebook | ◻ bantu laporan/poster |
| 3 Probability & Inference | ◻ belajar, coba dengan draf | ✅ `02a` lalu mulai `02b` | ✅ selesaikan `02b` | ◻ bantu jelaskan ke Peran 6 |
| 4 Regression & Modeling | ◻ cek Peran 2, belajar | ✅ `03` regresi | ✅ finalisasi + asumsi | ◻ bantu laporan |
| 5 Data Visualizer | ✅ tabel & grafik deskriptif | ✅ scatter + grafik poster | ◻ pilih grafik laporan | ✅ tata letak laporan & poster |
| 6 Technical Writer | ◻ draf latar belakang & metodologi | ✅ interpretasi Tahap 2–3 | ✅ interpretasi regresi + rekomendasi | ✅ teks laporan, naskah presentasi |

## Jadwal rinci

| Hari | Siapa | Apa |
|---|---|---|
| **1** | Peran 1 | Cek repo & kolaborator; kirim pesan ke grup; **rapat kick-off 30 menit** (peran, jadwal, jam rapat). |
| **1–2** | Semua | Baca ketentuan + panduan peran; jalankan `00_Kenalan_Dengan_Data`; simpan salinan notebook ke Drive masing-masing. |
| **1–3** | **Peran 2** | `01_Data_Engineer` → upload `data/Kelompok_12_data_bersih.csv` + hasil, **kabari grup**. |
| 1–3 | Peran 1 | Isi `reports/draft/01_latar_belakang_dan_rumusan_masalah.md`. |
| 3–4 | Peran 5 | `04_Data_Visualizer` bagian A–B (tabel deskriptif + 3 grafik). |
| 3–4 | Peran 4 | **Buddy check** pembersihan Peran 2 → lalu mulai `03_Regression_Modeling` dengan data bersih. |
| 3–4 | Peran 6 | `02_metodologi_pembersihan_data.md` dari log Peran 2. |
| **4** | Semua | **Rapat 20 menit** (cek progres Tahap 1). |
| 3–6 | Peran 3 | `02a` (peluang, Normal, Binomial). |
| 5–6 | Peran 2 | Cek silang 1–2 angka Peran 3 di Excel. |
| 5–9 | Peran 3 | `02b` (CI, t-test, ANOVA+Tukey, Chi-Square). |
| 4–8 | Peran 4 | Regresi, interpretasi, asumsi residual. |
| 5–8 | Peran 5 | Scatter + grafik poster (bagian C–D). |
| 6–9 | Peran 6 | Isi `03_interpretasi_hasil_per_uji.md` begitu hasil masuk. |
| **8** | Semua | **Rapat 20 menit** (cek Tahap 2–4). |
| 8–9 | Peran 2 | Cek silang 1 uji dari `02b` (Excel/Jamovi). |
| 8–10 | Peran 1 | Rumuskan **≥ 3 rekomendasi** (`04_kesimpulan_dan_rekomendasi.md`). |
| 9–10 | Peran 6 | Haluskan rekomendasi; tulis naskah presentasi 5 menit. |
| 10 | Peran 2 | Uji **"Restart & Run all"** semua notebook (reproducibility). |
| **11–14** | Semua | **Susun laporan PDF & poster** (menyusul): Peran 5 tata letak, Peran 6 teks, Peran 1 pesan utama. Latihan Gallery Walk minimal 3×. Isi halaman pengesahan & tanda tangan. |
| **12** | Semua | **Rapat 30 menit**: review draf laporan & poster. |
| **14** | — | Pengumpulan / Gallery Walk. |

## Aturan percepatan (karena waktu sempit)
1. **Jangan menunggu sempurna.** Kerjakan dengan data draf dulu; ganti ke data resmi begitu ada.
2. **Kabari grup begitu selesai** satu hasil — orang lain sedang menunggu.
3. **Macet lebih dari 3 jam? Langsung tanya.** Jangan diam sehari.
4. Peran 3 paling berat: Peran 2 dan Peran 4 yang lebih ringan di Hari 4–7 **wajib siap membantu** (cek silang, siapkan ringkasan).
5. Rapat singkat tiap 3–4 hari, bukan mingguan.

## Buddy check (saling periksa)
| Yang diperiksa | Pemeriksa | Cek apa |
|---|---|---|
| Pembersihan data (Peran 2) | Peran 4 | Keputusan punya alasan? Jumlah baris di log = di file bersih? |
| Tabel & grafik deskriptif (Peran 5) | Peran 6 | Angka grafik = angka tabel? Judul sesuai kenyataan? |
| Peluang & inferensi (Peran 3) | Peran 2 | Hitung ulang 1–2 angka dengan Excel/Jamovi; sama? |
| Regresi (Peran 4) | Peran 3 | Persamaan, R², p-value sesuai ringkasan? Asumsi ditulis jujur? |
| Narasi & interpretasi (Peran 6) | Peran 3 | Istilah statistik benar (tidak menulis "H0 diterima")? |
| Rekomendasi (Peran 1) | Peran 4 | Tiap rekomendasi punya **angka pendukung**? |

Catat di `reports/draft/05_log_rapat_dan_review.md`.

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

## Format rapat singkat (20–30 menit)
1. (5 mnt) Tiap orang: *sudah selesai apa · macet di mana · butuh apa dari siapa.*
2. (10 mnt) Review hasil (tampilkan notebook/grafik).
3. (5 mnt) Keputusan bersama yang tertunda (mis. cara menangani outlier).
4. (5 mnt) Tugas sampai rapat berikutnya + siapa menunggu siapa.

## Penamaan file hasil (otomatis oleh notebook)
`<tahap>_<isi>.csv|png` — contoh `03_ttest_hasil.csv`, `04_scatter_tren.png`. Jangan ganti nama manual.
