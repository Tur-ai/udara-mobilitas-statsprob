# Laporan Progres Minggu 2: Pemodelan Probabilitas dan Distribusi

**Kelompok:** 12  
**Tema Studi Kasus:** Tema B — Kualitas Udara & Mobilitas Perkotaan  
**Penanggung Jawab Minggu 2:** Probability & Inference Analyst & Project Lead  

---

## 1. Evaluasi Lanjutan dan Penyelarasan Data (Project Lead)
Pada awal pekan kedua, dilakukan peninjauan terhadap kesiapan dataset bersih `data/Kelompok_12_data_bersih.csv` ($N = \text{[isi N]}$ observasi) agar seluruh anggota tim merujuk pada sumber data yang seragam. Jalur pembacaan berkas pada notebook tahap pemodelan telah disesuaikan dengan struktur direktori utama repositori. Selain itu, kelengkapan draf metodologi pembersihan data pada `reports/draft/02_metodologi_pembersihan_data.md` serta catatan pembagian kerja pada `reports/draft/05_log_rapat_dan_review.md` telah diperbarui sebelum tahap analisis probabilitas dijalankan.

## 2. Pelaksanaan Analisis Probabilitas dan Distribusi (Probability & Inference Analyst)
Seluruh perhitungan peluang dan pemodelan sebaran data pekan kedua telah dieksekusi melalui notebook `notebooks/02a_Probability_Peluang_Distribusi.ipynb` dengan rincian hasil sebagai berikut:

* **Peluang Empiris dan Peluang Bersyarat (Checklist 2a):** Telah dihitung tiga nilai peluang kejadian empiris serta dua peluang bersyarat yang menjawab rumusan masalah utama Tema B. Secara keseluruhan, proporsi kondisi udara berstatus Tidak Sehat tercatat sebesar `[XX,XX]%` ($P = \text{[0,XXXX]}$). Ketika pengamatan dikondisikan pada periode jam sibuk, nilai peluang bersyarat $P(\text{Tidak Sehat} \mid \text{Jam Sibuk} = \text{Ya})$ menjadi `[XX,XX]%`, dibandingkan dengan `[XX,XX]%` pada periode di luar jam sibuk. Perbedaan tersebut mengindikasikan adanya kecenderungan peningkatan risiko polusi pada jam padat lalu lintas yang akan diuji signifikansinya pada tahap inferensi.
* **Pemodelan Distribusi Normal (Checklist 2b):** Variabel kontinu `Indeks_PM25` dimodelkan dengan estimasi rata-rata sampel $\mu = \text{[XX,XX]}$ dan simpangan baku $s = \text{[XX,XX]}$. Pemeriksaan kesesuaian distribusi dilakukan melalui histogram kurva *PDF*, *Normal Q-Q Plot*, perbandingan aturan empiris 68–95–99,7, serta uji formal Shapiro-Wilk ($W = \text{[0,XXXX]}$, $p\text{-value} = \text{[X,XXXX]}$). Melalui standardisasi skor-$Z$, probabilitas teoretis polusi kategori Tidak Sehat $P(\text{Indeks\_PM25} > 65)$ diperoleh sebesar `[XX,XX]%`, sedangkan peluang kategori Baik $P(\text{Indeks\_PM25} \le 35)$ tercatat sebesar `[XX,XX]%`.
* **Pemodelan Distribusi Binomial (Checklist 2c):** Kejadian status udara Tidak Sehat dengan proporsi empiris $p = \text{[0,XXXX]}$ dimodelkan pada skenario pengambilan sampel acak sebanyak $n = 20$ titik pengukuran. Hasil perhitungan fungsi massa probabilitas menghasilkan peluang tepat $P(X = \text{[k]}) = \text{[XX,XX]}\%$ dan peluang kumulatif minimal $P(X \ge \text{[k]}) = \text{[XX,XX]}\%$, dengan nilai harapan sebanyak `[X,XX]` titik berada dalam kategori Tidak Sehat.

## 3. Daftar Keluaran (*Deliverables*) Minggu 2
* **Notebook Analisis:** `notebooks/02a_Probability_Peluang_Distribusi.ipynb` (telah dijalankan penuh beserta narasi interpretasi)
* **Tabel Output:** `outputs/tables/02a_peluang_empiris_bersyarat.csv`, `02_normal_aturan_empiris.csv`, `02_normal_peluang.csv`, dan `02_binomial_tabel.csv`
* **Grafik Visualisasi:** `outputs/figures/02_normal_histogram_qq.png`, `02_normal_area_peluang.png`, dan `02_binomial_pmf.png`
* **Draf Laporan & Log:** Pembaruan pada `reports/draft/03_interpretasi_hasil_per_uji.md` dan `reports/draft/05_log_rapat_dan_review.md`