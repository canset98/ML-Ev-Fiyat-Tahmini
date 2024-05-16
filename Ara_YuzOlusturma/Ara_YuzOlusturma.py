#gereken kütüphaneleri ekledik

import pandas as pd
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import Canvas
from tkinter import ttk
from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd
from sklearn import model_selection
import xgboost as xgb
from xgboost import XGBRegressor

#Veri Setini Okuyoruz

df_2 = (pd.read_csv(r"C:\Users\pvtech\Downloads\son_hali_emlakjet (1).xlsx"))
df_2.drop("Unnamed: 0", axis = 1, inplace = True)
df = df_2.copy()

#Fiyat tahmininde bize evin değerinin pahalı yada ucuz olduğunu hesapta göstermeye yarayan sütunlarımızı giriyoruz.
df = df[["ilçe","türü","net_metrekare","alan","oda_sayısı","bina_yaşı","ısıtma","site_içerisinde",
         "eşya_durumu","banyo_sayısı","wc_sayısı","dairenin_katı","fiyat"]]

X = df.drop(["fiyat"], axis = 1)
y = df["fiyat"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 144)
xgb1 = XGBRegressor(colsample_bytree = 0.5, learning_rate = 0.09, max_depth = 4, n_estimators = 2000)
model_xgb = xgb1.fit(X_train, y_train)
model_xgb.predict(X_test)[15:20]
model_xgb.score(X_test, y_test)

#BU KISMA KADAR MODELİMİZİ EĞİTTİK VE ARAYÜZE BAŞLAYABİLİRİZ
#İlk olarak bir pencere bir "nesne" oluşturuyoruz.

pencere = Tk()
pencere.title("Ev Fiyat Tahmini") #Penceremizin başlığını veriyoruz

pencere.configure(background='#81e6d9')#pencerenin arka plan rengini ve geometri ölçülerini veriyoruz.
pencere.geometry("1700x900")
pencere.state("normal")


def mesaj():
    messagebox.showinfo(title="Başarılı", message="Seçim başarılı")


def olumsuz():
    messagebox.showwarning(title="Dikkat", message="Seçim Yapmadınız") #uyarı mesajımız


# DEĞİŞKENLER

def ilce_düzenle():
    global ilce
    ilce_deger = ilce_kutu.get()
    if (ilce_deger == "Sarıyer"):
        ilce = 0
        mesaj()
    elif (ilce_deger == "Silivri"):
        ilce = 1
        mesaj()
    elif (ilce_deger == "Sultanbeyli"):
        ilce = 2
        mesaj()
    elif (ilce_deger == "Sultangazi"):
        ilce = 3
        mesaj()
    elif (ilce_deger == "Tuzla"):
        ilce = 4
        mesaj()
    elif (ilce_deger == "Zeytinburnu"):
        ilce = 5
        mesaj()
    elif (ilce_deger == "Çekmeköy"):
        ilce = 6
        mesaj()
    elif (ilce_deger == "Ümraniye"):
        ilce = 7
        mesaj()
    elif (ilce_deger == "Sultanbeyli"):
        ilce = 8
        mesaj()
    elif (ilce_deger == "Üsküdar"):
        ilce = 9
        mesaj()
    elif (ilce_deger == "Şile"):
        ilce = 10
        mesaj()
    elif (ilce_deger == "Şişli"):
        ilce = 11
        mesaj()
    else:
        olumsuz()
    print(ilce)


def tür_düzenle():
    global tür
    tür_deger = tür_kutu.get()
    if (tür_deger == "Bina"):
        tür = 0
        mesaj()
    elif (tür_deger == "Daire"):
        tür = 1
        mesaj()
    elif (tür_deger == "Köşk"):
        tür = 2
        mesaj()
    elif (tür_deger == "Müstakil"):
        tür = 3
        mesaj()
    elif (tür_deger == "Residence"):
        tür = 4
        mesaj()
    elif (tür_deger == "Villa"):
        tür = 5
        mesaj()
    elif (tür_deger == "Yalı"):
        tür = 6
        mesaj()
    elif (tür_deger == "yalı dairesi"):
        tür = 7
        mesaj()
    else:
        olumsuz()


def net_düzenle():
    global net
    net_metrekare = int(net_entry.get())
    if (net_metrekare > 0):
        net = net_metrekare
        mesaj()
        print(net_metrekare)
    else:
        olumsuz()


def oda_düzenle():
    global oda
    oda_deger = oda_kutu.get()
    if (oda_deger == "1"):
        oda = 0
        mesaj()
    elif (oda_deger == "1+1"):
        oda = 1
        mesaj()
    elif (oda_deger == "2+1"):
        oda = 2
        mesaj()
    elif (oda_deger == "2+2"):
        oda = 3
        mesaj()
    elif (oda_deger == "3+1"):
        oda = 4
        mesaj()
    elif (oda_deger == "3+2"):
        oda = 5
        mesaj()
    elif (oda_deger == "4+1"):
        oda = 6
        mesaj()
    elif (oda_deger == "4+2"):
        oda = 7
        mesaj()
    elif (oda_deger == "5+1"):
        oda = 8
        mesaj()
    elif (oda_deger == "5+2"):
        oda = 9
        mesaj()
    elif (oda_deger == "5+3"):
        oda = 10
        mesaj()
    elif (oda_deger == "6+1"):
        oda = 11
        mesaj()
    elif (oda_deger == "6+2"):
        oda = 12
        mesaj()
    elif (oda_deger == "6+3"):
        oda = 13
        mesaj()
    elif (oda_deger == "7+2"):
        oda = 14
        mesaj()
    elif (oda_deger == "7+3"):
        oda = 15
        mesaj()
    elif (oda_deger == "8+"):
        oda = 16
        mesaj()
    elif (oda_deger == "Stüdyo"):
        oda = 17
        mesaj()
    else:
        olumsuz()


def yaş_düzenle():
    global yaş
    yaş_deger = yaşlar_kutu.get()
    if (yaş_deger == "0"):
        yaş = 0
        mesaj()
    elif (yaş_deger == "1"):
        yaş = 1
        mesaj()
    elif (yaş_deger == "2"):
        yaş = 3
        mesaj()
    elif (yaş_deger == "3"):
        yaş = 5
        mesaj()
    elif (yaş_deger == "4"):
        yaş = 6
        mesaj()
    elif (yaş_deger == "5-10"):
        yaş = 7
        mesaj()
    elif (yaş_deger == "11-20"):
        yaş = 2
        mesaj()
    elif (yaş_deger == "20 ve üzeri"):
        yaş = 4
        mesaj()
    else:
        olumsuz()


def site_düzenle():
    global site
    site_deger = site_kutu.get()
    if (site_deger == "Evet"):
        site = 0
        mesaj()
    elif (site_deger == "Hayır"):
        site = 1
        mesaj()
    else:
        olumsuz()


def eşya_düzenle():
    global eşya
    eşya_deger = eşya_kutu.get()
    if (eşya_deger == "Boş"):
        eşya = 0
        mesaj()
    elif (eşya_deger == "Eşyalı"):
        eşya = 1
        mesaj()
    else:
        olumsuz()


def alan_düzenle():
    global alan
    alan_ent = int(alan_entry.get())
    if (alan_ent > 0):
        alan = alan_ent
        print(alan)
        mesaj()
    else:
        olumsuz()


def ısıtma_düzenle():
    global ısıtma
    ısıtma_deger = ısıtma_kutu.get()
    if (ısıtma_deger == "Doğalgaz Sobalı"):
        ısıtma = 0
        mesaj()
    elif (ısıtma_deger == "Güneş Enerjisi"):
        ısıtma = 1
        mesaj()
    elif (ısıtma_deger == "Isıtma Yok"):
        ısıtma = 2
        mesaj()
    elif (ısıtma_deger == "Kat Kaloriferi"):
        ısıtma = 3
        mesaj()
    elif (ısıtma_deger == "Klimalı"):
        ısıtma = 4
        mesaj()
    elif (ısıtma_deger == "Kombi Doğalgaz"):
        ısıtma = 5
        mesaj()
    elif (ısıtma_deger == "Merkezi (Pay Ölçer)"):
        ısıtma = 6
        mesaj()
    elif (ısıtma_deger == "Merkezi Doğalgaz"):
        ısıtma = 7
        mesaj()
    elif (ısıtma_deger == "Sobalı"):
        ısıtma = 8
        mesaj()
    elif (ısıtma_deger == "Yerden Isıtma"):
        ısıtma = 9
        mesaj()
    else:
        olumsuz()


def banyo_düzenle():
    global banyo
    banyo_deger = banyo_kutu.get()
    if (banyo_deger == "0"):
        banyo = 0
        mesaj()
    elif (banyo_deger == "1"):
        banyo = 1
        mesaj()
    elif (banyo_deger == "2"):
        banyo = 2
        mesaj()
    elif (banyo_deger == "3"):
        banyo = 3
        mesaj()
    elif (banyo_deger == "4"):
        banyo = 4
        mesaj()
    elif (banyo_deger == "5"):
        banyo = 5
        mesaj()
    elif (banyo_deger == "6+"):
        banyo = 6
        mesaj()
    else:
        olumsuz()


def wc_düzenle():
    global wc
    wc_deger = wc_kutu.get()
    if (wc_deger == "0"):
        wc = 0
        mesaj()
    elif (wc_deger == "1"):
        wc = 1
        mesaj()
    elif (wc_deger == "2"):
        wc = 2
        mesaj()
    elif (wc_deger == "3"):
        wc = 3
        mesaj()
    elif (wc_deger == "4"):
        wc = 4
        mesaj()
    elif (wc_deger == "5"):
        wc = 5
        mesaj()
    elif (wc_deger == "6+"):
        wc = 6
        mesaj()
    else:
        olumsuz()


def daire_düzenle():
    global daire
    daire_deger = daire_kutu.get()
    if (daire_deger == "-1"):
        daire = 0
        mesaj()
    elif (daire_deger == "-2"):
        daire = 1
        mesaj()
    elif (daire_deger == "-3"):
        daire = 2
        mesaj()
    elif (daire_deger == "1"):
        daire = 3
        mesaj()
    elif (daire_deger == "10-20"):
        daire = 4
        mesaj()
    elif (daire_deger == "2"):
        daire = 5
        mesaj()
    elif (daire_deger == "20-30"):
        daire = 6
        mesaj()
    elif (daire_deger == "3"):
        daire = 8
        mesaj()
    elif (daire_deger == "30-40"):
        daire = 9
        mesaj()
    elif (daire_deger == "4"):
        daire = 10
        mesaj()
    elif (daire_deger == "5"):
        daire = 11
        mesaj()
    elif (daire_deger == "6"):
        daire = 12
        mesaj()
    elif (daire_deger == "7"):
        daire = 13
        mesaj()
    elif (daire_deger == "8"):
        daire = 14
        mesaj()
    elif (daire_deger == "9"):
        daire = 15
        mesaj()
    elif (daire_deger == "Bahçe Katı"):
        daire = 17
        mesaj()
    elif (daire_deger == "Bahçe Dublex"):
        daire = 16
        mesaj()
    elif (daire_deger == "Bodrum"):
        daire = 18
        mesaj()
    elif (daire_deger == "Giriş"):
        daire = 19
        mesaj()
    elif (daire_deger == "Müstakil"):
        daire = 20
        mesaj()
    elif (daire_deger == "Villa Tipi"):
        daire = 21
        mesaj()
    elif (daire_deger == "Çatı Dublex"):
        daire = 22
        mesaj()
    elif (daire_deger == "Çatı Katı"):
        daire = 22
        mesaj()
    else:
        olumsuz()

    baslık_label = Label(pencere, text="EV FİYAT TAHMİNİ", font="helvetica 50", borderwidth=20, padx=550, pady=40,
                         background="#90cdf4")
    baslık_label.place(x=70, y=20)

    # İLÇE KISMI
    ilce_label = Label(text="İlçe Seçimi", font="helvetica 12", borderwidth=6)
    ilce_label.place(x=100, y=300)

    ilceler = ["Çekmeköy", "Sarıyer", "Silivri", "Sultanbeyli", "Sultangazi", "Şile", "Şişli", "Tuzla", "Ümraniye",
               "Üsküdar", "Zeytinburnu"]
    ilce_kutu = Combobox(pencere, values=ilceler)
    ilce_kutu.place(x=100, y=350)

    ilce_buton = Button(pencere, text="Seç", command=ilce_düzenle, font="helvetica 12", borderwidth=6)
    ilce_buton.place(x=100, y=400)
    # --------

    # BİNA TÜRÜ
    bina_label = Label(text="Bina Türünü Seçiniz", font="helvetica 12", borderwidth=6)
    bina_label.place(x=300, y=300)

    türler = ["Bina", "Daire", "Köşk", "Müstakil", "Residence", "Villa", "Yalı", "yalı dairesi", "yazlık",
              "çiftlik evi"]
    tür_kutu = Combobox(pencere, values=türler)
    tür_kutu.place(x=300, y=350)

    tür_buton = Button(pencere, text="Seç", command=tür_düzenle, font="helvetica 12", borderwidth=6)
    tür_buton.place(x=300, y=400)
    # ---------

    # ODA SAYISI
    oda_label = Label(text="Oda Sayısı Seçiniz", font="helvetica 12", borderwidth=6)
    oda_label.place(x=500, y=300)

    odalar = ["1", "1+1", "2+1", "2+2", "3+1", "3+2", "4+1", "4+2", "5+1", "5+2", "5+3", "6+1", "6+2", "6+3", "7+2",
              "7+3", "8+", "Stüdyo"]
    oda_kutu = Combobox(pencere, values=odalar)
    oda_kutu.place(x=500, y=350)

    oda_buton = Button(pencere, text="Seç", command=oda_düzenle, font="helvetica 12", borderwidth=6)
    oda_buton.place(x=500, y=400)
    # ---------------

    # SİTE İÇERİSİNDE
    site_label = Label(text="Site Durumunu Seçiniz", font="helvetica 12", borderwidth=6)
    site_label.place(x=700, y=300)
    siteler = ["Evet", "Hayır"]
    site_kutu = Combobox(pencere, values=siteler)
    site_kutu.place(x=700, y=350)

    site_buton = Button(pencere, text="Seç", command=site_düzenle, font="helvetica 12", borderwidth=6)
    site_buton.place(x=700, y=400)
    # ---------------------

    # EŞYA DURUMU
    eşya_label = Label(pencere, text="Eşya Durumunu Seçiniz", font="helvetica 12", borderwidth=6)
    eşya_label.place(x=100, y=500)

    eşyalar = ["Boş", "Eşyalı"]
    eşya_kutu = Combobox(pencere, values=eşyalar)
    eşya_kutu.place(x=100, y=550)

    eşya_buton = Button(pencere, text="Seç", command=eşya_düzenle, font="helvetica 12", borderwidth=6)
    eşya_buton.place(x=100, y=600)
    # -------------

    # BİNA YAŞI
    yaş_label = Label(text="Bina Yaşını Seçiniz", font="helvetica 12", borderwidth=6)
    yaş_label.place(x=300, y=500)

    yaşlar = ["0", "1", "2", "3", "4", "5-10", "11-20", "20 ve üzeri"]
    yaşlar_kutu = Combobox(pencere, values=yaşlar)
    yaşlar_kutu.place(x=300, y=550)

    yaşlar_buton = Button(pencere, text="Seç", command=yaş_düzenle, font="helvetica 12", borderwidth=6)
    yaşlar_buton.place(x=300, y=600)
    # ------------------

    # NET METREKARE
    net_label = Label(text="Net Metrekareyi Giriniz", font="helvetica 12", borderwidth=6)
    net_label.place(x=500, y=500)

    net_entry = Entry()
    net_entry.place(x=500, y=550)

    net_buton = Button(pencere, text="Seç", command=net_düzenle, font="helvetica 12", borderwidth=6)
    net_buton.place(x=500, y=600)

    # ALAN DÜZENLE
    alan_label = Label(pencere, text="Evin Alanını Girin", font="helvetica 12", borderwidth=6)
    alan_label.place(x=700, y=500)

    alan_entry = Entry()
    alan_entry.place(x=700, y=550)

    alan_buton = Button(pencere, text="Seç", command=alan_düzenle, font="helvetica 12", borderwidth=6)
    alan_buton.place(x=700, y=600)

    # ISITMA
    ısıtma_label = Label(text="Isıtma Türünü Seçiniz", font="helvetica 12", borderwidth=6)
    ısıtma_label.place(x=100, y=700)

    ısıtmalar = ["Doğalgaz Sobalı", "Güneş Enerjisi", "Isıtma Yok", "Kat Kaloriferi", "Klimalı", "Kombi Doğalgaz",
                 "Merkezi (Pay Ölçer)",
                 "Merkezi Doğalgaz", "Sobalı", "Yerden Isıtma"]
    ısıtma_kutu = Combobox(pencere, values=ısıtmalar)
    ısıtma_kutu.place(x=100, y=750)

    ısıtma_buton = Button(pencere, text="Seç", command=ısıtma_düzenle, font="helvetica 12", borderwidth=6)
    ısıtma_buton.place(x=100, y=800)
    # ---------------------

    # BANYO SAYISI
    banyo_label = Label(text="Banyo Türünü Seçiniz", font="helvetica 12", borderwidth=6)
    banyo_label.place(x=300, y=700)

    banyolar = ["0", "1", "2", "3", "4", "5", "6+"]
    banyo_kutu = Combobox(pencere, values=banyolar)
    banyo_kutu.place(x=300, y=750)

    banyo_buton = Button(pencere, text="Seç", command=banyo_düzenle, font="helvetica 12", borderwidth=6)
    banyo_buton.place(x=300, y=800)
    # --------------------

    # WC SAYISI
    wc_label = Label(text="WC Türünü Seçiniz", font="helvetica 12", borderwidth=6)
    wc_label.place(x=500, y=700)

    wcler = ["0", "1", "2", "3", "4", "5", "6+"]
    wc_kutu = Combobox(pencere, values=wcler)
    wc_kutu.place(x=500, y=750)

    wc_buton = Button(pencere, text="Seç", command=wc_düzenle, font="helvetica 12", borderwidth=6)
    wc_buton.place(x=500, y=800)
    # --------------

    # DAİRENİN KATI
    daire_label = Label(text="Daire Katını Seçiniz", font="helvetica 12", borderwidth=6)
    daire_label.place(x=700, y=700)

    daireler = ["-1", "-2", "-3", "Giriş", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10-20", "20-30", "30-40",
                "Bahçe Dublex", "Bahçe Katı", "Bodrum", "Müstakil", "Villa Tipi", "Çatı Dublex", "Çatı Katı"]
    daire_kutu = Combobox(pencere, values=daireler)
    daire_kutu.place(x=700, y=750)

    daire_buton = Button(pencere, text="Seç", command=daire_düzenle, font="helvetica 12", borderwidth=6)
    daire_buton.place(x=700, y=800)

    # ML KISIM BAŞLANGIÇ

    def hesapla():
        yeni_veri = [[ilce], [tür], [net], [alan], [oda], [yaş], [ısıtma], [site], [eşya], [banyo], [wc], [daire]]
        yeni_veri = pd.DataFrame(yeni_veri).T
        # kullanıcı seçe bastığı zaman bir değer oluşuyor o değeri de yeni_veri adında bir değişkene atadım ve bunu dataframe'e çevirerek tranzpozunu aldım yani veri setinde makine öğrenmesini aynı hale getirdim ki makine öğrenmesinde tahmin ettirebileyim.
        df_2 = yeni_veri.rename(columns={0: "ilçe",
                                         1: "türü",
                                         2: "net_metrekare",
                                         3: "alan",
                                         4: "oda_sayısı",
                                         5: "bina_yaşı",
                                         6: "ısıtma",
                                         7: "site_içerisinde",
                                         8: "eşya_durumu",
                                         9: "banyo_sayısı",
                                         10: "wc_sayısı",
                                         11: "dairenin_katı"})

        pred = model_xgb.predict(df_2)
#sonra oluşturduğum modelde df_2 ye tahmin yaptırdım.bunu da pred diye tahmine atadım.
        if (pred < 0):
            pred = -1 * pred

        pred = int(pred) #int değerine çevirdim

        s2 = Label(pencere, text=pred, font="helvetica 20", borderwidth=6, padx=200, pady=40)
        s2.place(x=1210, y=700)

    # HESAPLA
    hesapla_buton = Button(pencere, text="HESAPLA", command=hesapla, font="helvetica 15", borderwidth=60, padx=100,
                           pady=40, background="#f7fafc")
    hesapla_buton.place(x=1200, y=300)

    s1 = Label(pencere, text="", font="helvetica 12", borderwidth=6, padx=200, pady=40)
    s1.place(x=1210, y=700)