#Import modul yang diperlukan untuk memproses data
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
#Assign Features and Labels
hargaTanah = ['murah','sedang','mahal','mahal','mahal','sedang','murah','murah','mahal','sedang']
jarakdariKota = ['dekat','dekat','dekat','jauh','sedang','jauh','jauh','sedang','jauh','sedang']
angkutanUmum = ['tidak','tidak','tidak','tidak','tidak','ada','ada','tidak','ada','ada']
dipilihPerumahan = ['ya','ya','ya','tidak','tidak','tidak','tidak','ya','tidak','ya']

#convert value atribut string menjadi numbers
hargaTanah_ecd = le.fit_transform(hargaTanah)
jarakdariKota_ecd = le.fit_transform(jarakdariKota)
angkutanUmum_ecd = le.fit_transform(angkutanUmum)
dipilihPerumahan_ecd = le.fit_transform(dipilihPerumahan)

print('Harga tanah encoded = ', hargaTanah_ecd)
print('Jarak dari kota encoded = ', jarakdariKota_ecd)
print('Angkutan umum encoded = ', angkutanUmum_ecd)
print('Dipilih perumahan encoded = ', dipilihPerumahan_ecd)

features = list(zip(hargaTanah_ecd,jarakdariKota_ecd,angkutanUmum_ecd))
print(features)

#Training model menggunakan training sets
model.fit(features, dipilihPerumahan_ecd)

#Prediksi output soal : Harga(mahal), jarak(sedang), angkutan umum(ada)
predicted = model.predict([[0,2,0]]) #input ==> 0 = mahal, 2 = sedang, 0 = ada
print('Predict output = ',predicted) # output ==> 0 = tidak


#Assign Features and Labels
usia = ['muda','muda','muda','muda','tua','tua','tua','tua','tua','tua']
pekerjaan = ['pelajar','mahasiswa','karyawan','karyawan','wiraswasta','wiraswasta','wiraswasta','karyawan','pensiunan','pensiunan']
pendapatan = ['sedikit','sedikit','sedikit','sedang','sedang','sedang','banyak','banyak','sedang','sedang','sedikit']
bukaRekening = ['ya','ya','tidak','ya','tidak','tidak','tidak','ya','tidak','tidak']

#Mengonvert label string menjafi numbers
usia_ecd = le.fit_transform(usia)
pekerjaan_ecd = le.fit_transform(pekerjaan)
pendapatan_ecd = le.fit_transform(pendapatan)
bukaRekening_ecd = le.fit_transform(bukaRekening)

print('Usia encoded = ', usia_ecd)
print('Pekerjaan encoded = ', pekerjaan_ecd)
print('Pendapatan encoded = ', pendapatan_ecd)
print('Buka rekening encoded = ', bukaRekening_ecd)

features_2 = list(zip(usia_ecd,pekerjaan_ecd,pendapatan_ecd))
print(features_2)

#Training model menggunakan training sets
model.fit(features_2, bukaRekening_ecd)

#Prediksi output soal  : Usia(muda),Pekerjaan(karyawan), pendapatan(banyak)
Predicted = model.predict([[0,0,0]]) #input ==> 0= muda, 0= karyawan, 0 = banyak
print('Predicted output = ',Predicted) #output ==> 1 = ya

#Prediksi output soal : usia(tua), pkerjaan(pensiunan), pendapatan(banyak)
Predicted = model.predict([[1,3,1]])   #Input ==> 1 =tua, 3 = pensiunan, 1 = sedang
print('Predicted output = ',Predicted) #output ==> 0 = tidak

