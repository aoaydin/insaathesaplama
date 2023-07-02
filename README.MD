
# İnşaat Mühendisliği Hesaplama Aracı

Bu, inşaat mühendisleri için geliştirilmiş bir hesaplama aracıdır. İnşaat projelerinde yaygın olarak kullanılan bazı hesaplamaları gerçekleştirmek ve raporlama yapmak için kullanılabilir. Bu araç, Python programlama dilinde yazılmıştır ve basit bir metin tabanlı arayüze sahiptir.

## Özellikler

Bu hesaplama aracı aşağıdaki hesaplamaları gerçekleştirebilir:

1. Taşıma Gücü Hesaplama: Temel taşıma gücünü hesaplamak için gerekli olan parametreleri alır ve sonucu yazdırır.
2. Kesit Optimizasyonu: Etki eden moment değeri ve malzeme akma dayanımı kullanılarak optimize edilmiş kesit boyutlarını hesaplar ve sonucu yazdırır.
3. Beton Miktarı Hesaplama: Bir yapının beton miktarını hesaplamak için gerekli olan parametreleri alır ve sonucu yazdırır.
4. İzleme ve Raporlama: Bir proje için izleme sonuçlarını alır, bir rapor oluşturur ve raporu bir dosyaya kaydeder.

## Kullanım

Bu hesaplama aracını kullanmak için aşağıdaki adımları izleyin:

1. Python yüklü olmalıdır. Eğer Python yüklü değilse, Python'ı [buradan](https://www.python.org/downloads/) indirip kurun.
2. Bu hesaplama aracının kaynak kodlarını bilgisayarınıza indirin.
3. İndirdiğiniz klasöre terminal veya komut istemcisinden erişin.
4. Ana menüyü başlatmak için aşağıdaki komutu çalıştırın:

   ```bash
   python main.py
   ```

# Gerekli Paketleri Yükleme
Bu hesaplama aracını kullanmak için öncelikle gerekli paketleri yüklemeniz gerekmektedir. Aşağıdaki komutu çalıştırarak gerekli paketleri yükleyebilirsiniz:

```bash
pip install numpy
```



Bu kod, inşaat mühendisleri için çeşitli hesaplamaları yapmak için bir hesaplama aracıdır. İnşaat mühendislerinin yaygın olarak kullandığı bazı hesaplamaları gerçekleştirebilir ve raporlamalarını yapabilir.

Kodun ana bölümü, `ana_menu()` fonksiyonunu içerir. Bu fonksiyon, kullanıcıya bir dizi seçenek sunar ve seçimlerine göre ilgili hesaplamaları yapar. Aşağıda, kodun her bir bölümünün işlevini ve kullanımını açıklayan ayrıntılı bir açıklama bulunmaktadır:

1. `taşıma_gücü_hesaplama()`: Bu fonksiyon, temel taşıma gücünü hesaplar. Kullanıcıdan temel taşıma gücü karakteristik dayanımı (qk), temel seviyesinde etkiyen düşey yük, kesme ve moment etkilerinin oluşturduğu temel taban basıncı (qo), taşıma gücü katsayıları (Nq, Nc, Ng), temel şekli katsayıları (sc, sq, sg), derinlik katsayıları (dc, dq, dg), temel taban eğimi katsayıları (bc, bq, bg), temel zemin eğimi katsayıları (gc, gq, gg) ve yükleme eğikliği katsayıları (ic, iq, ig) gibi girişleri alır ve taşıma gücünü hesaplayarak sonucu yazdırır.

2. `kesit_optimizasyonu()`: Bu fonksiyon, etki eden moment değeri ve malzeme akma dayanımı kullanılarak optimize edilmiş kesit boyutlarını hesaplar. Moment değeri (M) ve malzeme akma dayanımı (sigma_y) girişlerini alır ve kesit boyutlarını (d ve b) hesaplayarak sonucu yazdırır.

3. `beton_miktarı_hesaplama()`: Bu fonksiyon, bir yapının beton miktarını hesaplar. Yapının uzunluğu (uzunluk), genişliği (genişlik), yüksekliği (yükseklik) ve duvar kalınlığı (duvar_kalinligi) gibi girişleri alır ve beton miktarını hesaplayarak sonucu yazdırır.

4. `izleme_ve_raporlama()`: Bu fonksiyon, bir projenin izleme sonuçlarını alarak bir rapor oluşturur ve dosyaya kaydeder. Kullanıcıdan proje adı (proje_adi) ve izleme sonuçları (izleme_sonuclari) gibi girişleri alır, bir rapor oluşturur ve bu raporu bir dosyaya kaydederek sonucu yazdırır.

5. `ana_menu()`: Bu fonksiyon, kullanıcıya ana menüyü gösterir

 ve kullanıcının seçimlerine göre ilgili hesaplamaları yapar veya programdan çıkar. Kullanıcı 1-5 arasında bir seçim yapar ve seçimine göre ilgili hesaplama fonksiyonunu çağırır. Geçerli olmayan bir seçim yapılırsa, hata mesajı verilir ve tekrar seçim yapması istenir.

Bu kod, kullanıcının çeşitli inşaat mühendisliği hesaplamalarını yapmasına olanak tanır ve sonuçları kullanıcıya sunar. Ayrıca, kullanıcının izleme sonuçlarını raporlamasını sağlar ve bu raporu bir dosyaya kaydeder.




# Civil Engineering Calculation Tool

This is a calculation tool developed for civil engineers. It can be used to perform and report some commonly used calculations in construction projects. This tool is written in the Python programming language and has a simple text-based interface.

## Features

This calculation tool can perform the following calculations:

1. Bearing Capacity Calculation: Takes the required parameters to calculate the bearing capacity of a foundation and prints the result.
2. Section Optimization: Calculates the optimized dimensions of a section based on the applied moment and material yield strength, and prints the result.
3. Concrete Quantity Calculation: Takes the required parameters to calculate the quantity of concrete for a structure and prints the result.
4. Monitoring and Reporting: Takes monitoring results for a project, generates a report, and saves the report to a file.

## Usage

To use this calculation tool, follow these steps:

1. Make sure Python is installed. If Python is not installed, you can download and install it from [here](https://www.python.org/downloads/).
2. Download the source code of this calculation tool to your computer.
3. Navigate to the downloaded folder using a terminal or command prompt.
4. Run the following command to start the main menu:

   ```bash
   python main.py```

# Installing Required Packages
To use this calculation tool, you need to install the required packages. You can install them by running the following command:

```bash
pip install numpy
```

This command will install the `numpy` package. This package is necessary for performing mathematical operations used in the calculations. Make sure Python is installed before using the `pip` command.

This code is a calculation tool for performing various calculations commonly used in civil engineering and generating reports.
