################# Veriable Unpacking ###################
#Şimdiye kadar hep tek değişkene tek değer verdik. Peki bir seferde birden çok değişkene
#değer vermek için ne yaparız?
x = 4
y = 7
## Bu iki değişken ataması da aynıdır.
x, y = (4,7)
####-> Aşağıdaki değer ataması doğru bir değer atamadır.
x, y, z =(3, 5, 6)
print(x, y, z)

##### Bazı değerlere ihtiyacım yoksa ########
# Diyelim ki soldaki yapınun sadece birinci elemanına bir değer eşitleyip kullanmak istiyorum. Daha önce döngülerde yaptığımız gibi kullanmayacağımız değişkene _ diyebiliriz.

x, _ = (4, 7)

##### Sol ve sağdaki yapı farklı sayıdaysa #####
x, y, z = (4, 8, 9, 10, 11)
"""
Bunu gidermek için * yapısını kullanacağız. Aşağıdaki kod şu demek oluyor:
İlk iki elemanı x ve y'ye eşitle, sonuna kadar kalan diğer tüm elemanları z'ye eşitle. 
Bunun sonunda z 11,2,21'den oluşacak, tipi list olacak.
"""
x, y, *z = (4, 8, 9, 10, 11)

################## ENUMERATE ####################


"""for ile non-scalar yapılar içerisinde dolaşırken ya elemanları ya da indexleri üzerinde dolanmıştık, ama neden ikisi de aynı anda olmasın?
Variable Unpacking konusunda bir tuple, liste gibi yapıların değerlerini birden çok değişkene bir seferde eşitlemeyi görmüştük.

Bunun aynısını iterasyonda da yapabiliriz.
"""
l = [(1,2), (10,20)]

for e in l:
    print(e)

####->
for e in l:
    a, b = e
    print(a)
    print(b)
    print("*********")
"""
1
2
*********
10
20
*********
"""
for a, b in l:
    print("tuple'ın ilk elemanı", a)
    print("tuple'ın ikinci elemanı", b)
    print("-----------------------------")

"""
tuple'ın ilk elemanı 1
tuple'ın ikinci elemanı 2
-----------------------------
tuple'ın ilk elemanı 10
tuple'ın ikinci elemanı 20
-----------------------------
"""
# enumerate() bize (index, element) olarak verecek.
adlar = ['Tyler', 'Blake', 'Cory', 'Cameron']


for e in adlar:
    print(e)


# Tyler
# Blake
# Cory
# Cameron


for i, e in enumerate(adlar):
    print(i, "indexindeki eleman:", e)


# 0 indexindeki eleman: Tyler
# 1 indexindeki eleman: Blake
# 2 indexindeki eleman: Cory
# 3 indexindeki eleman: Cameron
# enumerate() 0'dan başlamak zorunda değil, özellikle kaçtan başlayacağını belirtebiliriz.
for i, e in enumerate(adlar, start = 100):
    print(i, "lokasyonunda bulunan eleman:", e)


# 100 lokasyonunda bulunan eleman: Tyler
# 101 lokasyonunda bulunan eleman: Blake
# 102 lokasyonunda bulunan eleman: Cory
# 103 lokasyonunda bulunan eleman: Cameron

# zip()


# Farklı yapıların içinde paralel iterasyon yapmamızı sağlar. zip()
ogrenciler = ["ogrenci_1", "ogrenci_2", "ogrenci_3"]


notlar = [90,80,72]


for s, g in zip(ogrenciler, notlar):
    print(s, g)


for e in zip(ogrenciler, notlar):
    print(e)


for i in range(len(ogrenciler)):
    print(ogrenciler[i], notlar[i])

# zip() Örnek:


# Her ayki karı hesaplamak
satis = [3500.00, 76300.00, 67200.00]


maliyet = [56700.00, 21900.00, 12100.00]


for i in range(len(maliyet)):
    s = satis[i]
    c = maliyet[i]
    
    kar = s - c
    print(f'Total profit: {kar}')


# Total profit: -53200.0
# Total profit: 54400.0
# Total profit: 55100.0


satis = [3500.00, 76300.00, 67200.00]
maliyet = [56700.00, 21900.00, 12100.00]
for s, c in zip(satis, maliyet):
    kar = s - c
    print(f'Total profit: {kar}')


# Total profit: -53200.0
# Total profit: 54400.0
# Total profit: 55100.0

# zip() ile Dictionary Yaratmak:
keys = ['isim', 'soyad', 'ulke', 'is']
values = ['Denis', 'Walker', 'Turkey', 'data scientist']

#############
d = {}


for k, v in zip(keys, values):
    d[k] = v

#####################



{'isim': 'Denis', 'soyad': 'Walker', 'ulke': 'Turkey', 'is': 'data scientist'}


d["isim"]