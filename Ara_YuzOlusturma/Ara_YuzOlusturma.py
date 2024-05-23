from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import Canvas
from tkinter import ttk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import xgboost as xgb
from xgboost import XGBRegressor

# Veri Setini Okuyoruz
df_2 = pd.read_csv(r"C:\Users\pvtech\Downloads\son_hali_emlakjet.csv")
df_2.drop("Unnamed: 0", axis=1, inplace=True)
df = df_2.copy()

# Fiyat tahmininde bize evin değerinin pahalı yada ucuz olduğunu hesapta göstermeye yarayan sütunlarımızı giriyoruz...
df = df[['İlçe', 'Krediye_Uygunluk', 'Net_Metrekare', 'Brüt_Metrekare', 'Oda_Sayısı', 'Binanın_Yaşı', 'Isıtma_Tipi', 'Site_İçerisinde', 'Eşya_Durumu', 'Banyo_Sayısı', 'Yatırıma_Uygunluk', 'Bulunduğu_Kat','Fiyatı']]

X = df.drop(["Fiyatı"], axis=1)
y = df["Fiyatı"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=144)

xgb1 = XGBRegressor(colsample_bytree=0.5, learning_rate=0.09, max_depth=4, n_estimators=2000)
model_xgb = xgb1.fit(X_train, y_train)

# BU KISMA KADAR MODELİMİZİ EĞİTTİK VE ARAYÜZE BAŞLAYABİLİRİZ
# İlk olarak bir pencere bir "nesne" oluşturuyoruz.
pencere = Tk()
pencere.title("Ev Fiyat Tahmini")  # Penceremizin başlığını veriyoruz
pencere.configure(background='#1E2762')  # Pencerenin arka plan rengini ve geometri ölçülerini veriyoruz.
pencere.geometry("2000x2000")
pencere.state("normal")


def mesaj():
    messagebox.showinfo(title="Başarılı", message="Seçim başarılı")


def olumsuz():
    messagebox.showwarning(title="Dikkat", message="Seçim Yapmadınız")  # uyarı mesajımız


# DEĞİŞKENLER
def İlçe_düzenle():
    global İlçe
    İlçe_deger = İlçe_kutu.get()
    if İlçe_deger == "Avcılar":
        İlçe = 0
        mesaj()
    elif İlçe_deger == "Bahçelievler":
        İlçe = 1
        mesaj()
    elif İlçe_deger == "Bakırköy":
        İlçe = 2
        mesaj()
    elif İlçe_deger == "Bağcılar":
        İlçe = 3
        mesaj()
    elif İlçe_deger == "Başakşehir":
        İlçe = 4
        mesaj()
    elif İlçe_deger == "Beylikdüzü":
        İlçe = 5
        mesaj()
    elif İlçe_deger == "Beşiktaş":
        İlçe = 6
        mesaj()
    elif İlçe_deger == "Esenyurt":
        İlçe = 7
        mesaj()
    elif İlçe_deger == "Kadıköy":
        İlçe = 8
        mesaj()
    elif İlçe_deger == "Maltepe":
        İlçe = 9
        mesaj()
    elif İlçe_deger == "Pendik":
        İlçe = 10
        mesaj()
    elif İlçe_deger == "Sarıyer":
        İlçe = 11
        mesaj()

    elif İlçe_deger == "Şişli":
        İlçe = 12
        mesaj()

    else:
        olumsuz()
    print(İlçe)

#kredi
def Kredi_düzenle():
    global Kredi
    kredi_deger = kredi_kutu.get()  # == yerine = kullanarak değeri atıyoruz
    if kredi_deger == "Bilinmiyor":
        Kredi = 0
        mesaj()
    elif kredi_deger == "Krediye Uygun":
        Kredi = 1
        mesaj()

    elif kredi_deger == "Krediye Uygun Değil":
        Kredi = 2
        mesaj()

    else:
        olumsuz()
    print(Kredi)




def net_düzenle():
    global net
    net_metrekare = int(net_entry.get())
    if net_metrekare > 0:
        net = net_metrekare
        mesaj()
        print(net_metrekare)
    else:
        olumsuz()


def oda_düzenle():
    global oda
    oda_deger = oda_kutu.get()
    if oda_deger == "1 Oda":
        oda = 0
        mesaj()
    elif oda_deger == "1+1":
        oda = 1
        mesaj()
    elif oda_deger == "1.5+1":
        oda = 2
        mesaj()
    elif oda_deger == "2+0":
        oda = 3
        mesaj()
    elif oda_deger == "2+1":
        oda = 4
        mesaj()
    elif oda_deger == "2+2":
        oda = 5
        mesaj()
    elif oda_deger == "2.5+1":
        oda = 6
        mesaj()
    elif oda_deger == "3+1":
        oda = 7
        mesaj()
    elif oda_deger == "3+2":
        oda = 8
        mesaj()
    elif oda_deger == "3.5+1":
        oda = 9
        mesaj()
    elif oda_deger == "4+1":
        oda = 10
        mesaj()
    elif oda_deger == "4+2":
        oda = 11
        mesaj()
    elif oda_deger == "4.5+1":
        oda = 12
        mesaj()
    elif oda_deger == "5+1":
        oda = 13
        mesaj()
    elif oda_deger == "5+2":
        oda = 14
        mesaj()
    elif oda_deger == "5+3":
        oda = 15
        mesaj()
    elif oda_deger == "6+1":
        oda = 16
        mesaj()
    elif oda_deger == "6+2":
        oda = 17
        mesaj()
    elif oda_deger == "6+3":
        oda = 18
        mesaj()
    elif oda_deger == "6+4":
        oda = 19
        mesaj()
    elif oda_deger == "7+1":
        oda = 20
        mesaj()
    elif oda_deger == "7+2":
        oda = 21
        mesaj()
    elif oda_deger == "8+Oda":
        oda = 22
        mesaj()
    elif oda_deger == "Stüdyo":
        oda = 23
        mesaj()
    else:
        olumsuz()
    print(oda)

def yaş_düzenle():
    global yaş
    yaş_deger = yaşlar_kutu.get()
    if yaş_deger == "0":
        yaş = 0
        mesaj()
    elif yaş_deger == "1":
        yaş = 1
        mesaj()
    elif yaş_deger == "11-15":
        yaş = 2
        mesaj()
    elif yaş_deger == "16-20":
        yaş = 3
        mesaj()
    elif yaş_deger == "2":
        yaş = 4
        mesaj()
    elif yaş_deger == "21 Ve Üzeri":
        yaş = 5
        mesaj()
    elif yaş_deger == "3":
        yaş = 6
        mesaj()
    elif yaş_deger == "4":
        yaş = 7
        mesaj()
    elif yaş_deger == "5-10":
        yaş = 8
        mesaj()
    else:
        olumsuz()
    print(yaş)

def site_düzenle():
    global site
    site_deger = site_kutu.get()
    if site_deger == "Evet":
        site = 0
        mesaj()
    elif site_deger == "Hayır":
        site = 1
        mesaj()
    else:
        olumsuz()
    print(site)

def eşya_düzenle():
    global eşya
    eşya_deger = eşya_kutu.get()
    if eşya_deger == "Var":
        eşya = 0
        mesaj()
    elif eşya_deger == "Yok":
        eşya = 1
        mesaj()
    else:
        olumsuz()
    print(eşya)

def alan_düzenle():
    global alan
    alan_ent = int(alan_entry.get())
    if alan_ent > 0:
        alan = alan_ent
        print(alan)
        mesaj()
    else:
        olumsuz()


def ısıtma_düzenle():
    global ısıtma
    ısıtma_deger = ısıtma_kutu.get()
    if ısıtma_deger == "Doğalgaz":
        ısıtma = 0
        mesaj()
    elif ısıtma_deger == "Isıtma Yok":
        ısıtma = 1
        mesaj()
    elif ısıtma_deger == "Klimalı":
        ısıtma = 2
        mesaj()
    elif ısıtma_deger == "Sobalı":
        ısıtma = 3
        mesaj()
    elif ısıtma_deger == "Yerden Isıtma":
        ısıtma = 4
        mesaj()
    else:
        olumsuz()
    print(ısıtma)

def banyo_düzenle():
    global banyo
    banyo_deger = banyo_kutu.get()
    if banyo_deger == "0":
        banyo = 0
        mesaj()
    elif banyo_deger == "1":
        banyo = 1
        mesaj()
    elif banyo_deger == "15":
        banyo = 2
        mesaj()
    elif banyo_deger == "2":
        banyo = 3
        mesaj()
    elif banyo_deger == "3":
        banyo = 4
        mesaj()
    elif banyo_deger == "4":
        banyo = 5
        mesaj()
    elif banyo_deger == "5":
        banyo = 6
        mesaj()
    elif banyo_deger == "6":
        banyo = 7
        mesaj()
    else:
        olumsuz()
    print(banyo)
 #Yatırım
def Yatırım_düzenle():
    global Yatırım
    yatırım_deger = yatırım_kutu.get()  # == yerine = kullanarak değeri atıyoruz
    if yatırım_deger == "Bilinmiyor":
        Yatırım  = 0
        mesaj()
    elif yatırım_deger == "Yatırıma Uygun":
        Yatırım = 1
        mesaj()
    elif yatırım_deger == "Yatırıma Uygun Değil":
        Yatırım = 2
        mesaj()
    else:
        olumsuz()
    print(Yatırım)

def daire_düzenle():
    global daire
    daire_deger = daire_kutu.get()
    if daire_deger == "-1":
        daire = 0
        mesaj()
    elif daire_deger == "-2":
        daire = 1
        mesaj()
    elif daire_deger == "-3":
        daire = 2
        mesaj()
    elif daire_deger == "1":
        daire = 3
        mesaj()
    elif daire_deger == "10-20":
        daire = 4
        mesaj()
    elif daire_deger == "2":
        daire = 5
        mesaj()
    elif daire_deger == "21-29":
        daire = 6
        mesaj()
    elif daire_deger == "3":
        daire = 7
        mesaj()
    elif daire_deger == "30-40":
        daire = 8
        mesaj()
    elif daire_deger == "4":
        daire = 9
        mesaj()
    elif daire_deger == "5":
        daire = 10
        mesaj()
    elif daire_deger == "6":
        daire = 11
        mesaj()
    elif daire_deger == "7":
        daire = 12
        mesaj()
    elif daire_deger == "8":
        daire = 13
        mesaj()
    elif daire_deger == "9":
        daire = 14
        mesaj()
    elif daire_deger == "Bodrum":
        daire = 15
        mesaj()
    elif daire_deger == "Giriş":
        daire = 16
        mesaj()
    elif daire_deger == "Çatı Katı":
        daire = 17
        mesaj()
    else:
        olumsuz()
    print(daire)

baslık_label = Label(pencere, text="EV FİYAT TAHMİNİ", font="helvetica 50", borderwidth=20, padx=350, pady=40, background="#7B2049")
baslık_label.place(x=70, y=20)

# İLÇE KISMI
ilce_label = Label(text="İlçe Seçimi", font="helvetica 12", borderwidth=6,background='#418EC6')
ilce_label.place(x=100, y=250)

İlçeler = ["Avcılar", "Bahçelievler", "Bakırköy", "Bağcılar", "Başakşehir", "Beylikdüzü", "Beşiktaş", "Esenyurt", "Kadıköy", "Maltepe", "Pendik","Sarıyer","Şişli"]
İlçe_kutu = Combobox(pencere, values=İlçeler)
İlçe_kutu.place(x=100, y=300)

ilce_buton = Button(pencere, text="Seç", command=İlçe_düzenle, font="helvetica 12", borderwidth=6,background='#418EC6')
ilce_buton.place(x=100, y=350)

#Krediye Uygunluk
kredi_label=Label(text="Krediye Uygunluk", font="helvetica 12", borderwidth=6,background='#418EC6')
kredi_label.place(x=300, y=250)

uygunluk = ["Bilinmiyor","Krediye Uygun","Krediye Uygun Değil"]
kredi_kutu = Combobox(pencere, values=uygunluk)
kredi_kutu.place(x=300,y=300)

kredi_buton = Button(pencere, text="Seç", command=Kredi_düzenle, font="helvetica 12", borderwidth=6,background='#418EC6')
kredi_buton.place(x=300, y=350)



# ODA SAYISI
oda_label = Label(text="Oda Sayısı Seçiniz", font="helvetica 12", borderwidth=6,background='#418EC6')
oda_label.place(x=500, y=250)

odalar = ["1 Oda", "1+1", "1.5+1", "2+0", "2+1", "2+2", "2.5+1", "3+1", "3+2", "3.5+1", "4+1", "4+2", "4.5+1", "5+1", "5+2", "5+3", "6+1","6+2","6+3","6+4","7+1","7+2","8+Oda","Stüdyo"]
oda_kutu = Combobox(pencere, values=odalar)
oda_kutu.place(x=500, y=300)

oda_buton = Button(pencere, text="Seç", command=oda_düzenle, font="helvetica 12", borderwidth=6,background='#418EC6')
oda_buton.place(x=500, y=350)

# SİTE İÇERİSİNDE
site_label = Label(text="Site Durumunu Seçiniz", font="helvetica 12", borderwidth=6,background='#418EC6')
site_label.place(x=700, y=250)
siteler = ["Evet", "Hayır"]
site_kutu = Combobox(pencere, values=siteler)
site_kutu.place(x=700, y=300)

site_buton = Button(pencere, text="Seç", command=site_düzenle, font="helvetica 12", borderwidth=6,background='#418EC6')
site_buton.place(x=700, y=350)

# EŞYA DURUMU
eşya_label = Label(pencere, text="Eşya Durumunu Seçiniz", font="helvetica 12", borderwidth=6,background='#418EC6')
eşya_label.place(x=100, y=450)

eşyalar = ["Var", "Yok"]
eşya_kutu = Combobox(pencere, values=eşyalar)
eşya_kutu.place(x=100, y=500)

eşya_buton = Button(pencere, text="Seç", command=eşya_düzenle, font="helvetica 12", borderwidth=6,background='#418EC6')
eşya_buton.place(x=100, y=550)

# BİNA YAŞI
yaş_label = Label(text="Bina Yaşını Seçiniz", font="helvetica 12", borderwidth=6,background='#418EC6')
yaş_label.place(x=300, y=450)

yaşlar = ["0", "1", "11-15", "16-20", "2", "21 Ve Üzeri", "3", "4","5-10"]
yaşlar_kutu = Combobox(pencere, values=yaşlar)
yaşlar_kutu.place(x=300, y=500)

yaşlar_buton = Button(pencere, text="Seç", command=yaş_düzenle, font="helvetica 12", borderwidth=6,background='#418EC6')
yaşlar_buton.place(x=300, y=550)

# NET METREKARE
net_label = Label(text="Net Metrekareyi Giriniz", font="helvetica 12", borderwidth=6,background='#418EC6')
net_label.place(x=500, y=450)

net_entry = Entry()
net_entry.place(x=500, y=500)

net_buton = Button(pencere, text="Seç", command=net_düzenle, font="helvetica 12", borderwidth=6,background='#418EC6')
net_buton.place(x=500, y=550)

# BRÜT METREKARE DÜZENLE
alan_label = Label(pencere, text="Brüt Metrekaresini Girin", font="helvetica 12", borderwidth=6,background='#418EC6')
alan_label.place(x=700, y=450)

alan_entry = Entry()
alan_entry.place(x=700, y=500)

alan_buton = Button(pencere, text="Seç", command=alan_düzenle, font="helvetica 12", borderwidth=6,background='#418EC6')
alan_buton.place(x=700, y=550)

# ISITMA
ısıtma_label = Label(text="Isıtma Türünü Seçiniz", font="helvetica 12", borderwidth=6,background='#418EC6')
ısıtma_label.place(x=100, y=650)

ısıtmalar = ["Doğalgaz", "Isıtma Yok", "Klimalı", "Sobalı", "Yerden Isıtma"]
ısıtma_kutu = Combobox(pencere, values=ısıtmalar)
ısıtma_kutu.place(x=100, y=700)

ısıtma_buton = Button(pencere, text="Seç", command=ısıtma_düzenle, font="helvetica 12", borderwidth=6,background='#418EC6')
ısıtma_buton.place(x=100, y=750)

# BANYO SAYISI
banyo_label = Label(text="Banyo Türünü Seçiniz", font="helvetica 12", borderwidth=6,background='#418EC6')
banyo_label.place(x=300, y=650)

banyolar = ["0", "1", "15", "2", "3", "4", "5","6"]
banyo_kutu = Combobox(pencere, values=banyolar)
banyo_kutu.place(x=300, y=700)

banyo_buton = Button(pencere, text="Seç", command=banyo_düzenle, font="helvetica 12", borderwidth=6,background='#418EC6')
banyo_buton.place(x=300, y=750)

#YATIRIMA UYGUNLUK
yatırım_label=Label(text="Yatırıma Uygunluk", font="helvetica 12", borderwidth=6,background='#418EC6')
yatırım_label.place(x=500, y=650)

uygunluk = ["Bilinmiyor","Yatırıma Uygun","Yatırıma Uygun Değil"]
yatırım_kutu = Combobox(pencere, values=uygunluk)
yatırım_kutu.place(x=500,y=700)

yatırım_buton = Button(pencere, text="Seç", command=Yatırım_düzenle, font="helvetica 12", borderwidth=6,background='#418EC6')
yatırım_buton.place(x=500, y=750)

# DAİRENİN KATI
daire_label = Label(text="Daire Katını Seçiniz", font="helvetica 12", borderwidth=6,background='#418EC6')
daire_label.place(x=700, y=650)

daireler = ["-1", "-2", "-3", "1", "10-20", "2", "21-29", "3", "30-40", "4", "5", "6", "7", "8", "9", "Bodrum", "Giriş", "Çatı Katı"]
daire_kutu = Combobox(pencere, values=daireler)
daire_kutu.place(x=700, y=700)

daire_buton = Button(pencere, text="Seç", command=daire_düzenle, font="helvetica 12", borderwidth=6,background='#418EC6')
daire_buton.place(x=700, y=750)

# ML KISIM BAŞLANGIÇ
def hesapla():
    # Daha önce belirlenmiş değişkenlerden yeni bir DataFrame oluşturuyoruz.
    yeni_veri = pd.DataFrame({
        "İlçe": [İlçe],
        "Krediye_Uygunluk": [Kredi],
        "Net_Metrekare": [net],
        "Brüt_Metrekare": [alan],
        "Oda_Sayısı": [oda],
        "Binanın_Yaşı": [yaş],
        "Isıtma_Tipi": [ısıtma],
        "Site_İçerisinde": [site],
        "Eşya_Durumu": [eşya],
        "Banyo_Sayısı": [banyo],
        "Yatırıma_Uygunluk": [Yatırım],
        "Bulunduğu_Kat": [daire]
    })

    # Modeli kullanarak tahmin yapıyoruz.
    pred = model_xgb.predict(yeni_veri)

    # Tahmin edilen değeri görselleştiriyoruz.
    if pred < 0:
        pred = -1 * pred
    pred = int(pred)
    s2 = Label(pencere, text=f"Tahmini Fiyat: {pred} TL", font="helvetica 20", borderwidth=6, padx=40, pady=35,background='#418EC6')
    s2.place(x=1100, y=600)

# HESAPLA
hesapla_buton = Button(pencere, text="HESAPLA", command=hesapla, font="helvetica 15", borderwidth=60, padx=65, pady=40,background='#418EC6')
hesapla_buton.place(x=1200, y=300)



# Pencere döngüsünü başlat
pencere.mainloop()