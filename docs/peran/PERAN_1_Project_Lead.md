# PERAN 1 — Project Lead
*(Perumusan masalah & kesimpulan strategis)*

## Kamu di proyek ini
Kamu **kapten kapal**, bukan juru mesin. Kamu tidak harus paling jago statistik, tapi kamu yang memastikan (1) semua orang tahu harus mengerjakan apa dan kapan, (2) keputusan penting dicatat, (3) hasil 5 orang menyatu menjadi **satu cerita utuh**: *apa masalahnya → apa temuannya → apa yang sebaiknya dilakukan*.
Dalam analogi proyek Linux: kamu *maintainer* yang menjaga repo tetap rapi dan arah proyek jelas.

## Hasil akhir yang harus kamu serahkan
| File | Isi | Kapan |
|---|---|---|
| Repo GitHub siap pakai | struktur ter-upload, placeholder diganti, 5 kolaborator masuk | Tahap 1, hari 1 |
| `reports/draft/00_halaman_pengesahan.md` | nama, NIM, peran, % kontribusi, tanda tangan | diisi bertahap, final di akhir |
| `reports/draft/01_latar_belakang_dan_rumusan_masalah.md` | konteks, rumusan masalah, tujuan, variabel, batasan | Tahap 1 |
| `reports/draft/04_kesimpulan_dan_rekomendasi.md` | kesimpulan strategis + **≥ 3 rekomendasi konkret** | Tahap 4 |
| `reports/draft/05_log_rapat_dan_review.md` | notulen rapat singkat + catatan buddy check | tiap rapat |

## Langkah demi langkah

### Tahap 1
1. **Setup repo** — ikuti `docs/02_panduan_github_colab.md` Bagian 1–3. Pastikan semua anggota bisa membuka notebook `00_Kenalan_Dengan_Data` di Colab. *Tes nyata:* minta tiap orang mengirim screenshot "Setup selesai".
2. **Rapat kick-off 30 menit:** bagikan peran (satu orang satu peran), sepakati jadwal (`docs/03_jadwal_dan_alur_kerja.md`), sepakati cara komunikasi (grup chat) dan jam rapat mingguan.
3. **Isi `01_latar_belakang_dan_rumusan_masalah.md`.** Template sudah ada. Intinya:
   - *Konteks:* kenapa kualitas udara (PM2.5) penting bagi kota? (cari 2–3 fakta/ sumber tepercaya; tulis sumbernya)
   - *Rumusan masalah:* ubah 4 pertanyaan dosen menjadi kalimat tanya milikmu (lihat README).
   - *Tujuan:* satu tujuan per pertanyaan.
   - *Data:* ringkas dari `data/README.md`.
   - *Batasan:* data **observasional** — kita bisa melihat hubungan, tidak otomatis membuktikan sebab-akibat.
4. **Tetapkan kerangka konsisten:** nama variabel, singkatan, dan satuan yang sama dipakai semua orang (mis. selalu "Indeks PM2.5", bukan kadang "PM25").

### Tahap 2–3 (mode koordinator)
5. Tiap rapat singkat (tiap 3–4 hari): tanya 3 hal — *sudah selesai apa, macet di mana, menunggu siapa.* Catat di log rapat.
6. Pantau GitHub: apakah hasil sudah di-upload? Apakah buddy check sudah dijalankan?
7. **Jaga agar Peran 3 tidak kewalahan** (beban terberat di Tahap 2–3): tanyakan apakah ada bagian yang bisa dibantu cek oleh orang lain.
8. Mulai kumpulkan **temuan sementara** ke `04_kesimpulan_dan_rekomendasi.md` (bagian "Catatan temuan") setiap kali satu hasil keluar.

### Tahap 4 (kesimpulan strategis)
9. Setelah Peran 3 dan 4 selesai, baca ringkasan hasil: `outputs/tables/03_ringkasan_uji_hipotesis.csv`, `04_regresi_koefisien.csv`, `04_regresi_skenario_prediksi.csv`.
10. Susun kesimpulan dengan **rantai "Temuan → Bukti → Arti → Rekomendasi"**:

    > **Temuan:** (satu kalimat, bahasa awam) →
    > **Bukti:** (angka + uji, mis. "rata-rata PM2.5 di Pusat Kota … vs Pinggiran …, ANOVA p < 0.05") →
    > **Arti:** (apa pengaruhnya bagi warga/kota) →
    > **Rekomendasi:** (tindakan konkret)

11. **Rekomendasi yang baik itu konkret.** Cek dengan 5 pertanyaan: **Siapa** yang bertindak? **Apa** tindakannya? **Di mana**? **Kapan**? **Bagaimana kita tahu berhasil** (indikator terukur)? Rekomendasi seperti "pemerintah harus peduli lingkungan" = **tidak konkret**.
12. Minta **Peran 4** (buddy check) memastikan tiap rekomendasi punya angka pendukung; minta **Peran 6** menghaluskan bahasanya.
13. Finalisasi: isi halaman pengesahan (**persentase kontribusi harus jujur dan total 100%**; tiap anggota tanda tangan), cek konsistensi angka laporan = poster = notebook.

## Konsep yang harus kamu pahami
- **Observasional vs eksperimen.** Data kita hasil pengamatan; tidak ada yang "memaksa" volume kendaraan naik. Jadi kita bilang *"berkaitan dengan / diikuti oleh"*, bukan *"menyebabkan"* — kecuali ada alasan ilmiah kuat (di sini ada: kendaraan mengeluarkan partikel).
- **Signifikan secara statistik ≠ penting secara praktis.** Selisih kecil bisa signifikan jika sampel besar. Selalu sertakan **besar selisihnya** (mis. "26 poin lebih tinggi"), bukan hanya p-value.
- **Gambaran besar tiap metode** (cukup tahu intinya untuk memimpin presentasi): uji-t (bandingkan 2 rata-rata), ANOVA (≥ 3 rata-rata), Chi-Square (hubungan 2 kategori), regresi (prediksi + besar pengaruh).

## Kesalahan umum
- Rekomendasi tanpa angka atau terlalu umum.
- Mengklaim sebab-akibat dari data observasional.
- Menumpuk semua pekerjaan di Peran 3 lalu panik di Tahap 3.
- Menunda laporan/poster ke 2 hari terakhir. (Susun kerangka laporan sejak Tahap 3!)
- Persentase kontribusi dibagi rata "asal" padahal kerja tidak merata — dosen bisa menanyakannya.

## Pertanyaan yang mungkin ditanya dosen (siapkan jawabanmu)
1. Apa masalah utama yang kalian teliti dan kenapa penting?
2. Apa **3 temuan utama** kalian?
3. Dari temuan itu, keputusan apa yang kalian sarankan? Bagaimana mengukur keberhasilannya?
4. Apa keterbatasan analisis kalian?
5. Bagaimana kalian membagi kerja? Siapa mengerjakan apa?

## Kerja sama
- **Menerima dari:** semua peran (hasil tiap tahap).
- **Memberi ke:** Peran 6 (bahan rekomendasi), Peran 5 (pesan utama untuk poster).
- **Diperiksa oleh:** Peran 4 (rekomendasi didukung angka).

## ✅ Checklist
- [ ] Repo siap, placeholder diganti, 5 kolaborator masuk & bisa membuka Colab
- [ ] Peran terbagi + jadwal disepakati
- [ ] Latar belakang & rumusan masalah selesai
- [ ] Rapat singkat tercatat
- [ ] ≥ 3 rekomendasi konkret (siapa-apa-di mana-kapan-indikator) dengan angka pendukung
- [ ] Halaman pengesahan terisi (kontribusi total 100%) & ditandatangani semua
- [ ] Angka di laporan = poster = notebook
