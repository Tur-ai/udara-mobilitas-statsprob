alpha = 0.05
keputusan_f = "H0 ditolak (model signifikan secara simultan)" if model.f_pvalue < alpha else "Gagal menolak H0 (model tidak signifikan secara simultan)"
keputusan_t1 = "signifikan secara parsial" if model.pvalues["Volume_Kendaraan"] < alpha else "tidak signifikan secara parsial"
keputusan_t2 = "signifikan secara parsial" if model.pvalues["Kecepatan_Angin_KmJ"] < alpha else "tidak signifikan secara parsial"

narasi = f"""
=== DRAF INTERPRETASI REGRESI (UNTUK reports/draft/03_interpretasi_hasil_per_uji.md) ===
1. Persamaan Regresi:
   {persamaan}
   - Konstanta (b0 = {b0:.4f}): Nilai prediksi dasar Indeks_PM25 ketika Volume_Kendaraan = 0 dan Kecepatan_Angin_KmJ = 0.
   - Koefisien Volume_Kendaraan (b1 = {b1:.4f}): Setiap kenaikan 1 satuan Volume_Kendaraan mengubah rata-rata Indeks_PM25 sebesar {b1:+.4f} poin dengan asumsi Kecepatan_Angin_KmJ tetap.
   - Koefisien Kecepatan_Angin_KmJ (b2 = {b2:.4f}): Setiap kenaikan 1 km/jam Kecepatan_Angin_KmJ mengubah rata-rata Indeks_PM25 sebesar {b2:+.4f} poin dengan asumsi Volume_Kendaraan tetap.

2. Koefisien Determinasi:
   - R-squared = {model.rsquared:.4f} ({model.rsquared*100:.2f}%): Sebesar {model.rsquared*100:.2f}% variasi Indeks_PM25 dapat dijelaskan oleh Volume_Kendaraan dan Kecepatan_Angin_KmJ, sedangkan {(1-model.rsquared)*100:.2f}% dijelaskan oleh faktor lain di luar model.
   - Adjusted R-squared = {model.rsquared_adj:.4f}.

3. Uji Signifikansi Simultan (Uji-F):
   - F-statistik = {model.fvalue:.4f}, p-value = {model.f_pvalue:.4e} (alpha = {alpha}) -> {keputusan_f}.

4. Uji Signifikansi Parsial (Uji-t):
   - Volume_Kendaraan: t = {model.tvalues['Volume_Kendaraan']:.4f}, p-value = {model.pvalues['Volume_Kendaraan']:.4e} -> {keputusan_t1}.
   - Kecepatan_Angin_KmJ: t = {model.tvalues['Kecepatan_Angin_KmJ']:.4f}, p-value = {model.pvalues['Kecepatan_Angin_KmJ']:.4e} -> {keputusan_t2}.
"""
print(narasi)