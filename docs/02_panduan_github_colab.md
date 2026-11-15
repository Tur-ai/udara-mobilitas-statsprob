# Panduan Kerja Bareng: GitHub + Google Colab (untuk pemula)

**Ide dasarnya (3 baris):**
- **GitHub** = lemari arsip bersama. Semua file proyek disimpan di sana.
- **Google Colab** = "laptop pinjaman" di internet untuk menjalankan kode Python. Gratis, tidak perlu install.
- Alurnya: **buka notebook dari GitHub → kerjakan di Colab → unduh hasil → upload hasil ke GitHub.**

Daftar isi: [1. Setup repo (Project Lead)](#1-setup-repo-project-lead-sekali-saja) · [2. Ganti placeholder](#2-ganti-placeholder-username-dan-nama-repo) · [3. Repo private + token](#3-repo-private-agar-aman-dari-plagiarisme) · [4. Alur kerja harian](#4-alur-kerja-harian-semua-anggota) · [5. Mengunggah hasil](#5-mengunggah-hasil-ke-github) · [6. Menyimpan notebook](#6-menyimpan-notebook-yang-sudah-diisi) · [7. Aturan agar tidak tabrakan](#7-aturan-agar-tidak-tabrakan) · [8. Troubleshooting](#8-troubleshooting)

> Tampilan menu GitHub/Colab kadang berubah sedikit. Kalau nama tombolnya agak beda, cari yang artinya sama.

---

## 1. Setup repo (Project Lead, sekali saja)

1. Masuk ke <https://github.com> → **Sign up** (kalau belum punya akun).
2. Klik tombol **+** di kanan atas → **New repository**.
   - **Repository name:** mis. `proyek-udara-kelompok12` (tanpa spasi).
   - Pilih **Private** (lihat Bagian 3 kenapa).
   - Centang **Add a README file**? **Jangan** — repo harus kosong.
   - Klik **Create repository**.
3. **Unzip** file proyek ini di laptop. Kamu akan punya folder `proyek-kualitas-udara-kelompok12/` berisi `README.md`, `data/`, `notebooks/`, dst.
4. Di halaman repo yang kosong, klik link **uploading an existing file** (atau **Add file → Upload files**).
5. Buka folder hasil unzip, **pilih SEMUA isinya** (bukan folder induknya), lalu **seret ke jendela browser**.
   - Pastikan di daftar upload terlihat `README.md`, folder `data`, `notebooks`, `src`, `docs`, `outputs`, `reports`, `poster`.
   - ⚠️ Folder yang kosong (`outputs/figures`) tetap ikut karena berisi file `.gitkeep`. File berawalan titik seperti `.gitignore` kadang tersembunyi di laptop — tidak masalah kalau tidak ikut.
6. Tulis pesan (*commit message*): `Upload struktur awal proyek` → **Commit changes**.
7. Undang anggota: **Settings → Collaborators → Add people** → masukkan username GitHub 5 teman. Mereka menerima email undangan dan harus **menerimanya**.

> Batas upload lewat browser: 100 file sekali upload. Repo ini sekitar 40 file, aman.

---

## 2. Ganti placeholder `USERNAME` dan `NAMA-REPO`

Di notebook dan README ada tulisan `USERNAME` dan `NAMA-REPO` yang harus diganti dengan username & nama repo kalian. Pilih **salah satu** cara:

### Cara A — `github.dev` (paling mudah, tanpa install apa-apa)
1. Buka halaman utama repo, lalu **tekan tombol titik `.` di keyboard** (atau ganti `github.com` di address bar menjadi `github.dev`). Editor VS Code terbuka di browser.
2. Tekan **Ctrl + Shift + H** (Mac: Cmd + Shift + H) → muncul *Search: Replace across files*.
3. Pada kolom atas ketik `USERNAME/NAMA-REPO`, kolom bawah isi `usernamemu/nama-repomu` (contoh `budi-santoso/proyek-udara-kelompok12`) → klik ikon **Replace All** (ikon dua kotak/panah di sebelah kanan) → konfirmasi.
4. Ulangi untuk dua baris ini:
   - cari `GITHUB_USER = "USERNAME"` → ganti `GITHUB_USER = "usernamemu"`
   - cari `GITHUB_REPO = "NAMA-REPO"` → ganti `GITHUB_REPO = "nama-repomu"`
5. Buka ikon **Source Control** (cabang di sisi kiri) → ketik pesan `Ganti placeholder` → klik **Commit & Push** (✔).

### Cara B — jalankan skrip (butuh Python di laptop)
```
python setup_repo.py usernamemu nama-repomu
```
lalu upload ulang file yang berubah (atau pakai Git jika sudah terbiasa).

**Cek berhasil:** buka `notebooks/00_Kenalan_Dengan_Data.ipynb` di GitHub, lihat sel setup: `GITHUB_USER` dan `GITHUB_REPO` harus sudah berisi nama asli.

---

## 3. Repo private agar aman dari plagiarisme

Dosen menyatakan memakai dataset kelompok lain = nilai 0. Repo **public** bisa dilihat semua orang, termasuk kelompok lain → risiko disalin. Karena itu **disarankan Private**.

Konsekuensi: saat Colab mengambil file dari repo private, ia butuh **kunci akses (token)**.

### Opsi A (disarankan) — Private + token
Dilakukan **tiap anggota sendiri** (jangan berbagi token lewat grup chat!):

1. Di GitHub: foto profil → **Settings** → **Developer settings** (paling bawah di kiri) → **Personal access tokens** → **Tokens (classic)** → **Generate new token (classic)**.
   - *Note:* `colab-proyek-udara`
   - *Expiration:* 60 days (cukup untuk 4 minggu + cadangan)
   - Centang **`repo`** → **Generate token** → **salin tokennya sekarang** (hanya tampil sekali).
   > Kenapa *classic*? Token "fine-grained" tidak bisa mengakses repo milik orang lain meski kamu kolaborator, jadi untuk repo yang dimiliki Project Lead, token classic yang berfungsi.
2. Di Colab, buka notebook apa saja → klik ikon **🔑 Secrets** di sisi kiri → **Add new secret**:
   - *Name:* `GITHUB_TOKEN` (huruf besar semua, persis)
   - *Value:* tempel tokennya
   - Aktifkan toggle **Notebook access**.
3. Notebook akan otomatis memakai token itu saat `git clone`. Secrets itu **tersimpan di akun Colab-mu**, jadi cukup sekali (tapi toggle "Notebook access" perlu diaktifkan di setiap notebook baru).
4. Jangan pernah menaruh token di dalam notebook, README, atau chat.

### Opsi B — Public sementara (lebih mudah, ada risiko)
Kalau token merepotkan, repo boleh *public* selama pengerjaan **dengan sadar risikonya**: kelompok lain bisa menemukan dan menyalin. Ubah jadi Private begitu proyek dikumpulkan (**Settings → Danger Zone → Change visibility**).

---

## 4. Alur kerja harian (semua anggota)

1. **Buka notebook peranmu** lewat tombol "Open in Colab" di `README.md` (klik, lalu izinkan akses GitHub jika diminta).
2. Jalankan sel **SETUP** paling atas (Shift + Enter). Pertama kali Colab akan meng-*clone* repo; tunggu sampai muncul `Setup selesai`.
3. Jalankan sel satu per satu dari atas ke bawah. **Jangan loncat**, banyak sel bergantung pada sel sebelumnya.
4. Isi bagian bertanda **✏️ ISI** dengan kata-katamu sendiri (klik dua kali sel teksnya untuk mengedit).
5. Di sel paling bawah, `unduh_hasil(...)` membuat ZIP hasil dan mengunduhnya ke laptop.
6. Unggah ke GitHub (Bagian 5) dan simpan notebook (Bagian 6).
7. **Kabari grup**: "Hasil Minggu 2 sudah di-upload ✅".

### Hal yang perlu diketahui tentang Colab
- **Sesi bisa mati** kalau didiamkan lama. Semua variabel hilang, **file di sesi itu juga hilang** → makanya hasil harus segera diunduh & di-upload.
- Kalau sesi baru: jalankan lagi SETUP dan sel-sel di atas yang dibutuhkan (*Runtime → Run all* paling gampang).
- Notebook baru yang dibuka dari GitHub selalu mengambil **versi terbaru** repo → data bersih dari Peran 2 otomatis terpakai.
- Mau mulai bersih: **Runtime → Disconnect and delete runtime**, lalu buka lagi.

---

## 5. Mengunggah hasil ke GitHub

Setelah mengunduh `hasil_xxx.zip`:
1. **Unzip** di laptop. Di dalamnya ada folder `outputs/` (dan untuk Peran 2 juga `data/`).
2. Buka repo di GitHub → **Add file → Upload files**.
3. **Seret folder `outputs`** (dan `data` bila ada) ke jendela browser. Struktur folder otomatis terjaga: file masuk ke `outputs/tables/` dan `outputs/figures/` yang benar.
4. Commit message yang baik: `Minggu 2: hasil peluang & distribusi (Peran 3)`.
5. Klik **Commit changes** (langsung ke `main` sudah oke karena tiap orang menulis file yang berbeda).

---

## 6. Menyimpan notebook yang sudah diisi

Notebook dengan kalimat ✏️ yang sudah kamu isi **harus** disimpan (itu bagian "file kerja" yang dikumpulkan). Dua cara:

- **Dari Colab langsung:** *File → Save a copy in GitHub* → pilih repo & branch `main` → *File path* isi `notebooks/NAMA_FILE_YANG_SAMA.ipynb` → OK. (Colab akan meminta izin GitHub pertama kali.) Beri pesan commit yang jelas.
- **Lewat unduh manual:** *File → Download → Download .ipynb* → di GitHub buka folder `notebooks` → **Add file → Upload files** → seret file (nama harus **sama persis** agar menimpa versi lama).

Setelah menyimpan, **cek di GitHub** bahwa tanggal edit file berubah.

---

## 7. Aturan agar tidak tabrakan

1. **Satu file = satu pemilik** (tabel pemilik ada di `docs/03_jadwal_dan_alur_kerja.md`).
2. **Jangan mengedit `data/Kelompok_12_Tema_B_Kualitas_Udara.csv`** (data asli) dan `src/helpers.py` tanpa izin Project Lead.
3. **Jangan membuka dan menyimpan notebook milik orang lain** ke GitHub — walau cuma "mencoba".
4. Dua orang tidak boleh meng-upload **file dengan nama yang sama** pada waktu yang sama. Karena nama file sudah dibedakan per minggu/peran, ini jarang terjadi.
5. Ingin tahu siapa mengubah apa? Buka file di GitHub → **History**.
6. **Salah upload?** Jangan panik: file → **History** → buka versi sebelumnya → salin isinya, atau minta Project Lead memulihkan.

---

## 8. Troubleshooting

| Masalah | Penyebab umum | Solusi |
|---|---|---|
| `RuntimeError: Gagal clone repo` | `GITHUB_USER`/`GITHUB_REPO` masih placeholder, atau repo private tanpa token, atau token kadaluarsa | Cek Bagian 2 & 3. Pastikan secret bernama persis `GITHUB_TOKEN` dan **Notebook access** aktif. |
| `remote: Repository not found` | Kamu belum menerima undangan kolaborator, atau tokennya tidak punya izin `repo` | Terima undangan di email/GitHub; buat token baru dengan centang `repo`. |
| `ModuleNotFoundError: No module named 'src'` | Sel SETUP belum dijalankan / `os.chdir` gagal | Jalankan sel SETUP paling atas dulu. |
| `FileNotFoundError: data/Kelompok_12_...csv` | Folder kerja salah atau file belum ter-upload | Jalankan SETUP; cek file ada di GitHub di folder `data/`. |
| Muncul `DRAF SEMENTARA` | Data bersih resmi belum di-upload Peran 2 | Normal di awal. Tanyakan Peran 2. Setelah ada, mulai sesi baru (Runtime → Disconnect and delete runtime) lalu jalankan ulang. |
| Hasil berbeda dari teman | Kalian memakai data yang berbeda (draf vs resmi) | Pastikan semua memakai data bersih resmi yang sama; jalankan ulang dari awal. |
| Error di tengah notebook | Sel di atasnya belum dijalankan | *Runtime → Restart session and run all*. |
| Gambar/file hilang setelah sesi mati | File di sesi Colab bersifat sementara | Selalu jalankan sel `unduh_hasil` dan upload ke GitHub segera. |
| Tidak bisa meng-clone sama sekali (darurat) | Masalah akses/jaringan | **Cara manual:** jalankan sel `import os; os.makedirs('/content/proyek/src'); os.makedirs('/content/proyek/data')`, lalu di panel **Files** (ikon folder kiri) unggah `src/helpers.py` ke `/content/proyek/src/` dan file CSV ke `/content/proyek/data/`, kemudian jalankan SETUP lagi. |
| Colab "Unable to connect to GitHub" saat Open notebook | Izin akses GitHub belum diberikan | Di dialog Colab pilih **Authorize**; centang opsi *include private repos*. |

Masih buntu? Tulis di grup: **apa yang kamu klik, pesan error lengkap (screenshot)**, dan tag Project Lead.
