# PERAN 6 — Technical Writer & Presentation Lead
*(Menerjemahkan hasil uji statistik menjadi bahan kebijakan/bisnis)*

## Kamu di proyek ini
Kamu **jembatan antara angka dan manusia**. Temanmu menghasilkan "t = 8.24, p < 0.001". Kamu mengubahnya menjadi: *"Udara di hari kerja secara nyata lebih berpolusi daripada akhir pekan — selisih sekitar 14 poin — jadi program pengurangan kendaraan layak difokuskan di hari kerja."* Kamu juga **memimpin presentasi** Gallery Walk (7 menit: 5 menit paparan + 2 menit tanya-jawab).

## Hasil akhir yang harus kamu serahkan
| File | Isi | Kapan |
|---|---|---|
| `reports/draft/02_metodologi_pembersihan_data.md` | bahasa jelas dari log Peran 2 | Tahap 1 |
| `reports/draft/03_interpretasi_hasil_per_uji.md` | untuk SETIAP analisis: H0, H1, statistik, p, keputusan, **interpretasi bahasa sehari-hari** | Tahap 2–4 |
| Polesan `04_kesimpulan_dan_rekomendasi.md` | rekomendasi bahasa kebijakan/bisnis (dari Peran 1) | Tahap 4 |
| Naskah presentasi 5 menit + daftar tanya-jawab | | Tahap 4 |
| Ringkasan eksekutif (untuk laporan) | 1 halaman | menyusul |

## Langkah demi langkah

### Tahap 1
1. Jalankan `00_Kenalan_Dengan_Data`. Baca `data/README.md` dan `docs/04_glosarium.md`.
2. Setelah Peran 2 mengirim log, tulis `02_metodologi_pembersihan_data.md`: *apa masalah di data → apa yang kami lakukan → kenapa → dampaknya.* Tanyakan ke Peran 2 bila ada alasan yang belum jelas.
3. **Buddy check Peran 5:** cocokkan angka di tabel dan grafik; cek judul grafik tidak melebih-lebihkan.

### Tahap 2 dan 3
4. Setelah Peran 3 meng-upload hasil, isi `03_interpretasi_hasil_per_uji.md`. Untuk tiap uji gunakan **resep 4 kalimat**:
   1. **Pertanyaan** (apa yang ingin diketahui?)
   2. **Hasil** (angka kunci: rata-rata/proporsi, selisih)
   3. **Seberapa yakin** (p-value / CI dalam bahasa awam)
   4. **Artinya** (apa implikasinya bagi kota/warga)
5. Duduk 15 menit dengan Peran 3: bacakan interpretasimu → minta dikoreksi istilah statistiknya (buddy check).

### Tahap 4
6. Ambil rekomendasi mentah Peran 1 → ubah menjadi bahasa kebijakan/bisnis: **siapa**, **apa**, **di mana**, **kapan**, **indikator keberhasilan**, **perkiraan dampak** (pakai angka what-if Peran 4).
7. Tulis **naskah presentasi 5 menit** (struktur di bawah) + latihan dengan stopwatch.
8. Susun daftar **15 pertanyaan tanya-jawab** dari "Pertanyaan yang mungkin ditanya dosen" di 6 file peran; bagikan ke semua untuk dilatih.
9. Bersama Peran 5 dan Peran 1: susun **laporan PDF & poster** (menyusul).

## Menerjemahkan istilah statistik ke bahasa awam
| Jargon | Bahasa awam |
|---|---|
| "Tolak H0 (p < 0.05)" | "Perbedaannya cukup kuat; sangat kecil kemungkinannya terjadi hanya karena kebetulan." |
| "Gagal tolak H0 (p ≥ 0.05)" | "Belum ada bukti yang cukup bahwa ada beda. (Bukan berarti pasti sama.)" |
| "CI 95% = [40.1; 43.5]" | "Kami cukup yakin (95%) rata-rata sebenarnya di kota ini antara 40,1 dan 43,5." |
| "R² = 0.82" | "Volume kendaraan dan angin bersama-sama menjelaskan sekitar 82% naik-turunnya PM2.5." *(angka contoh — pakai angka hasil asli)* |
| "b1 = +0.08" | "Setiap tambahan 100 kendaraan, rata-rata PM2.5 naik sekitar 8 poin, dengan angin dianggap tetap." *(contoh)* |
| "Korelasi r = 0.7" | "Keduanya cenderung naik bersama, hubungannya cukup kuat. Itu tidak otomatis berarti yang satu menyebabkan yang lain." |
| "Asumsi homoskedastisitas terpenuhi" | "Ketelitian prediksi model kurang lebih sama di semua tingkat polusi, jadi kita bisa memercayai hasilnya." |
| "Signifikan secara statistik" | "Cukup kuat untuk dianggap bukan kebetulan." |

> ⚠️ Angka pada kolom kanan hanya **contoh**. Selalu ganti dengan angka hasil asli dari file di `outputs/tables/`.

**Aturan emas penulisan:** satu kalimat = satu gagasan · sebut **angka + satuan** · jelaskan istilah teknis saat pertama muncul · jangan menulis "terbukti"/"menyebabkan" tanpa dasar · tulis keterbatasan secara jujur.

## Struktur presentasi 5 menit (Gallery Walk)
| Waktu | Isi | Pembicara (usulan) |
|---|---|---|
| 0:00–0:30 | **Pembuka:** masalah & kenapa penting (1 fakta menarik) | Peran 1 / 6 |
| 0:30–1:15 | **Data & pembersihan:** apa datanya, apa jebakannya, apa yang dilakukan | Peran 2 |
| 1:15–3:15 | **3 temuan utama** (peluang/uji/regresi) — tiap temuan = 1 grafik + 1 kalimat | Peran 3 & 4 |
| 3:15–4:30 | **Rekomendasi** (≥ 3, konkret) | Peran 1 / 6 |
| 4:30–5:00 | **Penutup:** satu kalimat yang harus diingat + keterbatasan | Peran 1 |
| 5:00–7:00 | **Tanya-jawab** — **siapa pun bisa ditanya**; yang paling paham menjawab, yang lain melengkapi | semua |

**Tips:** satu tiang cerita (*masalah → bukti → solusi*) · latihan minimal 3× dengan stopwatch · siapkan satu kalimat jawaban untuk "apa keterbatasan kalian?".

## Kesalahan umum
- Menyalin angka/istilah tanpa mengerti → kamu jadi sasaran tanya jawab.
- Menulis "H0 diterima" atau "terbukti menyebabkan".
- Rekomendasi tanpa angka.
- Interpretasi yang bertentangan dengan hasil uji (mis. p > 0.05 tapi tulis "berbeda signifikan").
- Presentasi 8 menit padahal jatahnya 5.
- Angka di naskah berbeda dari di poster/laporan.

## Pertanyaan yang mungkin ditanya dosen
1. Jelaskan temuan kalian pada orang awam dalam 1 menit.
2. Apa arti statistik "signifikan" yang kalian pakai?
3. Kalau kalian jadi pemerintah kota, apa yang pertama dilakukan dan kenapa?
4. Apa yang tidak bisa disimpulkan dari data ini?
5. Apa keterbatasan data/analisis kalian?

## Kerja sama
- **Menunggu dari:** Peran 2 (log), Peran 3 (hasil uji), Peran 4 (regresi), Peran 1 (rekomendasi mentah), Peran 5 (grafik).
- **Memberi ke:** Peran 1 & 5 (teks final untuk laporan & poster).
- **Memeriksa:** Peran 5. **Diperiksa oleh:** Peran 3.

## ✅ Checklist
- [ ] Metodologi pembersihan data (bahasa jelas)
- [ ] Interpretasi tiap analisis (resep 4 kalimat) — Tahap 2, 3, 4
- [ ] Interpretasi sudah diperiksa Peran 3
- [ ] Rekomendasi berbahasa kebijakan/bisnis dengan angka pendukung
- [ ] Naskah presentasi 5 menit + latihan dengan stopwatch
- [ ] Daftar tanya-jawab dibagikan & dilatih
