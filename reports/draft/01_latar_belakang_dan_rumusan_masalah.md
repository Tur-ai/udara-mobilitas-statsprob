# Latar belakang dan rumusan masalah

Mobilitas perkotaan berubah menurut hari, lokasi, dan waktu. Jumlah kendaraan memberikan ukuran aktivitas lalu lintas, sementara angin menggambarkan kondisi yang dapat memengaruhi penyebaran partikel. Pusat Kota, Kawasan Kampus, dan Pinggiran memberi tiga konteks untuk membandingkan kualitas udara dan menentukan prioritas pengukuran.

Proyek ini menggunakan `Kelompok_12_Tema_B_Kualitas_Udara.csv`, berisi 350 observasi. `Indeks_PM25` digunakan sebagai ukuran numerik kualitas udara dalam skala dataset. `Status_Udara` merangkum ukuran itu ke dalam kategori Baik, Sedang, dan Tidak Sehat. Variabel lain mencakup volume kendaraan, kecepatan angin, suhu, jenis hari, dan indikator jam sibuk.

## Rumusan masalah

1. Apakah rata-rata Indeks_PM25 berbeda antara hari kerja dan akhir pekan? Uji dengan uji-t Welch dua sampel independen.
2. Apakah rata-rata Indeks_PM25 berbeda antara Pusat Kota, Kawasan Kampus, dan Pinggiran? Uji dengan ANOVA satu arah dan identifikasi pasangan dengan Tukey.
3. Apakah Status_Udara berasosiasi dengan Jam_Sibuk? Uji dengan Chi-Square dan bandingkan peluang Tidak Sehat di dalam dan di luar jam sibuk.
4. Bagaimana volume kendaraan dan kecepatan angin berasosiasi dengan Indeks_PM25 setelah mengontrol suhu dan prediktor lain dalam regresi linear berganda?

Tujuan analisis adalah mengukur perbedaan yang terlihat dalam sampel, menilai ketidakpastian, dan merumuskan opsi pemantauan serta uji coba pengelolaan mobilitas. Analisis menggunakan observasi yang lolos pembersihan. Cakupan kota dan periode pengamatan tidak diketahui. Tanpa tanggal dan identitas stasiun, independensi serta representativitas belum dapat dipastikan. Desain observasional dan kovariat terbatas membatasi klaim sebab-akibat. Ambang 35 dan 65 mengikuti kamus dataset. Satuan dan kalibrasi alat belum terdokumentasi.
