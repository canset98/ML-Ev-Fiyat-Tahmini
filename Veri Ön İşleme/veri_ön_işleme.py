import pandas as pd

from sklearn import preprocessing  # etiketleme işlemi için gerekli kütüphane


# Veri setini okuma işlemi gerçekleştiriyoruz.
df = (pd.read_csv(r"C:\Users\1brah1m\Downloads\ML-Ev-Fiyat-Tahmini\VeriyiTanımaVeGörselleştirme\Emlakjet.csv"))
print(df.head())

print(df.columns)
# Sütun adlarını gösterir.

# Sütunların verilerini ve hangisi veriden kaç tane olduğunu görürüz.
for column in df.columns:
    print(f" {column}:")
    print(df[column].unique())
    print(df[column].value_counts())
    print("\n")

# Sadece metin türündeki sütunlarda baştaki ve sondaki boşlukları kaldırır
for column in df.select_dtypes(include=['object']).columns:
    df[column] = df[column].str.strip()


# Sütunlarda işlemler:

# Hayır olan yatırıma uygunluk durumunu yatırıma uygun değil olarak değiştirdik.
df.loc[df.Yatırıma_Uygunluk == "Hayır", "Yatırıma_Uygunluk"] = "Yatırıma Uygun değil"
# Evet olan yatırıma uygunluk durumunu yatırıma uygun olarak değiştirdik.
df.loc[df.Yatırıma_Uygunluk == "Evet", "Yatırıma_Uygunluk"] = "Yatırıma Uygun"

# KREDIYE UYGUN yazısını Krediye Uygun olarak değiştirdik.
df.loc[df.Krediye_Uygunluk == "KREDIYE UYGUN", "Krediye_Uygunluk"] = "Krediye Uygun"

# Bazı gereksiz sütunları kaldırdık.
df.drop(["İlan_Numarası", "İlan_Güncelleme_Tarihi", "İlan_Oluşturma_Tarihi"], axis=1, inplace=True)

# '0 (Yeni)' şeklinde yazan bina yaşını sıfır yaptık
df.loc[df.Binanın_Yaşı == "0 (Yeni)", "Binanın_Yaşı"] = "0"


# Banyo sayısı kısmında düzeltme yaptık ve integera çevirdik.
df.loc[df.Banyo_Sayısı == "Yok", "Banyo_Sayısı"] = 0
df.loc[df.Banyo_Sayısı == "1", "Banyo_Sayısı"] = 1
df.loc[df.Banyo_Sayısı == "2", "Banyo_Sayısı"] = 2
df.loc[df.Banyo_Sayısı == "3", "Banyo_Sayısı"] = 3
df.loc[df.Banyo_Sayısı == "4", "Banyo_Sayısı"] = 4
df.loc[df.Banyo_Sayısı == "5", "Banyo_Sayısı"] = 5
df.loc[df.Banyo_Sayısı == "6+", "Banyo_Sayısı"] = 6
df.loc[df.Banyo_Sayısı == "15", "Banyo_Sayısı"] = 15
df.loc[df.Banyo_Sayısı == "1075", "Banyo_Sayısı"] = 6
df.loc[df.Banyo_Sayısı == "Var", "Banyo_Sayısı"] = 1
df.loc[df.Banyo_Sayısı == "28 M2", "Banyo_Sayısı"] = 1
df.loc[df.Banyo_Sayısı == "Genel Fiyat", "Banyo_Sayısı"] = 1


# Fiyat durumunda evet kısmını genel fiyat olarak değiştirdik.
df.loc[df.Fiyat_Durumu == "Evet", "Fiyat_Durumu"] = 'Genel Fiyat'
# Fiyat durumunda hayırı bilinmiyora çevirdik.
df.loc[df.Fiyat_Durumu == "Hayır", "Fiyat_Durumu"] = 'Bilinmiyor'

# Yaptığımız değişiklikleri kaydettik.
df.to_csv('emlakjet_2.csv')



# çok fazla ve karmaşık veriler olduğu için düzenleme gerçekleştiriceğiz.
df.loc[df.Bulunduğu_Kat == "Düz Giriş", "Bulunduğu_Kat"] = "Giriş"
df.loc[df.Bulunduğu_Kat == "Bahçe Katı", "Bulunduğu_Kat"] = "Giriş"
df.loc[df.Bulunduğu_Kat == "Yüksek Giriş", "Bulunduğu_Kat"] = "Giriş"
df.loc[df.Bulunduğu_Kat == "Müstakil", "Bulunduğu_Kat"] = "Giriş"
df.loc[df.Bulunduğu_Kat == "Villa Tipi", "Bulunduğu_Kat"] = "Giriş"

df.loc[df.Bulunduğu_Kat == "Tam Bodrum", "Bulunduğu_Kat"] = "Bodrum"

df.loc[df.Bulunduğu_Kat == "Çatı Dubleks" , "Bulunduğu_Kat"] = "Çatı Katı"

df.loc[df.Bulunduğu_Kat == "1. Kat", "Bulunduğu_Kat"] = "1"
df.loc[df.Bulunduğu_Kat == "2. Kat", "Bulunduğu_Kat"] = "2"
df.loc[df.Bulunduğu_Kat == "3. Kat", "Bulunduğu_Kat"] = "3"
df.loc[df.Bulunduğu_Kat == "4. Kat", "Bulunduğu_Kat"] = "4"
df.loc[df.Bulunduğu_Kat == "5. Kat", "Bulunduğu_Kat"] = "5"
df.loc[df.Bulunduğu_Kat == "6. Kat", "Bulunduğu_Kat"] = "6"
df.loc[df.Bulunduğu_Kat == "7. Kat", "Bulunduğu_Kat"] = "7"
df.loc[df.Bulunduğu_Kat == "8. Kat", "Bulunduğu_Kat"] = "8"
df.loc[df.Bulunduğu_Kat == "9. Kat", "Bulunduğu_Kat"] = "9"

df.loc[df.Bulunduğu_Kat == "10. Kat", "Bulunduğu_Kat"] = "10-20"
df.loc[df.Bulunduğu_Kat == "11. Kat", "Bulunduğu_Kat"] = "10-20"
df.loc[df.Bulunduğu_Kat == "12. Kat", "Bulunduğu_Kat"] = "10-20"
df.loc[df.Bulunduğu_Kat == "13. Kat", "Bulunduğu_Kat"] = "10-20"
df.loc[df.Bulunduğu_Kat == "14. Kat", "Bulunduğu_Kat"] = "10-20"
df.loc[df.Bulunduğu_Kat == "15. Kat", "Bulunduğu_Kat"] = "10-20"
df.loc[df.Bulunduğu_Kat == "16. Kat", "Bulunduğu_Kat"] = "10-20"
df.loc[df.Bulunduğu_Kat == "17. Kat", "Bulunduğu_Kat"] = "10-20"
df.loc[df.Bulunduğu_Kat == "18. Kat", "Bulunduğu_Kat"] = "10-20"
df.loc[df.Bulunduğu_Kat == "19. Kat", "Bulunduğu_Kat"] = "10-20"
df.loc[df.Bulunduğu_Kat == "20. Kat", "Bulunduğu_Kat"] = "10-20"

df.loc[df.Bulunduğu_Kat == "21. Kat", "Bulunduğu_Kat"] = "21-29"
df.loc[df.Bulunduğu_Kat == "22. Kat", "Bulunduğu_Kat"] = "21-29"
df.loc[df.Bulunduğu_Kat == "23. Kat", "Bulunduğu_Kat"] = "21-29"
df.loc[df.Bulunduğu_Kat == "24. Kat", "Bulunduğu_Kat"] = "21-29"
df.loc[df.Bulunduğu_Kat == "25. Kat", "Bulunduğu_Kat"] = "21-29"
df.loc[df.Bulunduğu_Kat == "26. Kat", "Bulunduğu_Kat"] = "21-29"
df.loc[df.Bulunduğu_Kat == "27. Kat", "Bulunduğu_Kat"] = "21-29"
df.loc[df.Bulunduğu_Kat == "28. Kat", "Bulunduğu_Kat"] = "21-29"
df.loc[df.Bulunduğu_Kat == "29. Kat", "Bulunduğu_Kat"] = "21-29"

df.loc[df.Bulunduğu_Kat == "30. Kat", "Bulunduğu_Kat"] = "30-40"

df.loc[df.Bulunduğu_Kat == "10-20. Kat", "Bulunduğu_Kat"] = "10-20"
df.loc[df.Bulunduğu_Kat == "30-40. Kat", "Bulunduğu_Kat"] = "30-40"

df.loc[df.Bulunduğu_Kat == "Kot 1 (-1). Kat" , "Bulunduğu_Kat"] = "-1"
df.loc[df.Bulunduğu_Kat == "Kot 2 (-2). Kat" , "Bulunduğu_Kat"] = "-2"
df.loc[df.Bulunduğu_Kat == "Kot 3 (-3). Kat" , "Bulunduğu_Kat"] = "-3"



# Etiketleme için nesne oluşturduk.
le = preprocessing.LabelEncoder()

# Etiketleme genelde kategorik verilere yapılır.
# Kategorik veriler, genellikle metin şeklindeki (string) etiketler içeren sütunlardır. Bu veriler sayısal olmayan verilerdir.

# Kategorik sütunları etiketleme ve tersine çevirme

#kategorik sütunlar
categorical_columns = [
    'İlçe', 'Türü', 'Kategorisi', 'Binanın_Yaşı', 'Kullanım_Durumu',
    'Yatırıma_Uygunluk', 'Eşya_Durumu', 'Oda_Sayısı', 'Bulunduğu_Kat',
    'Isıtma_Tipi', 'Krediye_Uygunluk', 'Site_İçerisinde', 'Takas',
    'Fiyat_Durumu', 'İl', 'Mahalle', 'yaka'
]

# 'Banyo_Sayısı' sütunu verilerini metin türüne çevirerek etiketleme işlemi yaparız.
df['Banyo_Sayısı'] = df['Banyo_Sayısı'].astype(str)
categorical_columns.append('Banyo_Sayısı')


# her bir sütun için döngü ile etiketleme işlemi
# Her kategorik sütuna göre döngü başlat
encoded_values = {}
for column in categorical_columns:
    # Her sütundaki metin türündeki verileri sayısal değerlere dönüştür
    df[column] = le.fit_transform(df[column])
    # etiketleme işlemi yaptık..
    # Dönüştürülen benzersiz değerleri al
    unique_encoded_values = df[column].unique()
    # Sayısal değerleri tekrar metin türüne çevir
    inverse_transformed_values = le.inverse_transform(unique_encoded_values)
    # Oluşan sayısal ve metin değerleri eşleştirerek sözlüğe ekle
    encoded_values[column] = dict(zip(unique_encoded_values, inverse_transformed_values))



# kontrol için
# Tüm kategorik sütunlar için dönüştürülen değerleri ve karşılık gelen orijinal metinleri yazdır
for column, mappings in encoded_values.items():
    print(f"Sütun: {column}")
    for encoded_value, original_value in mappings.items():
        print(f"{encoded_value}: {original_value}")
    print("\n")



# Son halini excel ve csv dosyası olarak kaydediyoruz.
df.to_excel("son_hali_emlakjet.xlsx")
df.to_csv("son_hali_emlakjet.csv")