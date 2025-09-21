# Zaman Serisi Analizi ile Enerji Tüketim Desenleri Keşfi

Bu proje, çeşitli ABD enerji sağlayıcılarından alınan saatlik enerji tüketim verilerini analiz ederek, tüketimdeki temel desenleri ve döngüleri ortaya çıkarmayı amaçlamaktadır. Proje, birden fazla ham veri dosyasının birleştirilmesinden başlayarak, veri temizleme, öznitelik mühendisliği ve çeşitli zaman ölçeklerinde görselleştirme adımlarını içermektedir.

## 📈 Yapılan Analizler

Bu proje kapsamında aşağıdaki analizler gerçekleştirilmiştir:

* **Genel Trend Analizi:** Yıllar içindeki aylık ortalama enerji tüketiminin genel eğilimi incelenmiştir.
* **Mevsimsel Döngü Analizi:** Enerji tüketiminin yılın hangi aylarında arttığı ve azaldığı (yaz/kış zirveleri) analiz edilmiştir.
* **Haftalık Döngü Analizi:** Hafta içi ve hafta sonu arasındaki tüketim farkları ortaya konulmuştur.
* **Günlük (Saatlik) Döngü Analizi:** Tüketimin 24 saatlik bir dilim içindeki değişimi (gece/gündüz farkları) incelenmiştir.
* **Karşılaştırmalı Analiz:** Toplam tüketim ile en büyük paya sahip birkaç bölgenin tüketim desenleri karşılaştırılmıştır.

## 🛠️ Kullanılan Teknolojiler

* **Python 3.x**
* **Pandas:** Veri manipülasyonu, temizleme ve analizi için.
* **Matplotlib:** Veri görselleştirme ve grafik oluşturma için.

## 📊 Veri Seti

Bu çalışmada kullanılan veri seti, AEP, COMED, DAYTON gibi 11 farklı enerji sağlayıcısının 2004-2018 yılları arasındaki saatlik enerji tüketim (Megawatt cinsinden) kayıtlarını içermektedir. Veriler, birden fazla CSV dosyası olarak temin edilmiştir.

## 🚀 Kurulum ve Kullanım

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1.  **Repository'yi klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI-ADINIZ/PROJE-ADINIZ.git](https://github.com/KULLANICI-ADINIZ/PROJE-ADINIZ.git)
    ```

2.  **Veri Yolu'nu Güncelleyin:**
    `main.py` betiği içindeki `base_path` değişkenini, CSV dosyalarının kendi bilgisayarınızda bulunduğu klasör yolu ile güncelleyin.

3.  **Betiği Çalıştırın:**
    ```bash
    python main.py
    ```
    *Betiği çalıştırdığınızda, analizler sırasıyla yapılacak ve ilgili grafikler ekranda gösterilecektir.*
