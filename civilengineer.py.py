import numpy as np

def taşıma_gücü_hesaplama():
    print("Taşıma Gücü Hesaplama Aracı")
    
    # Hesaplama için girişleri al
    qk = float(input("Temel taşıma gücü karakteristik dayanımı (qk) girin [kN/m²]: "))
    qo = float(input("Temel seviyesinde etkiyen düşey yük, kesme ve moment etkilerinin oluşturduğu temel taban basıncı (qo) girin [kN/m²]: "))
    γRv = float(input("Temel taşıma gücü dayanım katsayısı (γRv) girin: "))
    Nq = float(input("Taşıma Gücü Katsayısı (Nq) girin: "))
    Nc = float(input("Taşıma Gücü Katsayısı (Nc) girin: "))
    Ng = float(input("Taşıma Gücü Katsayısı (Ng) girin: "))
    sc = float(input("Temel Şekli Katsayısı (sc) girin: "))
    sq = float(input("Temel Şekli Katsayısı (sq) girin: "))
    sg = float(input("Temel Şekli Katsayısı (sg) girin: "))
    dc = float(input("Derinlik Katsayısı (dc) girin: "))
    dq = float(input("Derinlik Katsayısı (dq) girin: "))
    dg = float(input("Derinlik Katsayısı (dg) girin: "))
    bc = float(input("Temel Taban Eğimi Katsayısı (bc) girin: "))
    bq = float(input("Temel Taban Eğimi Katsayısı (bq) girin: "))
    bg = float(input("Temel Taban Eğimi Katsayısı (bg) girin: "))
    gc = float(input("Temel Zemin Eğimi Katsayısı (gc) girin: "))
    gq = float(input("Temel Zemin Eğimi Katsayısı (gq) girin: "))
    gg = float(input("Temel Zemin Eğimi Katsayısı (gg) girin: "))
    ic = float(input("Yükleme Eğikliği Katsayısı (ic) girin: "))
    iq = float(input("Yükleme Eğikliği Katsayısı (iq) girin: "))
    ig = float(input("Yükleme Eğikliği Katsayısı (ig) girin: "))
    
    # Taşıma gücü hesaplama formülü
    qt = (Nc * sc * dc * bc + Nq * sq * dq * bq + Ng * sg * dg * bg) * qk + (ic * gc + iq * gq + ig * gg) * qk * γRv
    
    # Sonucu yazdır
    print("Temel taşıma gücü tasarım dayanımı (qt):", qt, "kN/m²")


def kesit_optimizasyonu():
    print("Kesit Optimizasyonu Aracı")
    
    # Hesaplama için girişleri al
    M = float(input("Etki eden moment değerini girin [kNm]: "))
    sigma_y = float(input("Malzeme akma dayanımını girin [MPa]: "))
    
    # Kesit boyutlarını hesapla
    d = ((16 * M) / (np.pi * sigma_y)) ** 0.5
    b = (M / (sigma_y * d ** 2)) * 1000
    
    # Sonucu yazdır
    print("Optimize edilmiş kesit boyutları:")
    print("d =", d, "mm")
    print("b =", b, "mm")


def beton_miktarı_hesaplama():
    print("Beton Miktarı Hesaplama Aracı")
    
    # Hesaplama için girişleri al
    uzunluk = float(input("Yapının uzunluğunu girin [m]: "))
    genislik = float(input("Yapının genişliğini girin [m]: "))
    yukseklik = float(input("Yapının yüksekliğini girin [m]: "))
    duvar_kalinligi = float(input("Duvar kalınlığını girin [cm]: "))
    
    # Beton miktarını hesapla
    alan = 2 * (uzunluk + genislik) * yukseklik + (uzunluk * genislik)
    hacim = alan * duvar_kalinligi / 100
    
    # Sonucu yazdır
    print("Beton miktarı:", hacim, "m³")


def izleme_ve_raporlama():
    print("İzleme ve Raporlama Aracı")
    
    # Hesaplama için girişleri al
    proje_adi = input("Proje adını girin: ")
    izleme_sonuclari = input("İzleme sonuçlarını girin: ")
    
    # Rapor oluştur
    rapor = f"Proje Adı: {proje_adi}\nİzleme Sonuçları: {izleme_sonuclari}"
    
    # Raporu dosyaya yazdır
    dosya_adi = f"{proje_adi}_raporu.txt"
    with open(dosya_adi, "w") as dosya:
        dosya.write(rapor)
    
    # Sonucu yazdır
    print("Rapor oluşturuldu ve", dosya_adi, "adlı dosyaya kaydedildi.")


def ana_menu():
    while True:
        print("\n--- İnşaat Mühendisliği Hesaplama Aracı ---")
        print("1. Taşıma Gücü Hesaplama")
        print("2. Kesit Optimizasyonu")
        print("3. Beton Miktarı Hesaplama")
        print("4. İzleme ve Raporlama")
        print("5. Çıkış")

        secim = input("Bir seçenek girin (1-5): ")

        if secim == "1":
            taşıma_gücü_hesaplama()
        elif secim == "2":
            kesit_optimizasyonu()
        elif secim == "3":
            beton_miktarı_hesaplama()
        elif secim == "4":
            izleme_ve_raporlama()
        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek, tekrar deneyin.")

ana_menu()
