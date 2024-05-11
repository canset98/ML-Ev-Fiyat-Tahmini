import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# veri setini tanıma
df =(pd.read_excel(r"C:\Users\90555\Downloads\zingat2.xlsx"))

print(df.info())

#verilerin açıklamaları (min fiyat ,max fiyat, st.sapması vs...)
print(df.describe().T)

print(df.head())

# Kullanım Durumu sütununun değerlerini sayma ve grafik çizme(Boş,Kiracı oturuyor,Mülk sahibi)
ax = df.iloc[:, 14].value_counts().plot.barh()
# Grafik başlığı eklemek
ax.set_title("Kullanım Durumu Değer Sayımları")
# Grafik penceresini göster
plt.show()





# Sütun veri tiplerini kontrol et
print(df.dtypes)


#türleri gösteriyoruz(Daire,Bina ,Villa ,vs..)
print(df.iloc[:,10].value_counts())

#Kategori İnceleme(satılık çoğu)
print(df.iloc[:,3].value_counts())

#Alan İnceleme
print(df.iloc[:,4].describe())

# Oda sütununun değerlerini sayma ve grafik çizme
ay = df.iloc[:, 5].value_counts().plot.barh()
# Grafik başlığı eklemek
ay.set_title("Oda Sütunu Değer Sayımları")
# Grafik penceresini göster
plt.show()

#Kat Sayısı
print(df.iloc[:,6].value_counts())

#Isıtma
print(df.iloc[:,7].value_counts())

#Bina Yaşı
print(df.iloc[:,12].value_counts())


#verilerin metrik bilgiler içerdiği için verileri temizliyoruz ('110 m2' gibi)
df[df.columns[11]] = pd.to_numeric(df[df.columns[11]].str.replace(' m2', ''), errors='coerce')
df[df.columns[15]] = pd.to_numeric(df[df.columns[15]].str.replace(' m2', ''), errors='coerce')

# NaN değerlerle başa çıkmak
df.dropna(subset=[df.columns[11], df.columns[15]], inplace=True)

sns.lmplot(x=df.columns[11], y=df.columns[15], data=df)
plt.ylim(0,8100)
plt.xlim(0,1.5)
# Grafiği göster
plt.show()