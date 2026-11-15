# Ringkasan Ketentuan Proyek (dari PDF "Panduan Teknis Proyek Case-Based Learning")

Mata kuliah **Statistika dan Probabilitas** · Durasi **2 minggu** (PDF awal tertulis 4 minggu; mengikuti info terbaru 2 minggu. **Konfirmasi tanggal deadline ke dosen**) · Tim **5/6 orang** · Kelompok kita: **12 (Tema B)**.

## 1. Aturan umum
| Aturan | Artinya buat kita |
|---|---|
| **Dataset unik** | Hanya boleh memakai `Kelompok_12_Tema_B_Kualitas_Udara.csv`. Memakai dataset kelompok lain → **nilai proyek = 0**. |
| **Perangkat lunak** | Boleh Python/R/SPSS/Jamovi/Excel. Kita pakai **Python di Google Colab**. Skrip/file olahan **wajib dilampirkan**. |
| **Pembagian peran** | Setiap anggota memegang **1 peran utama** dan **menandatangani pernyataan kontribusi** di halaman pertama laporan (template: `reports/draft/00_halaman_pengesahan.md`). |

## 2. Luaran yang dikumpulkan
| # | Luaran | Ketentuan | Status di repo ini |
|---|---|---|---|
| 1 | **Laporan Teknis (PDF)** | maks **10 halaman**: ringkasan eksekutif, metodologi pembersihan data, hasil analisis Tahap 1–4, rekomendasi | ⏳ disusun belakangan (`reports/`) |
| 2 | **File kerja/kode** | `.ipynb` dst., harus **reproducible** (bisa dijalankan ulang) | ✅ notebook sudah disediakan |
| 3 | **Poster infografis** | 1 halaman A2 / rasio 16:9; **Gallery Walk 7 menit** = 5 menit paparan + 2 menit tanya-jawab (dosen & peer-reviewer) | ⏳ disusun belakangan (`poster/`) |

## 3. Checklist analisis wajib → siapa yang mengerjakan

### Tahap 1 — Eksplorasi & pembersihan data
| Item dari dosen | Penanggung jawab | Di mana |
|---|---|---|
| a. Skala pengukuran semua kolom (Nominal/Ordinal/Interval/Rasio) | Peran 2 | `01_Data_Engineer` |
| b. Jumlah missing values + penanganan beralasan | Peran 2 | `01_Data_Engineer` |
| c. Outlier pagar IQR (Q1 − 1.5·IQR, Q3 + 1.5·IQR) + **boxplot sebelum & sesudah** | Peran 2 | `01_Data_Engineer` |
| d. Tabel deskriptif (Mean, Median, Modus, Std, Varians, IQR, Skewness) + **≥ 3 grafik** (Histogram, Boxplot, Grouped Bar) | Peran 5 | `04_Data_Visualizer` |

### Tahap 2 — Pemodelan probabilitas
| Item | Penanggung jawab | Di mana |
|---|---|---|
| a. Peluang empiris ≥ 3 kejadian, ≥ 2 di antaranya bersyarat P(A\|B) | Peran 3 | `02a_...` bagian A |
| b. 1 variabel kontinu vs Distribusi Normal (μ, σ sampel) + peluang 2 skenario batas | Peran 3 | `02a_...` bagian B |
| c. 1 variabel biner → proporsi p → Binomial n = 20: P(X = k) dan P(X ≥ k) | Peran 3 | `02a_...` bagian C |

### Tahap 3 — Inferensi (α = 0.05)
| Item | Penanggung jawab | Di mana |
|---|---|---|
| a. CI 95% rata-rata populasi variabel utama **dan** CI proporsi salah satu kategori | Peran 3 | `02b_...` bagian A |
| b1. Two-sample independent t-test | Peran 3 | `02b_...` bagian B |
| b2. One-Way ANOVA (+ Tukey jika signifikan) | Peran 3 | `02b_...` bagian C |
| b3. Chi-Square independensi (tabel kontingensi observasi vs ekspektasi) | Peran 3 | `02b_...` bagian D |
| *Tiap uji wajib: H0, H1, statistik uji, p-value, keputusan, interpretasi bahasa sehari-hari* | Peran 3 (angka) + Peran 6 (bahasa) | notebook + `reports/draft/03_...` |

### Tahap 4 — Korelasi, regresi & rekomendasi
| Item | Penanggung jawab | Di mana |
|---|---|---|
| a. Matriks korelasi Pearson semua variabel numerik + **scatter plot + garis tren** | Peran 4 (matriks) + Peran 5 (scatter) | `03_...` bagian A, `04_...` bagian C |
| b. Regresi linear berganda + persamaan ŷ = b0 + b1x1 + b2x2 | Peran 4 | `03_...` bagian B |
| c. R², Adjusted R², Uji-F, Uji-t tiap prediktor | Peran 4 | `03_...` bagian C |
| d. Asumsi residual: histogram/Q-Q (normalitas), fitted vs residual (homoskedastisitas) | Peran 4 | `03_...` bagian D |
| e. **Minimal 3 rekomendasi keputusan konkret** berbasis temuan | Peran 1 (rumus) + Peran 6 (bahasa) | `reports/draft/04_...` |

## 4. Peran resmi (sesuai dosen)
1. Project Lead — perumusan masalah & kesimpulan strategis
2. Data Engineer — pembersihan missing values & penanganan outlier
3. Probability & Inference Analyst — peluang bersyarat, distribusi, CI & uji hipotesis
4. Regression & Modeling Analyst — korelasi, model regresi & uji asumsi residual
5. Data Visualizer & Editor — visualisasi grafik, laporan teknis & poster infografis
6. Technical Writer & Presentation Lead — menerjemahkan hasil uji statistik menjadi bahan kebijakan/bisnis

> Catatan: beberapa item (mis. "tabel deskriptif") bisa dibaca masuk ke lebih dari satu peran di panduan dosen. Pembagian di atas adalah **keputusan tim** supaya beban merata; boleh disesuaikan asal tercatat di notulen rapat dan tercermin jujur di persentase kontribusi pada halaman pengesahan.
