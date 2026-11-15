"""
Mengganti placeholder USERNAME dan NAMA-REPO di semua file .md dan .ipynb.

Cara pakai (dijalankan SEKALI oleh Project Lead, di laptop yang sudah ada Python):
    python setup_repo.py NAMA_USER_GITHUB NAMA_REPO
Contoh:
    python setup_repo.py budi-santoso proyek-udara-k12

Belum punya Python di laptop? Pakai cara 'github.dev' di docs/02_panduan_github_colab.md (Bagian 2).
"""
import sys, pathlib

if len(sys.argv) != 3:
    sys.exit(__doc__)
user, repo = sys.argv[1], sys.argv[2]
akar = pathlib.Path(__file__).parent
n = 0
for p in akar.rglob("*"):
    if p.suffix in {".md", ".ipynb"} and ".git" not in p.parts:
        teks = p.read_text(encoding="utf-8")
        baru = teks.replace("USERNAME/NAMA-REPO", f"{user}/{repo}")
        baru = baru.replace('GITHUB_USER = "USERNAME"', f'GITHUB_USER = "{user}"')
        baru = baru.replace('GITHUB_REPO = "NAMA-REPO"', f'GITHUB_REPO = "{repo}"')
        if baru != teks:
            p.write_text(baru, encoding="utf-8"); n += 1
print(f"Selesai. {n} file diperbarui. Sekarang commit & push/upload perubahan ke GitHub.")
