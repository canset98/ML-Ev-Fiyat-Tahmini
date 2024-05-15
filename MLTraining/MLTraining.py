## Kütüphanelerimizi ekliyoruz
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.model_selection import cross_val_score
import joblib


# Son halini almış temiz verisetini okuyoruz
df_2 = pd.read_excel(r"son_hali_emlakjet.xlsx")
df_2.drop("Unnamed: 0", axis = 1, inplace = True)

df = df_2.copy()
print("df.columns", df.columns)


#Çalışmak istediğimiz sütunları aldık.
df = df[["Brüt_Metrekare", "Binanın_Yaşı","Binanın_Kat_Sayısı","Kullanım_Durumu",
         "Yatırıma_Uygunluk","Banyo_Sayısı","Net_Metrekare",
         "Oda_Sayısı", "Bulunduğu_Kat", "Isıtma_Tipi","Krediye_Uygunluk",
         "Fiyatı","İlçe","Mahalle", "yaka","Yaşam_endeksi","Nüfus"]]

print("df after selecting the feature", df.columns)
print(df)


# Bağımlı ve Bağımsız değişkenleri ayırdık
X = df.drop(["Fiyatı"], axis = 1)
y = df["Fiyatı"]
print("X",X)


# Eğitim ve Test verisinin ayrılması
# splitting oranı : 25% test 75% eğitim (train) o şekilde belirliyoruz
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 25, random_state = 144)


# (öznitelik seçimi) Feature Selection
""" veri setimiz çeşitli sütunler (features) içerir ve 
bazı özellikler önemli olmadığı için 
model eğitiminde gürültü yapar ve doğruluğu düşürür
bu yüzden feature_importances_ metodu kullanarak 
hangi özellikleri alabiliyoruz ve hangisi daha önemli belirleyebiliriz """
rf_test=RandomForestRegressor()
rf_test.fit(X_train, y_train)
importance=rf_test.feature_importances_
("importance",importance)

#özelliklerin önemine göre sıralıyoruz
#okunabilirliği arttırmak için data frame ile gösteriyoruz
feature_importance_df = pd.DataFrame({'Feature': X_train.columns, 'Importance': importance})

feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
print(feature_importance_df)

# GridSearchCV
"""bu aşamada Grid Search cv yönetimi kullanarak 
random forest algoritması için en uygun hyperparametreleri belirliyoruz
bu kod kısmı çalıştırdığımızda biraz zaman alır bu yüzden yorum olarak alıyoruz"""

#param_grids = {"n_estimators": [50, 100, 200, 300], "max_depth": [None, 5, 7, 10, 20, 30, 40, 50],
    #"min_samples_split": [2, 5, 10], 'bootstrap': [True, False]}

#grid_search = GridSearchCV(estimator=RandomForestRegressor(), param_grid=param_grids, cv=10, n_jobs=-1, verbose=2)
#grid_search.fit(X_train, y_train)
#print("best_params for training in rf", grid_search.best_params_)"""


#Eğitim için random forest modelinde best_params {'bootstrap': True, 'max_depth': None,
# 'min_samples_split': 10, 'n_estimators': 50}

#En uygun parametreleri giriyoruz
rf = RandomForestRegressor(n_estimators=50,max_depth=None,bootstrap=True,min_samples_split=10,random_state=0)

#Modelimizi eğitiyoruz
rf.fit(X_train, y_train)

#Tahmin yapıyoruz
y_pred=rf.predict(X_test)

# Değerlendirme metrikleri (Model evaluation)

"""bu aşamada eğitilen modelin doğruluğu ve başarıları ölçmek için regression bazı metrikleri kulladık"""
#modelin r^2 skorunu hesapladık. 0-1 arası değer döner bize
r2 = r2_score(y_test, y_pred)
#mse
mse = mean_squared_error(y_test, y_pred)
#rmse
rmse = np.sqrt(mse)
#cross_valdiation
cross_val=np.sqrt(-1*(cross_val_score(rf, X_test, y_test, cv=10, scoring='neg_mean_squared_error'))).mean()
#metriklerin sonuçları Yazdırıyoruz
print("R^2 score:", r2)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("cross_val",cross_val)

#eğitilen modelimizi kaydetiyoruz
#joblib.dump(rf, "./random_forest_Regressor.joblib")

"""bu eğitilen model kullnmak istiyorsak yeni bir modül açtığımızda aşağıdaki kodlar yazmamız gerekir"""
#new_rf=joblib.load("./random_forest_Regressor.joblib")

#data=new_rf.predict("")