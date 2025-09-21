import pandas as pd
from matplotlib import pyplot as plt

files = [
    "AEP_hourly.csv", "COMED_hourly.csv", "DAYTON_hourly.csv", 
    "DEOK_hourly.csv", "DOM_hourly.csv", "DUQ_hourly.csv", 
    "EKPC_hourly.csv", "FE_hourly.csv", "NI_hourly.csv", 
    "PJME_hourly.csv", "PJMW_hourly.csv"
]
base_path = "C:\\Users\\Ahmet\\Desktop\\pandas projesi\\archive\\"

paths = {f.split('_')[0]: base_path + f for f in files}


tüm_birlikler = []
print("--- Operasyon Başladı: Birlikler okunuyor... ---")
for birlik_adi, path in paths.items():
    try:
        birlik = pd.read_csv(
            path,
            parse_dates=['Datetime'],
            index_col='Datetime'
        )
        
        if not birlik.index.is_unique:
            print(f"-> '{birlik_adi}' birliğinde mükerrer kayıtlar düzeltiliyor.")
            birlik = birlik.groupby(level=0).mean()
        
        tüm_birlikler.append(birlik)
        print(f"-> '{birlik_adi}' birliği başarıyla eklendi.")

    except Exception as e:
        print(f"!!! '{birlik_adi}' birliği okunamadı. Hata: {e}")


if tüm_birlikler:
    print("\n--- Tüm veriler birleştiriliyor... ---")
    birlesik_ordu = pd.concat(tüm_birlikler, axis=1)
    birlesik_ordu.drop(columns=['AEP_MW'], inplace=True, errors='ignore')
    birlesik_ordu = birlesik_ordu.interpolate(method='time')
    birlesik_ordu['Total_MW'] = birlesik_ordu.sum(axis=1)
    elit_ordu = birlesik_ordu.loc['2013-06-01':].copy()
    print("--- Birleşik Ordu analize hazır! ---")

    elit_ordu['Yil'] = elit_ordu.index.year
    elit_ordu['Ay'] = elit_ordu.index.month
    elit_ordu['Haftanin_Gunu'] = elit_ordu.index.day_name()


    print("\n--- Grafik 1/3: Genel Aylık Trend oluşturuluyor... ---")
    aylik_rapor = elit_ordu.resample('ME').mean(numeric_only=True)
    aylik_rapor['Total_MW'].plot(
        title='Aylık Ortalama Toplam Enerji Tüketimi (Genel Trend)', 
        figsize=(14, 7)
    )
    plt.ylabel('Ortalama Megawatt (MW)')
    plt.xlabel('Tarih')
    plt.grid(True)
    plt.show()


    print("--- Grafik 2/3: Mevsimsel Döngü Analizi oluşturuluyor... ---")
    aylik_dongu = elit_ordu.groupby('Ay')['Total_MW'].mean()
    aylik_dongu.plot(
        kind='bar', 
        title='Yıl İçindeki Ortalama Aylık Enerji Tüketim Döngüsü',
        figsize=(12, 6),
        color='teal'
    )
    plt.xlabel('Ay')
    plt.ylabel('Ortalama Megawatt (MW)')
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.show()


    print("--- Grafik 3/3: Haftalık Döngü Analizi oluşturuluyor... ---")
    haftalik_dongu = elit_ordu.groupby('Haftanin_Gunu')['Total_MW'].mean()
    gun_siralama = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    haftalik_dongu = haftalik_dongu.reindex(gun_siralama)
    haftalik_dongu.plot(
        kind='bar',
        title='Haftalık Ortalama Enerji Tüketim Döngüsü',
        figsize=(12, 6),
        color='darkslateblue'
    )
    plt.xlabel('Haftanın Günü')
    plt.ylabel('Ortalama Megawatt (MW)')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

    print("--- Grafik 4/4: Günlük Saatlik Döngü Analizi oluşturuluyor... ---")

    elit_ordu['Saat'] = elit_ordu.index.hour

    gunluk_dongu = elit_ordu.groupby('Saat')['Total_MW'].mean()

    print("Günün Saatlerine Göre Ortalama Tüketim Raporu:")
    print(gunluk_dongu)

    gunluk_dongu.plot(
        kind='line',
        title='Gün İçindeki Ortalama Saatlik Enerji Tüketim Döngüsü',
        figsize=(12, 6),
        color='red',
        marker='o' 
    )
    plt.xlabel('Günün Saati (0-23)')
    plt.ylabel('Ortalama Megawatt (MW)')
    plt.xticks(ticks=range(0, 24, 1)) 
    plt.grid(True)
    plt.show()
    
    print("\n--- Karşılaştırmalı Analiz Başlıyor: Birlikler Gözetleniyor... ---")

    karsilastirma_raporu = aylik_rapor[['Total_MW', 'COMED_MW', 'DOM_MW', 'DAYTON_MW']]

    karsilastirma_raporu.plot(
        title='Toplam Tüketim ve Seçili Birliklerin Karşılaştırması',
        figsize=(15, 8)
    )
    plt.ylabel('Ortalama Megawatt (MW)')
    plt.xlabel('Tarih')
    plt.grid(True)
    plt.legend(title='Birlikler')
    plt.show()

    print("\n--- Operasyon Başarıyla Tamamlandı! ---")

else:
    print("Hiçbir veri okunamadığı için operasyon başarısız oldu.")