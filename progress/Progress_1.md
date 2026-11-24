# Laporan Progres Minggu 1: Eksplorasi Awal dan Pembersihan Data

**Kelompok:** 12  
**Tema Studi Kasus:** Tema B — Kualitas Udara & Mobilitas Perkotaan  
**Penanggung Jawab:** Project Lead & Data Engineer  

---

## 1. Koordinasi Tim dan Perumusan Masalah (Project Lead)
Pada pekan pertama, pengerjaan difokuskan pada penyiapan struktur repositori kerja serta penyelarasan pembagian tugas untuk enam peran anggota kelompok. Dokumen administrasi awal pada `reports/draft/00_halaman_pengesahan.md` telah dilengkapi dengan identitas anggota Kelompok 12 beserta pembagian porsi kontribusinya. Selain itu, empat pertanyaan riset utama yang menjadi acuan analisis statistik telah dirumuskan di dalam `reports/draft/01_latar_belakang_dan_rumusan_masalah.md`, meliputi pengujian perbedaan rata-rata `Indeks_PM25` berdasarkan jenis hari dan zona lokasi, keterkaitan antara status udara dan jam sibuk, serta pemodelan regresi pengaruh volume kendaraan dan kecepatan angin terhadap tingkat polusi.

## 2. Hasil Eksplorasi dan Pembersihan Data (Data Engineer)
Proses pemeriksaan dan pra-pemrosesan data dilakukan melalui notebook `00_Kenalan_Dengan_Data.ipynb` dan `01_Data_Engineer.ipynb` menggunakan dataset mentah `data/Kelompok_12_Tema_B_Kualitas_Udara.csv`. Rincian tahapan yang telah diselesaikan adalah sebagai berikut:

* **Klasifikasi Skala Pengukuran:** Seluruh atribut pada dataset telah dipetakan sesuai karakteristik statistiknya. Variabel numerik seperti `Indeks_PM25`, `Volume_Kendaraan`, dan `Kecepatan_Angin_KmJ` dikategorikan ke dalam skala Rasio karena memiliki titik nol mutlak. Sementara itu, `Status_Udara` diklasifikasikan sebagai skala Ordinal karena memuat tingkatan kualitas udara, sedangkan `Zona_Lokasi`, `Hari_Kerja`, dan `Jam_Sibuk` termasuk dalam skala Nominal sebagai label pembeda kategori.
* **Penanganan Data Hilang (*Missing Values*):** Berdasarkan hasil rekapitulasi pada `outputs/tables/`, ditemukan sebanyak **[isi jumlah, misal: XX]** data kosong pada variabel **[isi nama kolom atau tulis "tidak ditemukan data kosong pada seluruh kolom"]**[cite: 1]. Untuk menjaga keutuhan jumlah observasi, nilai yang hilang pada variabel numerik dengan sebaran miring (*skewed*) ditangani melalui imputasi median, sedangkan distribusi yang cenderung simetris menggunakan nilai rata-rata (*mean*), dan atribut kategorikal diisi menggunakan nilai modus[cite: 1].
* **Deteksi dan Penanganan Pencilan (*Outlier*):** Identifikasi nilai ekstrem diterapkan menggunakan metode batas pagar *Interquartile Range* ($Q_1 - 1.5 \times \text{IQR}$ dan $Q_3 + 1.5 \times \text{IQR}$) yang tercatat pada tabel laporan outlier di `outputs/tables/`[cite: 1]. Sebanyak **[isi total outlier, misal: XX]** titik pencilan terdeteksi pada variabel **[isi nama variabel]**. Penanganan dilakukan dengan metode *capping* (*winsorizing*) ke batas pagar atas dan bawah agar sebaran data menjadi lebih stabil tanpa mengurangi ukuran sampel[cite: 1]. Perbandingan sebaran sebelum dan sesudah proses ini telah divisualisasikan pada grafik boxplot di folder `outputs/figures/`[cite: 1].
* **Statistika Deskriptif dan Visualisasi Eksplorasi:** Ringkasan ukuran pemusatan dan penyebaran data bersih (meliputi *mean*, median, modus, standar deviasi, varians, IQR, serta *skewness*) telah dihimpun pada `outputs/tables/`[cite: 1]. Tiga grafik pendukung—yakni histogram sebaran `Indeks_PM25`, boxplot perbandingan antar-zona lokasi, serta diagram batang berkelompok (*grouped bar chart*) antara status udara dan jam sibuk—juga telah disusun untuk memetakan pola awal data[cite: 1].

## 3. Daftar Keluaran (*Deliverables*) Minggu 1
Seluruh hasil pengolahan data pekan pertama telah disimpan pada direktori berikut sebagai dasar pengerjaan analisis probabilitas dan inferensi pada pekan kedua[cite: 1]:
* **Dataset Bersih:** `data/[sesuaikan nama file bersih di folder data/]`[cite: 1]
* **Notebook Kerja:** `notebooks/00_Kenalan_Dengan_Data.ipynb` dan `notebooks/01_Data_Engineer.ipynb`[cite: 1]
* **Tabel Output:** `outputs/tables/` (laporan *missing values*, laporan *outlier*, dan tabel statistika deskriptif)[cite: 1]
* **Grafik Visualisasi:** `outputs/figures/` (5 file grafik PNG hasil pembersihan dan eksplorasi data)[cite: 1]
* **Draf Laporan:** `reports/draft/00_halaman_pengesahan.md`, `01_latar_belakang_dan_rumusan_masalah.md`, dan `02_metodologi_pembersihan_data.md`[cite: 1]
