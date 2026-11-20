# Bab II: Metodologi Eksplorasi dan Pembersihan Data

Tahap pra-pemrosesan data dilakukan untuk memastikan bahwa seluruh variabel pada dataset **Tema B (Kualitas Udara & Mobilitas Perkotaan)** berada dalam kondisi valid, konsisten, dan siap dianalisis secara statistik[cite: 1, 2]. Seluruh prosedur pembersihan dijalankan melalui notebook `00_Kenalan_Dengan_Data.ipynb` dan `01_Data_Engineer.ipynb` dengan dataset mentah `data/Kelompok_12_Tema_B_Kualitas_Udara.csv` ($N = \text{[isi jumlah baris awal]}$ observasi) sebagai sumber masukan utama[cite: 1].

---

## 2.1 Identifikasi Skala Pengukuran Variabel
Sebelum menerapkan teknik pembersihan maupun pengujian statistik, setiap kolom pada dataset diklasifikasikan berdasarkan tingkat skala pengukurannya agar pemilihan metode ringkasan dan uji hipotesis sesuai dengan sifat matematis data[cite: 1]. Rekapitulasi lengkap klasifikasi ini tersimpan pada berkas `outputs/tables/01_skala_pengukuran.csv` dengan pemetaan sebagai berikut:

* **Skala Rasio:** Diterapkan pada variabel numerik kontinu maupun diskrit yang memiliki titik nol mutlak dan perbandingan kelipatan yang bermakna, meliputi `Indeks_PM25` ($\mu\text{g/m}^3$), `Volume_Kendaraan` (unit kendaraan), dan `Kecepatan_Angin_KmJ` (km/jam)[cite: 1].
* **Skala Ordinal:** Diterapkan pada variabel kategorikal `Status_Udara` karena kategori di dalamnya memiliki tingkatan hierarkis yang mencerminkan tingkat keparahan kualitas udara (seperti *Baik*, *Sedang*, hingga *Tidak Sehat*)[cite: 1].
* **Skala Nominal:** Diterapkan pada atribut kategorikal yang berfungsi semata-mata sebagai label pembeda kelompok tanpa urutan tingkatan, yaitu `Zona_Lokasi`, `Hari_Kerja` (atau jenis hari), dan `Jam_Sibuk`[cite: 1].

---

## 2.2 Penanganan Data Hilang (*Missing Values*)
Pemeriksaan kelengkapan data dilakukan pada setiap atribut untuk mendeteksi keberadaan nilai kosong (*null/NaN*)[cite: 1]. Berdasarkan ringkasan hasil pengecekan pada `outputs/tables/01_missing_values.csv`, tercatat sebanyak **[isi total missing values atau tulis "0 (tidak ditemukan data hilang)"]** entri kosong pada dataset awal.

Apabila ditemukan data yang hilang, penanganan dilakukan melalui metode imputasi statistik guna mempertahankan keutuhan jumlah sampel penelitian[cite: 1]:
1. **Variabel Numerik:** Pemilihan ukuran pemusatan didasarkan pada tingkat kemencengan distribusi (*skewness*)[cite: 1]. Variabel dengan sebaran miring ($|\text{skewness}| > 0,5$) diimputasi menggunakan nilai **median** agar tidak terpengaruh nilai ekstrem, sedangkan variabel dengan sebaran cenderung simetris diimputasi menggunakan nilai rata-rata (**mean**)[cite: 1].
2. **Variabel Kategorikal:** Nilai yang hilang diisi menggunakan nilai yang paling sering muncul (**modus**) pada masing-masing kolom atribut[cite: 1].

---

## 2.3 Deteksi dan Penanganan Pencilan (*Outlier*) dengan Metode IQR
Identifikasi nilai ekstrem pada variabel numerik berskala rasio diterapkan menggunakan pendekatan *Interquartile Range* ($\text{IQR} = Q_3 - Q_1$)[cite: 1]. Suatu pengamatan dikategorikan sebagai pencilan apabila nilainya berada di luar rentang batas pagar bawah dan batas pagar atas yang dirumuskan sebagai berikut[cite: 1]:

$$\text{Batas Bawah} = Q_1 - 1,5 \times \text{IQR}$$

$$\text{Batas Atas} = Q_3 + 1,5 \times \text{IQR}$$

Berdasarkan hasil perhitungan pada `outputs/tables/01_outlier_iqr.csv`, ditemukan pencilan pada variabel **[isi nama variabel yang memiliki outlier, misalnya: `Indeks_PM25` sebanyak XX data, `Volume_Kendaraan` sebanyak XX data]**. Alih-alih menghapus baris observasi yang berpotensi mengurangi representasi sampel pada jam atau zona tertentu, penanganan pencilan dilakukan menggunakan metode ***capping* (*winsorizing*)**[cite: 1]. Melalui metode ini, nilai yang melampaui batas pagar atas disesuaikan ke nilai batas pagar atas, sedangkan nilai yang berada di bawah batas pagar bawah disesuaikan ke nilai batas pagar bawah[cite: 1]. Perubahan sebaran distribusi sebelum dan sesudah proses *capping* didokumentasikan secara visual pada `outputs/figures/01_boxplot_sebelum.png` dan `outputs/figures/01_boxplot_sesudah.png`.

---

## 2.4 Validasi Akhir dan Keluaran Data Bersih
Sebagai tahap verifikasi akhir, dilakukan perbandingan parameter statistik deskriptif (rata-rata, simpangan baku, nilai minimum, median, dan nilai maksimum) antara kondisi sebelum dan sesudah pembersihan yang tercatat pada `outputs/tables/01_perbandingan_sebelum_sesudah.csv` serta catatan kronologis pada `outputs/tables/01_log_pembersihan.txt`.

Hasil akhir dari seluruh rangkaian pra-pemrosesan ini disimpan ke dalam berkas **`data/Kelompok_12_data_bersih.csv`** dengan ukuran akhir tetap sebesar $N = \text{[isi jumlah baris akhir]}$ observasi tanpa nilai kosong maupun pencilan ekstrem. Dataset bersih tersebut ditetapkan sebagai rujukan tunggal bagi seluruh tahapan pemodelan probabilitas, pengujian hipotesis, analisis regresi, dan visualisasi data pada pekan-pekan berikutnya[cite: 1].