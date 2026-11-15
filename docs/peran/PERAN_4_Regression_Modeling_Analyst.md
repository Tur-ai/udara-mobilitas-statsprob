# PERAN 4 — Regression & Modeling Analyst
*(Korelasi, model regresi & uji asumsi residual)*

## Kamu di proyek ini
Kamu **pembuat model prediksi**. Kamu menjawab: *"Kalau volume kendaraan naik/ angin melemah, seberapa besar PM2.5 ikut berubah — dan seberapa bisa model ini dipercaya?"*
Ini bagian yang paling mirip "membuat model AI": regresi linear adalah bentuk paling dasar *machine learning* — komputer belajar pola dari data lalu dipakai untuk memprediksi. Bedanya, di sini kita juga wajib **menguji apakah modelnya layak dipercaya** (uji asumsi), bukan hanya melihat akurasi.

Beban terberatmu di **Tahap 4 (Hari ~4–10)**. Regresi **tidak menunggu** Peran 3: begitu data bersih resmi ada (Hari ~3), kamu langsung mulai. Di Tahap 1 kamu lebih ringan, jadi manfaatkan untuk **belajar** dan **memeriksa pekerjaan orang lain** (buddy check).

## Hasil akhir yang harus kamu serahkan
| File | Isi |
|---|---|
| `notebooks/03_Regression_Modeling.ipynb` | notebook lengkap dengan ✏️ terisi |
| `outputs/tables/04_korelasi_pearson.csv`, `04_korelasi_pvalue.csv`, `outputs/figures/04_heatmap_korelasi.png` | matriks korelasi |
| `outputs/tables/04_regresi_koefisien.csv`, `04_regresi_ringkasan.csv`, `04_persamaan_regresi.txt` | persamaan, R², Adj R², F, t |
| `outputs/tables/04_uji_asumsi.csv`, `04_vif.csv`, `outputs/figures/04_asumsi_residual.png` | pemeriksaan asumsi |
| `outputs/tables/04_regresi_skenario_prediksi.csv` | "what-if" untuk rekomendasi Peran 1 |

## Langkah demi langkah

### Tahap 1
1. Jalankan `00_Kenalan_Dengan_Data`.
2. **Buddy check Peran 2:** buka `01_Data_Engineer` hasil kerjanya. Cek: (a) tiap keputusan punya alasan, (b) jumlah baris di log = jumlah baris di `Kelompok_12_data_bersih.csv`, (c) kamu setuju dengan cara menangani outlier? Catat hasilnya di log rapat.
3. Mulai belajar konsep (bagian "Konsep"). Jalankan `03_Regression_Modeling` dengan data draf untuk melihat bentuk hasilnya.

### Tahap 2–3
4. Pelajari lebih dalam: baca `summary` OLS sedikit demi sedikit. Targetmu: bisa menunjuk di tabel itu *di mana* R², uji-F, dan uji-t.
5. Lakukan **buddy check Peran 1** (Tahap 4): memeriksa rekomendasi.

### Tahap 4 — mulai begitu data bersih resmi ada (data bersih resmi wajib)
6. Mulai sesi Colab baru; pastikan tertulis **DATA BERSIH RESMI**.
7. **Bagian A — Korelasi:** jalankan, baca heatmap, tulis interpretasi.
8. **Bagian B — Model:** jalankan model utama `PM2.5 ~ Volume + Angin`. Catat persamaan (otomatis tercetak).
9. **Bagian C — Evaluasi:** isi tabel ✏️ (Uji-F, Uji-t tiap prediktor, R², Adj R²). Tulis arti koefisien dalam kalimat sehari-hari.
10. **Bagian D — Asumsi:** baca 3 grafik residual + Shapiro + Breusch-Pagan + VIF. Tulis kesimpulan jujur (*terpenuhi / dilanggar / dampaknya*).
11. (Opsional) **Bagian E:** model diperluas; hanya sebagai analisis tambahan.
12. Berikan `04_regresi_skenario_prediksi.csv` & angka "what-if" ke **Peran 1**.
13. Upload hasil & simpan notebook. Minta **Peran 3** memeriksa interpretasimu.

## Konsep yang harus kamu pahami

**Korelasi r (−1 sampai +1):** kekuatan & arah hubungan *linear*. Tidak membuktikan sebab-akibat.

**Regresi linear berganda:** ŷ = b0 + b1·x1 + b2·x2.
- **b0** (intersep): prediksi y saat semua x = 0 (kadang tak bermakna fisik).
- **b1**: kalau x1 naik 1 satuan **dan x2 tetap**, y rata-rata berubah sebesar b1.
- **Residual** e = y − ŷ: selisih nyata vs prediksi. Mesin mencari b yang meminimalkan jumlah kuadrat residual (OLS).

**R² dan Adjusted R²:** proporsi variasi y yang dijelaskan model (0–1). Adjusted R² menghukum penambahan prediktor yang tidak berguna → pakai untuk membandingkan model dengan jumlah prediktor berbeda.

**Uji-F (simultan):** H0: semua koefisien = 0 (model tidak berguna). **Uji-t (parsial):** H0: koefisien itu = 0 (prediktor tidak berpengaruh, dengan prediktor lain tetap).

**Asumsi residual** (kenapa penting: kalau dilanggar, p-value & CI koefisien bisa menyesatkan):
| Asumsi | Cek | Tanda pelanggaran |
|---|---|---|
| Normalitas residual | histogram, Q-Q plot, Shapiro | Q-Q melengkung jauh; Shapiro p < 0.05 |
| Homoskedastisitas | fitted vs residual, Breusch-Pagan | sebaran melebar membentuk corong; BP p < 0.05 |
| Linearitas | fitted vs residual | pola melengkung |
| Tanpa multikolinearitas | VIF | VIF > 5–10 |

**Ekstrapolasi:** jangan memakai model di luar rentang data (mis. Volume jauh di atas 813) — prediksi di sana tidak bisa dipercaya.

## Kesalahan umum
- **Memasukkan `Status_Udara` sebagai prediktor** — itu hasil perhitungan dari PM2.5 ("menyontek jawaban").
- Menganggap R² tinggi = model pasti bagus (asumsi tetap harus dicek).
- Menafsirkan korelasi/koefisien sebagai sebab-akibat tanpa kehati-hatian.
- Mengabaikan hasil uji asumsi atau hanya menulis "terpenuhi" tanpa melihat grafik.
- Salah arah tanda koefisien (angin negatif = angin kencang **menurunkan** PM2.5).
- Lupa bahwa koefisien dibaca "dengan variabel lain tetap".
- Memakai data draf untuk hasil final.

## Pertanyaan yang mungkin ditanya dosen
1. Tuliskan persamaan regresi kalian dan jelaskan arti b1 dan b2.
2. Apa bedanya R² dan Adjusted R²? Berapa nilainya dan apa artinya?
3. Apa hipotesis Uji-F dan Uji-t? Apa keputusannya?
4. Kenapa asumsi residual perlu dicek? Apa yang kalian temukan?
5. Apakah volume kendaraan *menyebabkan* PM2.5 naik? (jawab hati-hati: data observasional, tapi ada dasar ilmiah)
6. Prediksi PM2.5 untuk volume 500 dan angin 10 km/jam? (berapa, dan berapa rentang ketidakpastiannya)
7. Kenapa `Status_Udara` tidak dimasukkan sebagai variabel prediktor?

## Kerja sama
- **Menunggu dari:** Peran 2 (data bersih).
- **Memberi ke:** Peran 1 (what-if), Peran 6 (interpretasi), Peran 5 (angka untuk scatter).
- **Memeriksa:** Peran 2 (pembersihan, Tahap 1), Peran 1 (rekomendasi, Tahap 4). **Diperiksa oleh:** Peran 3.

## ✅ Checklist
- [ ] Matriks korelasi + heatmap + interpretasi
- [ ] Persamaan regresi dengan angka b0, b1, b2
- [ ] R², Adj R², Uji-F, Uji-t (tiap prediktor) + makna
- [ ] Histogram/Q-Q residual + fitted vs residual + kesimpulan asumsi
- [ ] "What-if" diberikan ke Peran 1
- [ ] Buddy check Peran 2 & Peran 1 tercatat
- [ ] Hasil & notebook di GitHub
