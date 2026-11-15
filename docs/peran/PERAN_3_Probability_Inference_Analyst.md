# PERAN 3 — Probability & Inference Analyst
*(Peluang bersyarat, distribusi, CI & uji hipotesis)*

## Kamu di proyek ini
Kamu **detektif statistik**. Kamu menjawab "seberapa mungkin?" dan "apakah perbedaan ini nyata atau cuma kebetulan?". Beban kerjamu paling berat di **Tahap 2–3**, jadi **mulailah belajar dari Tahap 1** (data draf sudah bisa dipakai berlatih).

## Hasil akhir yang harus kamu serahkan
| Tahap | File | Isi |
|---|---|---|
| 2 | `notebooks/02a_Probability_Peluang_Distribusi.ipynb` | peluang empiris, Normal, Binomial |
| 2 | `outputs/tables/02_*.csv`, `outputs/figures/02_*.png` | tabel & gambar |
| 3 | `notebooks/02b_Inference_Uji_Hipotesis.ipynb` | CI, t-test, ANOVA+Tukey, Chi-Square |
| 3 | `outputs/tables/03_*.csv`, `outputs/figures/03_*.png` | tabel & gambar |
| 3 | `outputs/tables/03_ringkasan_uji_hipotesis.csv` | ringkasan untuk Peran 1 & 6 |

## Langkah demi langkah

### Tahap 1 — Belajar (jangan dilewatkan)
1. Jalankan `00_Kenalan_Dengan_Data`.
2. Pelajari konsep di bagian "Konsep" di bawah. Targetnya: bisa menjelaskan **p-value**, **H0/H1**, dan **peluang bersyarat** ke teman dengan kata-kata sendiri.
3. Buka `02a` dan `02b`, jalankan dengan data draf (akan muncul peringatan DRAF) untuk melihat alurnya. Belum perlu menulis interpretasi.

### Tahap 2 — `02a` (setelah data bersih resmi ada)
4. Mulai sesi Colab baru; jalankan SETUP; pastikan tertulis **DATA BERSIH RESMI**.
5. **Bagian A (peluang):** jalankan; ganti/tambah kejadian sesuai pikiranmu (≥ 3 peluang, ≥ 2 bersyarat). Tulis interpretasi ✏️.
6. **Bagian B (Normal):** lihat histogram, Q-Q plot, Shapiro. Tulis kesimpulan: *cukup normal atau tidak, dan kenapa.* Hitung 2 skenario (default: P(>65) dan P(≤35)) dan bandingkan dengan proporsi sebenarnya.
7. **Bagian C (Binomial):** pahami kenapa n = 20 dan "sukses" = Tidak Sehat. Isi interpretasi.
8. Jalankan `unduh_hasil`, upload ke GitHub, simpan notebook, kabari Peran 6 & Peran 2 (untuk cek silang).

### Tahap 3 — `02b`
9. **CI** (A): paham rumus; tulis interpretasi. 
10. **t-test, ANOVA, Chi-Square** (B, C, D): untuk **tiap** uji isi tabel ✏️: H0, H1, statistik, p-value, keputusan, interpretasi sehari-hari.
11. Jika ANOVA signifikan, baca hasil **Tukey** pasangan per pasangan.
12. Upload, kabari. Kirim `03_ringkasan_uji_hipotesis.csv` ke Peran 6 dan Peran 1.
13. Tahap 4: duduk bersama Peran 6 satu sesi untuk menjelaskan hasil agar tidak salah terjemah.

## Konsep yang harus kamu pahami

**Peluang empiris** = jumlah kejadian ÷ total. **Peluang bersyarat** P(A | B) = "peluang A jika B sudah terjadi" = jumlah (A dan B) ÷ jumlah B. *Contoh:* dari semua pengukuran saat jam sibuk, berapa persen yang Tidak Sehat?
**P(A|B) ≠ P(B|A).**

**Distribusi Normal:** lonceng simetris dengan pusat μ dan lebar σ. **Skor Z** = (x − μ)/σ = "berapa simpangan baku dari rata-rata". Aturan 68–95–99.7.

**Binomial:** n percobaan identik & independen, hasil sukses/gagal, peluang sukses p tetap. X = jumlah sukses. P(X = k) = C(n,k) p^k (1−p)^(n−k). Rata-rata = np.

**Confidence Interval 95%:** rentang yang jika prosedurnya diulang terus, 95% darinya akan memuat nilai populasi. Cara bicara aman: *"Kami 95% yakin nilai sebenarnya di antara A dan B."* **Bukan** "peluang nilai sebenarnya ada di rentang ini 95%."

**Uji hipotesis (resep):**
1. H0 = tidak ada beda/hubungan · H1 = ada.
2. Hitung statistik uji & **p-value**.
3. p-value = peluang mendapat hasil sekuat ini **jika H0 benar**.
4. p < 0.05 → **tolak H0**; p ≥ 0.05 → **gagal tolak H0**.

| Uji | Dipakai untuk | Statistik | Asumsi penting |
|---|---|---|---|
| t independen | bandingkan 2 rata-rata | t | independen; (kira-kira) normal; varians sama → Student, beda → Welch (Levene) |
| ANOVA | bandingkan ≥ 3 rata-rata | F | normal; varians sama; independen |
| Tukey | pasangan mana yang beda setelah ANOVA signifikan | — | — |
| Chi-Square | hubungan 2 variabel kategori | χ² | ekspektasi tiap sel ≥ 5 |

**Kenapa tidak 3× uji-t?** Tiap uji punya risiko salah 5%; diulang, risiko totalnya naik. ANOVA + Tukey menjaga risiko total tetap 5%.
**Signifikan ≠ penting:** lihat juga **ukuran efek** (Cohen's d, eta², Cramér's V) dan besar selisih.

### Contoh kerangka kalimat interpretasi
- Uji-t signifikan: *"Rata-rata PM2.5 pada hari kerja (… ) lebih tinggi dibanding akhir pekan (… ), selisih sekitar … poin. Perbedaan ini kuat dan bukan kebetulan (p < 0.05)."*
- Tidak signifikan: *"Tidak ada bukti yang cukup bahwa … berbeda (p = …). Bukan berarti pasti sama, hanya saja data kita belum menunjukkan beda yang meyakinkan."*

## Kesalahan umum
- Menulis **"H0 diterima"** → yang benar **"gagal menolak H0"**.
- Mengira **p-value = peluang H0 benar**. Bukan.
- Menulis p = 0.000 → tulis **p < 0.001**.
- Memakai uji-t berkali-kali untuk 3 kelompok.
- Lupa memeriksa syarat (ekspektasi ≥ 5 pada Chi-Square, Levene pada t-test).
- Menyimpulkan "ada hubungan sebab-akibat" dari Chi-Square/uji-t.
- Menjalankan notebook dengan data draf lalu mengumpulkannya sebagai hasil final.
- Menyalin interpretasi tanpa memahami.

## Pertanyaan yang mungkin ditanya dosen
1. Apa arti p-value = 0.03 dalam bahasa sehari-hari?
2. Kenapa kalian memakai Welch/Student? Apa hasil Levene?
3. Kenapa ANOVA, bukan beberapa kali uji-t? Apa fungsi Tukey?
4. Apa arti P(Tidak Sehat | Jam Sibuk) dan apa bedanya dengan P(Jam Sibuk | Tidak Sehat)?
5. Apakah PM2.5 benar-benar berdistribusi normal? Apa buktinya? Apa dampaknya pada hasil?
6. Kenapa model binomial hanya pendekatan untuk data ini?
7. Bagaimana cara membaca CI 95%?

## Kerja sama
- **Menunggu dari:** Peran 2 (data bersih).
- **Memberi ke:** Peran 6 (ringkasan & penjelasan), Peran 1 (temuan), Peran 5 (grafik).
- **Diperiksa oleh:** Peran 2 (cek silang di Excel). **Memeriksa:** Peran 4 (asumsi regresi) & Peran 6 (istilah).

## ✅ Checklist
- [ ] ≥ 3 peluang empiris, ≥ 2 bersyarat + interpretasi
- [ ] Normal: uji kecocokan + 2 skenario + interpretasi
- [ ] Binomial n = 20: P(X = k), P(X ≥ k) + interpretasi
- [ ] CI 95% mean **dan** CI proporsi
- [ ] t-test, ANOVA (+Tukey), Chi-Square: H0, H1, statistik, p, keputusan, interpretasi
- [ ] Hasil & notebook di GitHub; Peran 2 sudah cek silang
- [ ] Bisa menjelaskan semuanya tanpa membaca
