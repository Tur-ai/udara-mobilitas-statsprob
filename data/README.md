# Kamus Data — Kelompok 12, Tema B (Kualitas Udara & Mobilitas Perkotaan)

**File asli:** `Kelompok_12_Tema_B_Kualitas_Udara.csv` — 350 baris × 9 kolom. ⚠️ **Jangan diedit.**
**File bersih (dibuat Peran 2):** `Kelompok_12_data_bersih.csv`

| Kolom | Arti | Tipe | Catatan |
|---|---|---|---|
| `ID_Observasi` | nomor unik baris (OBS-12-xxxx) | pengenal | tidak dianalisis |
| `Zona_Lokasi` | Pusat Kota / Kawasan Kampus / Pinggiran | kategori (3) | faktor di ANOVA |
| `Jenis_Hari` | Hari Kerja / Akhir Pekan | kategori (2) | kelompok di uji-t |
| `Jam_Sibuk` | Ya / Tidak | kategori (2) | dipakai di Chi-Square & peluang bersyarat |
| `Volume_Kendaraan` | jumlah kendaraan | angka | prediktor regresi |
| `Kecepatan_Angin_KmJ` | kecepatan angin, km/jam | angka | prediktor regresi |
| `Suhu_Celcius` | suhu udara, °C | angka | variabel tambahan |
| `Indeks_PM25` | konsentrasi PM2.5 | angka | **variabel utama / respons regresi** |
| `Status_Udara` | Baik / Sedang / Tidak Sehat | kategori berurutan | turunan dari `Indeks_PM25` |

## Aturan kategori `Status_Udara` (terbaca dari data)
| Status | Rentang `Indeks_PM25` |
|---|---|
| Baik | ≤ 35 |
| Sedang | > 35 hingga 65 |
| Tidak Sehat | > 65 |

⚠️ `Status_Udara` dihitung **langsung** dari `Indeks_PM25`. Jangan dipakai sebagai prediktor untuk memprediksi `Indeks_PM25` (itu "menyontek jawaban").

## Hal yang perlu ditangani Peran 2 (Data Engineer)
Detail & keputusan lengkap ada di notebook `01_Data_Engineer`. Ringkasan temuan awal:
- Ada sel kosong di `Kecepatan_Angin_KmJ` dan `Indeks_PM25`.
- Ada baris yang `Status_Udara`-nya **bertentangan** dengan nilai `Indeks_PM25` (indikasi salah input).
- Ada nilai di luar pagar IQR pada beberapa variabel.
