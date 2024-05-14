import pandas as pd

from sklearn import preprocessing  #etiketleme işlemi için gerekli kütüphane


# veri setini okuma işlemi gerçekleştiriyoruz.
df = (pd.read_csv(r"C:\Users\1brah1m\Downloads\ML-Ev-Fiyat-Tahmini\VeriyiTanımaVeGörselleştirme\Emlakjet.csv"))
print(df.head())

print(df.columns)
# sütun adlarını gösterir.


# sütunların verilerini ve hangisi veriden kaç tane olduğunu görürüz.
for column in df.columns:
    print(f" {column}:")
    print(df[column].unique())
    print(df[column].value_counts())
    print("\n")


# Sadece metin türündeki sütunlarda baştaki ve sondaki boşlukları kaldırır
for column in df.select_dtypes(include=['object']).columns:
    df[column] = df[column].str.strip()


# sütunlarda işlemler:

# hayır olan yatırıma uygunluk durumunu yatırıma uygun değile çevirdik.
df.loc[df.Yatırıma_Uygunluk == "Hayır" "Yatırıma_Uygunluk"] = "Yatırıma Uygun değil"
# evet olan yatırıma uygunluk durumunu yatırıma uyguna çevirdik (yatırıma uygun zaten vardı; üstüne ekleme yaptık)
df.loc[df.Yatırıma_Uygunluk == "Evet" "Yatırıma_Uygunluk"] = "Yatırıma Uygun"

# KREDIYE UYGUN yazısını Krediye Uygun a çevirdik.
df.loc[df.Krediye_Uygunluk == "KREDIYE UYGUN" "Krediye_Uygunluk"] = "Krediye Uygun"

# bazı gereksiz sütunları kaldırdık.
df.drop(["İlan_Numarası", "İlan_Güncelleme_Tarihi", "İlan_Oluşturma_Tarihi"], axis = 1, inplace = True)

# bu şekilde yazan bina yaşını sıfır yaptık
df.loc[df.Binanın_Yaşı == "0 (Yeni)" "Binanın_Yaşı"] = "0"

# banyo sayısı kısmında düzeltme yaptık ve integera çevirdik.
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

# fiyat durumunda evet kısmını genel fiyat olarak değiştirdik.
df.loc[df.Fiyat_Durumu == "Evet", "Fiyat_Durumu"] = 'Genel Fiyat'
# fiyat durumunda hayırı bilinmiyora çevirdik.
df.loc[df.Fiyat_Durumu == "Hayır", "Fiyat_Durumu"] = 'Bilinmiyor'


# yaptığımız değişiklikleri kaydettik.
df.to_csv('emlakjet_2.csv')


df_2 = df.copy()
df_3 = df.copy()


# etiketleme için nesne oluşturduk.
le = preprocessing.LabelEncoder()


# Etiketleme genelde kategorik verilere yapılır.
# Kategorik veriler, genellikle metin şeklindeki (string) etiketler içeren sütunlardır. Bu veriler sayısal olmayan verilerdir.


# transform işlemi yaparak etiketleme yapmış oluruz.
df_3["İlçe"] = le.fit_transform(df_2.İlçe)

print(le.classes_)
# etiketlediğimiz verilerin neler olduğuna bakarız.

print(df_3.İlçe.unique())
# etiketlenmiş verilerin karşılığını öğreniriz.
le.inverse_transform([1])
le.inverse_transform([3])
le.inverse_transform([7])
le.inverse_transform([10])
# etiketledikten sonra hangi değerin hangi veriye karşılık geldiğini tek tek öğrenebiliriz.


df_3["Türü"] = le.fit_transform(df_2.Türü)
df_3["Kategorisi"] = le.fit_transform(df_2.Kategorisi)
df_3["Binanın_Yaşı"] = le.fit_transform(df_2.Binanın_Yaşı)
df_3["Kullanım_Durumu"] = le.fit_transform(df_2.Kullanım_Durumu)
df_3["Yatırıma_Uygunluk"] = le.fit_transform(df_2.Yatırıma_Uygunluk)
df_3["Eşya_Durumu"] = le.fit_transform(df_2.Eşya_Durumu)
df_3["Oda_Sayısı"] = le.fit_transform(df_2.Oda_Sayısı)
df_3["Bulunduğu_Kat"] = le.fit_transform(df_2.Bulunduğu_Kat)
df_3["Isıtma_Tipi"] = le.fit_transform(df_2.Isıtma_Tipi)
df_3["Krediye_Uygunluk"] = le.fit_transform(df_2.Krediye_Uygunluk)
df_3["Site_İçerisinde"] = le.fit_transform(df_2.Site_İçerisinde)
df_3["Takas"] = le.fit_transform(df_2.Takas)
df_3["Fiyat_Durumu"] = le.fit_transform(df_2.Fiyat_Durumu)
df_3["İl"] = le.fit_transform(df_2.İl)
df_3["İlçe"] = le.fit_transform(df_2.İlçe)
df_3["Mahalle"] = le.fit_transform(df_2.Mahalle)
df_3["yaka"] = le.fit_transform(df_2.yaka)

# bütün kategorik (string verili) değerleri etiketledi. (fit_trasform işlemi)


# 'Banyo_Sayısı' sütunu verilerini metin türüne çevirerek etiketleme işlemi yaparız.
df_2['Banyo_Sayısı'] = df_2['Banyo_Sayısı'].astype(str)
df_3["Banyo_Sayısı"] = le.fit_transform(df_2.Banyo_Sayısı)

# Bulunduğu_Kat daki değişkenlere bakıp bir düzenleme yapıcaz.
print(df.Bulunduğu_Kat.value_counts())

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

# yaptığımız değişiklikleri kontrol etmek için
print(df.Bulunduğu_Kat.value_counts())
print(df.Bulunduğu_Kat.unique())

# etiketleme
df_3["Bulunduğu_Kat"] = le.fit_transform(df_2.Bulunduğu_Kat)

# kontrol amaçlı tekrar yazdırıyoruz.
for column in df_3.columns:
    print(f" {column}:")
    print(df_3[column].value_counts())
    print(df_3[column].unique())
    print("\n")


# son halini excel ve csv dosyası olarak kaydediyoruz.
df_3.to_excel("son_hali_emlakjet.xlsx")
df_3.to_csv("son_hali_emlakjet.csv")
