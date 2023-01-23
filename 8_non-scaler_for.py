####### Listelerde İterasyon ########
notlar = [30,70,80,60]
for e in notlar:
    print(e)

####-> Not ortalamasını bulan program
t=0
notlar = [30,70,80,60]
for e in notlar:
    t += e
    ortalama = t/ len(notlar)
print(ortalama)

"""
for döngüsünü işlerken for <değişken> in <obje> yapısında, her iterasyonda değişkenin tek tek objenin elemanlarına eşit olduğunu konuşmuştuk.


list, tuple, dictionary non-scalar veri tiplerini gördük ve bunların hepsinin içsel bir yapısı var, şimdi bunların elemanlarında for kullanarak iterasyon yapmaya bakalım.

Listelerde İterasyon


Diyelim ki öğrencilerin notlarını bir listede tutuyoruz.
"""

notlar = [90,72,81,77]


for e in notlar:
    print(e)

"""
90
72
81
77
"""

# Bu sınıftaki not ortalamasına bakmak istiyor olabilirim.


t = 0

for e in notlar:
    t += e
    
ortalama = t / len(notlar)

print(ortalama)


# 80.0


# Burada e 'nin özel bir anlamı yok, sadece döngünün içinde onu kullanırken o adla referans veriyorum, adı penguen de olabilirdi.


t = 0

for penguen in notlar:
    t += penguen
    
ortalama = t / len(notlar)

print("Ortalama:",ortalama)


Ortalama: 80.0

"""
Bunun aynısını range() fonksiyonu ile de yapabilirdik.


for e in notlar diyince ilk iterasyonda enin değeri 90, ikincisinde 72... olarak devam etti.


range() ile indexlerde iterasyon yapıp indexing ile değerlerine de ulaşabilirdim. (Range belirli bir listenin indexlerinde iterasyon yapmamı sağlamıyor, range(len(notlar)) diyince bize 0,1,2.. len(notlar)-1 sayılarını verecek, bunlar da listenin indexleriyle örtüşüyor, yoksa range() index verir diye bir şey yok.)
"""

for i in range(4):
    print("Iteration: ", i)

"""
Iteration:  0
Iteration:  1
Iteration:  2
Iteration:  3
"""

t = 0

for i in range(len(notlar)):
    t += notlar[i]
    
ortalama = t / len(notlar)

print("Ortalama:",ortalama)

"""
Ortalama: 80.0
Diyelim ki öğretmen farketti ki herkese 5 puan az vermiş, herkesin puanını 5 arttırmak istiyor, bunu direkt listenin elemanlarında iterasyon yaparak yapamam. Listenin indexlerine erişip o değeri güncellemem lazım.
notlar
"""

[90, 72, 81, 77]
for e in notlar:
    print(e)

"""
90
72
81
77
"""

# Buradaki e sadece notların içindeki değerler,e 'yi değiştirmek listenin elemanlarını değiştirmez!


for e in notlar:
    print(e)
    e = e + 10
    print(e)
    print(notlar)
    print("--------------")

print(notlar)

"""
90
100
[90, 72, 81, 77]
--------------
72
82
[90, 72, 81, 77]
--------------
81
91
[90, 72, 81, 77]
--------------
77
87
[90, 72, 81, 77]
--------------
[90, 72, 81, 77]

"""
# Güncelleme mantığını range() ile indexlerinde iterasyon yaparak yapacağım.


for i in range(len(notlar)):
    notlar[i] += 5





# [95, 77, 86, 82]


# Hadi biraz da continue mantığının alıştırmasını yapmış olalım. Diyelim ki öğretmen 2. öğrencinin kağıdını doğru okumuş, 2. öğrenci (index 1'deki) hariç hepsinin değerini 5 arttıracak:


notlar = [90,72,81,77]


for i in range(len(notlar)):
    
    if i == 1:
        continue
        
    notlar[i] += 5

print(notlar)


#[95, 72, 86, 82]

"""
Şimdi de break egzersizi yapalım.


Diyelim ki bir listenin içinde belirli bir eleman var mı diye kontrol etmek istiyoruz. Bulunca aramaya devam etmeyeceğim. Devam etme mantığını break ile sağlayacağım.


İlk kullanıcıya hangi sayıyı aradığını soracağız, sonra bu sayı var mı kontrol edeceğiz.

"""
x = int(input("Hangi sayıyı kontrol edeyim?:"))

l = [2,3,40,100,10,1]

for e in l:
    print(e) # iterasyon break ile çıkmış mı görelim mi diye
    if e == x:
        print("Buldum!!")
        break

"""
Hangi sayıyı kontrol edeyim?:100
2
3
40
100
Buldum!!


Tuple'lerda İterasyon


Listelerde iterasyondan hiç bir farkı yok. Evet kısa bir açıklama oldu ama durum bu :) . Değerlerini güncelleyemiyoruz ama bu zaten döngüden bağımsız bir durum oluyor.
"""
t = (1,2,3,4)


for e in t:
    print(e)


# 1
# 2
# 3
# 4


toplam = 0

for e in t:
    toplam += e
    
print(toplam)


# 10


for i in range(len(t)):
    print(t[i])


# 1
# 2
# 3
# 4


for i in range(len(t)):
    t[i] += 2

"""
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-37-51c8ededb856> in <module>
      1 for i in range(len(t)):
----> 2     t[i] += 2


TypeError: 'tuple' object does not support item assignment

Dictionary'lerde İterasyon


Burada durum biraz farklı. Default olarak elemanlarında dolaş diyince key 'lerde iterasyon yapıyor. Zaten index mantığı olmadığı için range() ile yapmak çoğu zaman karşımıza çıkmaz.
"""

d = {"student_1": [90,89], "student_2": [80,83], "student_3": [72,71]}


for k in d:
    print(k)

"""
student_1
student_2
student_3
"""

# Değerlerine ulaşmak istiyorsam şöyle yapabilirdim:


for k in d:
    v = d[k]
    print(v)

"""
[90, 89]
[80, 83]
[72, 71]
"""
"""
Veya d.values() diyerek value'lerında iterasyon yapabilirim. Burada for <değişken> in <obje> yapısında <değişken> int vs gibi şeyler değil liste gibi yapılar da olabilir iterasyon içerisinde, burada da öyle oldu.


bu .values() 'dan dolayı olan bir şey değil, dictionary'nin value'lerı int olsa böyle olmazdı.
"""

d = {"student_1": 90, "student_2": 80, "student_3": 72}


for v in d.values():
    print(v)

"""
90
80
72
"""

d = {"student_1": [90,89], "student_2": [80,83], "student_3": [72,71]}


for v in d.values():
    print(v)

"""
[90, 89]
[80, 83]
[72, 71]
Burada v, her iterasyonda int .


85'den fazla alan biri var mı diye bakmak istiyorum diyelim, ve bunun kim olduğunu (olduklarını) bulmak istiyorum.
"""

d = {"student_1": 90, "student_2": 80, "student_3": 72}


for k in d:
    value = d[k]
    
    if value > 85:
        print(k)

"""

student_1


Aynı anda hem key hem de value'larda iterasyon yapmak için:


Variable unpacking konusunda bir tuple, liste gibi yapıların değerlerini birden çok değişkene bir seferde eşitlemeyi görmüştük.


Bunun aynısını iterasyonda da yapabiliriz.
"""


for k,v in d.items():
    print("key değeri:", k, "value değeri:", v)

"""
key değeri: student_1 value değeri: 90
key değeri: student_2 value değeri: 80
key değeri: student_3 value değeri: 72
"""