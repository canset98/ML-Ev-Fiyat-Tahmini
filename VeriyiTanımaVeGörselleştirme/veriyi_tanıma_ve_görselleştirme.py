import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# veri setini tanıma
df = (pd.read_csv(r"C:\Users\1brah1m\Downloads\ML-Ev-Fiyat-Tahmini\VeriyiTanımaVeGörselleştirme\Emlakjet.csv"))

print(df.info())

# verilerin açıklamaları (min fiyat ,max fiyat, st.sapması vs...)
print(df.describe().T)

print(df.head())

# ilçe inceleme
print(df.İlçe.value_counts())
df.İlçe.value_counts().plot.barh()
plt.show()

# yaka invceleme
print(df.yaka.value_counts())
df.yaka.value_counts().plot.barh()
plt.show()

# Kategori İnceleme(satılık çoğu)
print(df.Kategorisi.value_counts())
# Net_Metrekare İnceleme
print(df.Net_Metrekare.describe())
# Bina Yaşı
print(df.Binanın_Yaşı.value_counts())
fig = plt.figure(figsize=(5, 15))
df.Binanın_Yaşı.value_counts().plot(kind='pie', autopct='%.1f%%')
plt.ylabel("yaş", fontsize=20)
plt.show()
# Kat Sayısı
print(df.Binanın_Kat_Sayısı.value_counts())
# Dairenin Katı
print(df.Bulunduğu_Kat.value_counts())
# Kullanım Durumu
fig1 = plt.figure(figsize=(5, 15))
df.Kullanım_Durumu.value_counts().plot(kind='pie', autopct='%.1f%%')
plt.ylabel("", fontsize=20)
plt.title("Kullanım Durumu")
plt.show()
# Yatırıma Uygunluk
fig2 = plt.figure(figsize=(5, 15))
df.Yatırıma_Uygunluk.value_counts().plot(kind='pie', autopct='%.1f%%')
plt.ylabel("", fontsize=20)
plt.title("Yatırım Durumu")
plt.show()
# Eşya Durumu
fig3 = plt.figure(figsize=(5, 15))
df.Eşya_Durumu.value_counts().plot(kind='pie', autopct='%.1f%%')
plt.ylabel("", fontsize=20)
plt.title("Eşya Durumu")
plt.show()
# Banyo Sayısı
fig4 = plt.figure(figsize=(5, 15))
df.Banyo_Sayısı.value_counts().plot(kind='pie', autopct='%.1f%%')
plt.ylabel("", fontsize=14)
plt.title("Banyo Sayısı")
plt.show()
# Isıtma
print(df.Isıtma_Tipi.value_counts())
# Kredi Durumu
fig5 = plt.figure(figsize=(5, 15))
df.Krediye_Uygunluk.value_counts().plot(kind='pie', autopct='%.1f%%')
plt.ylabel("", fontsize=20)
plt.title("Kredi Durumu")
plt.show()

# Site İçerisinde
fig6 = plt.figure(figsize=(5, 15))
df.Site_İçerisinde.value_counts().plot(kind='pie', autopct='%.1f%%')
plt.ylabel("", fontsize=20)
plt.title("Site Durumu")
plt.show()
# Takas
fig7 = plt.figure(figsize=(5, 15))
df.Takas.value_counts().plot(kind='pie', autopct='%.1f%%')
plt.ylabel("", fontsize=20)
plt.title("Takas")
plt.show()

# fiyat _alan grafiği
(sns.lmplot(x='Fiyatı', y='Net_Metrekare', data=df))
plt.show()

sns.countplot(x='Kullanım_Durumu', data=df)
plt.show()

sns.barplot(x="Binanın_Yaşı", y="Fiyatı", data=df)
plt.show()
