from selenium import webdriver
import time
import pandas as pd

# Bu fonksyon listeyi string türüne çevirir.
def listToString(s):
    # Boş bir string baslatiyoruz
    str1 = " "
    return (str1.join(s))
    # return string

# Bu aşamada selenium ile veri çekmeye başlıyoruz.
# chrome driverin yolunu veriyoruz. Selenium u kullanmak için gereklidir.
driver_path = "C:/Users/User/Desktop/BUÜ MF BMB/Python/Yeni klasör/chromedriver-win64/chromedriver-win64/chromedriver.exe"
# browser adında bir değişken oluşturuyoruz ve driver yolumuzu veriyoruz,bunu ortam değişkenlerine eklememiz gerekiyor öncesinde
browser = webdriver.Chrome(driver_path)
# browser get ile verdiğimiz adres de ki web sitesine gitmiş oluyoruz.
browser.get("https://www.emlakjet.com/satilik-konut/istanbul-sariyer/")

# şimdi bu sayfa içinde her linke tıklayarak verileri çekeceğiz sonra o sayfadan çıkıp bi altında ki evin linke girip onun
# verilerini alarak sırayla bu işlemi devam ettireceğiz.

# Şuan da web sitesinin arayüzündeyiz. Amacımız evlerin detaylarına bakmak için linke tıklamak. Bunu da xpathlere göre yapacağız
# neden hepsini tek döngü de yapmadık. çünkü arada reklamlar olduğu için pathler karışıyor. Reklamları atlamak için
# böyle bi yol izledik

i = 1
while i<=2:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(i) + "]")
    # tıkla adında değişkene find diyerek bu xpath de 1. olana gidiyor.
    # click diyerek de bu linke tıklıyor ve evin detaylarına bakmak için sayfaya girmiş oluyoruz.
    tıkla.click()
    # özelliklerin hepsini almak için bu sefer bu kod ile oradaki css bloğuna göre veriyi çekeceğiz.
    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")
    # özellikleri bir önceki kodda aldık şimdi de evin fiyatını alıyoruz ve değişkene kaydediyoruz.
    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    # 2 tane boş liste oluşturuyoruz. Elimizdeki dağınık veriyi düzenleyip listeye atacağız.
    detaylar = []
    fiyat = []
    # çektiğimiz veriler text string olmadığı için verileri stringe çevirip demin oluşturduğumuz boş listeye atıyoruz.
    # çünkü verileri çektiğinizde liste olarak gelir.
    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    # özellikleri de stringe çevirerek listeye atıyoruz.
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
    # elimizde string olan liste halinde veriler var Önceden oluşturduğumuz listeden stringe çevirme fonksyonuyla stringe
    # çeviyoruzs
    det_str = listToString(detaylar)
    # string verimizi split ile satırlara göre ayırıyoruz. Ve ayrı adında değişkene atıyoruz.
    ayrı = det_str.split("\n")
    # Az once oluşturduğumuz ayrı değişkenini DataFrame çeviriyoruz Cunku calismasi daha kolay oluyor
    df = pd.DataFrame(ayrı)
    # Verimizdeki gereksiz verilerden kurtulmak için onları ayırıyoruz.
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]
    # değişiklikler yaptığımız için indexlerde kayma oldu, indexleri resetliyoruz,satir numaralarini duzenlemis oluyoruz
    df_yeni = df_yeni.reset_index()
    # gereksiz olusan index sütununu siliyoruz,reset_index yaptigimiz icin bize fazladan index adinda bir sutun veriyor
    # Bu sutundan da kurtulmak icin drop,index,axis=1 yani sutun islemi yapacagimizi belirtiyoruz,inplace=True yapiyoruz
    # inplace default olarak False gelir,True yaparsak da direkt kaydetmis olur
    df_yeni.drop("index", axis=1, inplace=True)
    # verilerimizi tekrar listeye çeviriyoruz.
    df_liste = df_yeni.values.tolist()
    # icerikler adında bos liste olusturuyoruz amacımız suan elimizdeki veri sütun adlarını ve içeriklerini barındırıyor
    # icerikleri sutun adlarından ayırmak icin bu islemi yapıyoruz,sutun adlarina ihtiyacimiz yok
    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2      # ikiserli ilerleme sebebi: dongu calistiginda:Turu,Konut,Kategorisi,Satilik diye gidecek
    # Hatırlarsak fiyatı başka bi yerde çekmiştik ve bunu da içeriklere yeni bi sütuna ekliyoruz.
    # öncesinde fiyat değişkenindeki gereksiz verileri siliyoruz. TL yazısı ve strip ile gereksiz boşluklar
    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    # içerikler kısmına fiyatı ekliyoruz.
    içerikler.append([fiyat_sade])
    # Suan liste halinde olan verimizi Df e çeviriyoruz ve transpozunu alıyoruz,Verilerimizi görünüm olarak yatay hale getirmek icin
    df_içerikler = pd.DataFrame(içerikler).T
    # verimizi csv dosyasına çeviriyoruz ve modu append yapıyoruz. Çünkü diğer çektiğimiz verileri de oraya ekleyeceğiz.
    # eğer mode = a yapmassak diğer gelen veriyi üzerine yazacaktır.
    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    # i değişkeni sayfadaki evlerin xpath de ki sayısı
    i = i + 1
    # bu kod ile bir önceki sayfaya geçiyoruz
    browser.execute_script("window.history.go(-1)")

print("ilk kısım çalıştı")



j = 4
while j <= 7:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(j) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    j = j + 1
    browser.execute_script("window.history.go(-1)")




    k = 12
    while k <= 13:
        tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(k) + "]")
        tıkla.click()

        print("üçüncü kisim 1")

        elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

        fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

        detaylar = []
        fiyat = []

        for i in fiyatlar:
            print(i.text)
            fiyat.append(i.text)

        for i in elements:
            print(i.text)
            detaylar.append(i.text)

        det_str = listToString(detaylar)
        ayrı = det_str.split("\n")

        df = pd.DataFrame(ayrı)
        df_yeni = df.iloc[7:53]
        df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

        df_yeni = df_yeni.reset_index()
        df_yeni.drop("index", axis=1, inplace=True)
        df_liste = df_yeni.values.tolist()

        içerikler = []
        i = 1
        while i <= 45:
            print(df_liste[i])
            içerikler.append(df_liste[i])
            i = i + 2

        fiyat_sade = fiyat[1].strip()
        fiyat_sade = fiyat_sade.replace("TL", "")
        içerikler.append([fiyat_sade])
        df_içerikler = pd.DataFrame(içerikler).T

        df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

        k = k + 1
        browser.execute_script("window.history.go(-1)")

    print("üçüncü kısım çalıştı")

l = 15
while l <= 17:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(l) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    l = l + 1
    browser.execute_script("window.history.go(-1)")

print("dördüncü kısım çalıştı")







m = 19
while m <= 24:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(m) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("beşinci kısım 1")
    m = m + 1
    browser.execute_script("window.history.go(-1)")

print("beşinci kısım calisti ")



n = 27
while n <= 32:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(n) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("altinci kısım 1")
    n = n + 1
    browser.execute_script("window.history.go(-1)")

print("altinci kısım calisti ")






o = 34
while o <= 39:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(o) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("yedinci kısım 1")
    o = o + 1
    browser.execute_script("window.history.go(-1)")

print("1. sf sonu, yedinci kısım son 1 ")






p = 1
while p <= 2:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(p) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("1. kisim")
    p = p + 1
    browser.execute_script("window.history.go(-1)")

print("2. sf bas,sekizinci kısım son 1 ")





r = 4
while r <= 7:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(r) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("ikinci kisim ")
    r = r + 1
    browser.execute_script("window.history.go(-1)")

print("2. sf 2. kısım")






s = 12
while s <= 13:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(s) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("ucuncu kısım ")
    s = s + 1
    browser.execute_script("window.history.go(-1)")

print("ikinci sf ucuncu kisim ")






t = 15
while t <= 17:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(t) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("dorduncu kısım 1")
    t = t + 1
    browser.execute_script("window.history.go(-1)")

print("ikinci sf dorduncu kisim son 1 ")







u = 19
while u <= 29:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(u) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("beşinci kısım 1")
    u = u + 1
    browser.execute_script("window.history.go(-1)")

print("ikinci sf bitti ")





v = 1
while v <= 2:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(v) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("birinci kısım 1")
    v = v + 1
    browser.execute_script("window.history.go(-1)")

print("ucuncu sf birinci kısım son 1 ")





y = 4
while y <= 7:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(y) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("ikinci kısım 1")
    y = y + 1
    browser.execute_script("window.history.go(-1)")

print("ucuncu sf ikinci kısım son 1 ")






z = 9
while z <= 10:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(z) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("ucuncu kısım 1")
    z = z + 1
    browser.execute_script("window.history.go(-1)")

print("ucuncu sf ucuncu kısım son 1 ")





a = 12
while a <= 13:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(a) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("dorduncu kısım 1")
    a = a + 1
    browser.execute_script("window.history.go(-1)")

print("ucuncu sf dorduncu kısım son 1 ")






b = 15
while b <= 24:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(b) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("beşinci kısım 1")
    b = b + 1
    browser.execute_script("window.history.go(-1)")

print("ucuncu sayfa beşinci kısım son 1 ")





c = 26
while c <= 35:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(c) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("altinci kısım 1")
    c = c + 1
    browser.execute_script("window.history.go(-1)")

print("ucuncu sayfa bitti ")






d = 1
while d <= 2:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(d) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("birinci kısım 1")
    d = d + 1
    browser.execute_script("window.history.go(-1)")

print("dorduncu sayfa birinci kısım son 1 ")






e = 4
while e <= 7:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(e) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("ikinci kısım 1")
    e = e + 1
    browser.execute_script("window.history.go(-1)")

print("dorduncu sayfa ikinci kısım son 1 ")






f = 9
while f <= 10:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(f) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("ucuncu kısım 1")
    f = f + 1
    browser.execute_script("window.history.go(-1)")

print("dorduncu sayfa ucuncu kısım son 1 ")





g = 12
while g <= 13:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(g) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("dorduncu kısım 1")
    g = g + 1
    browser.execute_script("window.history.go(-1)")

print("dorduncu sayfa dorduncu kısım son 1 ")





h = 15
while h <= 24:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(h) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("beşinci kısım 1")
    h = h + 1
    browser.execute_script("window.history.go(-1)")

print("dorduncu sayfa beşinci kısım son 1 ")





w = 26
while w <= 35:
    tıkla = browser.find_element_by_xpath("//*[@id='listing-search-wrapper']/div[" + str(w) + "]")
    tıkla.click()

    elements = browser.find_elements_by_css_selector("_2VNNor _2eyo_P")

    fiyatlar = browser.find_elements_by_css_selector("_2TxNQv")

    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)

    for i in elements:
        print(i.text)
        detaylar.append(i.text)

    det_str = listToString(detaylar)
    ayrı = det_str.split("\n")

    df = pd.DataFrame(ayrı)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]

    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis=1, inplace=True)
    df_liste = df_yeni.values.tolist()

    içerikler = []
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2

    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL", "")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T

    df_içerikler.to_csv(r"zingat3.csv", encoding="utf-8", index=False, mode="a")

    print("altinci kısım 1")
    w = w + 1
    browser.execute_script("window.history.go(-1)")

print("dorduncu sayfa bitti ")