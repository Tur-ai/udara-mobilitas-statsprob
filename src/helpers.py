"""
helpers.py - fungsi bantu yang dipakai SEMUA notebook.
Jangan diubah tanpa sepengetahuan Project Lead (kalau diubah, semua notebook ikut berubah).
"""
import os
import sys
import zipfile
import numpy as np
import pandas as pd

# ---------------------------------------------------------------- konfigurasi
NO_KELOMPOK = 12
FILE_MENTAH = "data/Kelompok_12_Tema_B_Kualitas_Udara.csv"
FILE_BERSIH = "data/Kelompok_12_data_bersih.csv"   # dibuat oleh Data Engineer
DIR_FIG = "outputs/figures"
DIR_TAB = "outputs/tables"
ALPHA = 0.05

KOLOM_NUMERIK = ["Volume_Kendaraan", "Kecepatan_Angin_KmJ", "Suhu_Celcius", "Indeks_PM25"]
KOLOM_KATEGORI = ["Zona_Lokasi", "Jenis_Hari", "Jam_Sibuk", "Status_Udara"]
URUTAN_STATUS = ["Baik", "Sedang", "Tidak Sehat"]
URUTAN_ZONA = ["Pusat Kota", "Kawasan Kampus", "Pinggiran"]
WARNA_STATUS = {"Baik": "#2e9e5b", "Sedang": "#f2b134", "Tidak Sehat": "#d64545"}
WARNA_ZONA = {"Pusat Kota": "#c0392b", "Kawasan Kampus": "#2980b9", "Pinggiran": "#27ae60"}

# ---------------------------------------------------------------- memuat data
def muat_data_mentah():
    """Data asli persis seperti dari dosen (belum dibersihkan)."""
    return pd.read_csv(FILE_MENTAH)


def _rapikan_tipe(df):
    df = df.copy()
    df["Status_Udara"] = pd.Categorical(df["Status_Udara"], categories=URUTAN_STATUS, ordered=True)
    return df


def muat_data_bersih(tampilkan_info=True):
    """
    Memuat data yang sudah dibersihkan Data Engineer (data/Kelompok_12_data_bersih.csv).
    Kalau file itu BELUM ada, dipakai DRAF SEMENTARA supaya kamu bisa mulai belajar/coding dulu.
    Hasil final WAJIB memakai data bersih resmi dari Data Engineer.
    """
    if os.path.exists(FILE_BERSIH):
        df = pd.read_csv(FILE_BERSIH)
        sumber = "DATA BERSIH RESMI (dari Data Engineer)"
    else:
        df = muat_data_mentah()
        df = df.dropna(subset=["Indeks_PM25"])
        df["Kecepatan_Angin_KmJ"] = df["Kecepatan_Angin_KmJ"].fillna(df["Kecepatan_Angin_KmJ"].median())
        df = df[df["Indeks_PM25"] <= 150]
        sumber = "!!! DRAF SEMENTARA !!! (data bersih resmi belum di-upload; jangan pakai untuk laporan final)"
    df = _rapikan_tipe(df)
    if tampilkan_info:
        print(f"Sumber data : {sumber}")
        print(f"Jumlah baris: {len(df)} | Jumlah kolom: {df.shape[1]}")
    return df


# ---------------------------------------------------------------- menyimpan hasil
_DISIMPAN = []   # daftar file yang disimpan pada sesi ini (dipakai unduh_hasil)


def _catat(path):
    if path not in _DISIMPAN:
        _DISIMPAN.append(path)


def simpan_gambar(fig, nama, dpi=200):
    """Simpan gambar ke outputs/figures/<nama>.png"""
    os.makedirs(DIR_FIG, exist_ok=True)
    path = f"{DIR_FIG}/{nama}.png"
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor="white")
    print(f"[tersimpan] {path}")
    _catat(path)
    return path


def simpan_tabel(df, nama, index=True):
    """Simpan tabel ke outputs/tables/<nama>.csv"""
    os.makedirs(DIR_TAB, exist_ok=True)
    path = f"{DIR_TAB}/{nama}.csv"
    df.to_csv(path, index=index, encoding="utf-8-sig")
    print(f"[tersimpan] {path}")
    _catat(path)
    return path


def simpan_teks(teks, nama):
    """Simpan catatan teks ke outputs/tables/<nama>.txt"""
    os.makedirs(DIR_TAB, exist_ok=True)
    path = f"{DIR_TAB}/{nama}.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(teks)
    print(f"[tersimpan] {path}")
    _catat(path)
    return path


# ---------------------------------------------------------------- unduh hasil dari Colab
def unduh_hasil(nama_zip, file_tambahan=()):
    """
    Kumpulkan SEMUA file yang disimpan (simpan_gambar/simpan_tabel/simpan_teks) pada sesi notebook ini
    + file_tambahan, jadikan 1 file ZIP bernama <nama_zip>.zip, lalu unduh (di Colab).
    Struktur folder di dalam ZIP sama dengan struktur repo, jadi tinggal di-upload ke GitHub.
    """
    daftar = list(file_tambahan) + [f for f in _DISIMPAN if f not in file_tambahan]
    nama_zip = nama_zip if nama_zip.endswith(".zip") else nama_zip + ".zip"
    with zipfile.ZipFile(nama_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for f in daftar:
            z.write(f)
    print(f"{len(daftar)} file dimasukkan ke {nama_zip}:")
    for f in daftar:
        print("  -", f)
    if "google.colab" in sys.modules:
        from google.colab import files
        files.download(nama_zip)
    else:
        print("(bukan di Colab - ZIP ada di folder kerja)")
    return nama_zip


# ---------------------------------------------------------------- fungsi statistik kecil
def batas_iqr(seri):
    """Mengembalikan (Q1, Q3, IQR, batas_bawah, batas_atas) dengan aturan pagar 1.5 x IQR."""
    s = seri.dropna()
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    return q1, q3, iqr, q1 - 1.5 * iqr, q3 + 1.5 * iqr


def status_dari_pm25(x):
    """Aturan kategori yang tampak di data: <=35 Baik, 35-65 Sedang, >65 Tidak Sehat."""
    if pd.isna(x):
        return np.nan
    if x <= 35:
        return "Baik"
    if x <= 65:
        return "Sedang"
    return "Tidak Sehat"
