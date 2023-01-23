#Fonksiyon, işlevselliğin karşılığı diyebiliriz.

"""
Bir fonksiyon, tek bir ilgili eylemi gerçekleştirmek için kullanılan, yeniden düzenlenebilir bir kod bloğudur. Fonksiyonlar, 
uygulamanız için daha iyi modülerlik yanı sıra kod yeniden kullanımı sağlar. Print gibi Python fonksiyonlarının yanı sıra
kullanıcı tanımlı fonksiyonları oluşturup kullanabiliriz. 

8.1. Bir fonksiyon tanımlama
Gerekli fonksiyonelliği sağlamak için fonksiyonları tanımlayabilirsiniz. Python’da bir fonksiyonu tanımlamak için basit kurallar:

Fonksiyon blokları, sırasıyla anahtar kelime def, ardından fonksiyon adı ve parantez (()) içerir.
Herhangi bir girdi parametresi veya argümanı bu parantez içine yerleştirilmelidir. Ayrıca bu parantez içindeki parametreleri de tanımlayabilirsiniz.
Her fonksiyon içindeki kod bloğu bir kolonla başlar (:) ve girintili olarak oluşturulur.
Bir işlevin ilk ifadesi isteğe bağlı bir yorum satırı (“…” içinde) olabilir. Özellikle fonksiyonu açıklamak için kullanılabilir.
İfade [return] içeriyorsa, isteğe bağlı olarak fonksiyondan çıkılır. Hiçbir argüman içermeyen bir return veya Return None aynı
 anlama gelir ve değer döndürmez. Ayrıca, hiç return içermeyen bir fonksiyon tanımlanabilir.


 def fonksiyonismi( parametreler ):
   "fonksiyonu_analatan_satır"
   fonksiyon_ifadeleri
   return [ifade]

"""

##Durum ne olursa olsun ekrana 5 bastırmasını istediğim bir fonksiyon tanımlaması.
def bes_bastir():
    print(5)
    return 5
bes_bastir()

##Fonksiyonlarda print ve return farkı: Print işlemin sonucunu bastırır, return ise içerisine ve verirsek onu bastırır gibi düşünebiliriz.
##Return komutu, bir fonksiyonun sonlandırılmasına ve fonksiyonun çağırıldığı yere değer götürmesine yarar.
def bes_bastir():
    return 5
print(bes_bastir())

## Fonksiyonlarda Argümanlar
def sayi_dondur(sayi):
    return sayi

a=sayi_dondur(5)
print(a)
#Fonksiyon içerisinde parametreye değer atama işlemi.
def sayi_dondur(sayi=250):
    return sayi
a=sayi_dondur()
print(a)

#Fonksiyon içerisinde parametreye değer atama işlemi.
def topla(a=1, b=3):
    return a+b
print(topla())
#Fonksiyon içerisinde parametreye değer atama işlemi.
def isim_yazdir(name="Merve",s_ad="Karakuş"):
    print(name,s_ad)
isim_yazdir()
#Girilen büyük sayiyi dondürme
def b_sayi(a,b):
    if a>b:
        print(a)
    else:
        print(b)
a = b_sayi(100,2)

##Girilen sayiya göre parametre belirleyerek büyük sayiyi bulma
a = int(input("Lütfen bir sayi giriniz:"))
b = int(input("Lütfen bir sayi daha giriniz:"))
def b_sayi(a,b):
    if a>b:
        print(a) #return a
    else:
        print(b) #return b
c = b_sayi(a,b)

# İsim ve yaş yazdıran fonksiyon
def infoYaz( ad, yas ):
   "İki parametreli fonksiyon"
   print("Adı: ", ad)
   print("Yaşı ", yas)
   return
 
infoYaz( yas=50, ad="miki" )

## Fonksiyonların birbiri ile ilişkisi. Fonksiyonları birbirinin içerisinde çağırarak işlemler yapabiliriz. Nasıl? Yapalım... :)


a = int(input("Lütfen bir sayi giriniz:"))
b = int(input("Lütfen bir sayi daha giriniz:"))
def b_sayi(a,b):
    if a>b:
        return a
    else:
        return b
c = b_sayi(a,b)

def metin_yazdir(a,b):
    buyuk_sayi = b_sayi(a,b)
    sablon_metin = "{} daha büyük sayidir".format(buyuk_sayi) 
    print(sablon_metin)
metin_yazdir(a,b)

# Fonksiyonların birden fazla sonuç döndürebilmesi için ne yapabiliriz?
#isim soyisim ayırma
adsoyad = str(input("Lütfen isminizi ve Soyisminizi giriniz:"))
def isim_soyisim_ayirma():
    isim = adsoyad.split()[0]
    soyisim = adsoyad.split()[1]
    return isim, soyisim

print(isim_soyisim_ayirma())

#Örnek

sayi1 = int(input("Lütfen bir sayi giriniz:"))
sayi2 = int(input("Lütfen bir sayı daha giriniz:"))
def top():
    if sayi1 < sayi2:
        sonuc = sayi1 * sayi2
        print(sonuc)
    else:
        sonuc = sayi1 + sayi2
        print(sonuc)
top()

#isim soyisim birleştirme fonksiyonu
def isim_soyisim_birlestir(isim, soyisim):
    return " ".join([isim,soyisim])
print(isim_soyisim_birlestir("Merve","Karakuş"))

"""
 Değişken uzunlukta argümanlar
Fonksiyon tanımlarken argüman sayısı belirsiz olabilir. Bu tür argüman 
sayısı belli olmayan fonksiyonlar değişken uzunluklu argümanlar olarak adlandırılır.
"""


## *args nedir ? Liste tanımlıyoruz gibi düşünebiliriz. İçeirisnde istediğimiz kadar parametre atabiliriz.
def isim_soyisim_birlestir(*args):
    return " ".join(args)

print(isim_soyisim_birlestir("Merve","Karakus","2","3")) 

# 
def isim_soyisim_birlestir(*args):
    for i in args:
        print(i)
    return " ".join(args)
print(isim_soyisim_birlestir("Merve","Karakus","2","3")) 
# Fonksiyon ortalama hesaplama örnek

def Topla(sayi1,sayi2,sayi3):
    return sayi1+sayi2+sayi3
 
def ortalama_hesapla(sayi1,sayi2,sayi3):
    ortalama = Topla(sayi1,sayi2,sayi3)/3.0
    print(ortalama)
 
ortalama_hesapla(1,2,3)


##Python dilinde tüm parametreler (argümanlar) referans olarak iletilir. 
# Bir parametrenin bir fonksiyon içinde ne ifade ettiğini değiştirirseniz, 
# değişiklik aynı zamanda çağırma işlemine geri yansır. Örneğin,

def beniDegistir( mylist ):
   "Bu değişiklik list'e yansır"
   mylist.append([1,2,3,4]);
   print("Fonksiyon içindeki değerler: ", mylist)
   return

mylist = [10,20,30]
print("Fonksiyon çağrılmadan önce list: ", mylist)
beniDegistir( mylist )
print("Fonksiyon çağrılmasından sonra list: ", mylist)
def beniDegistir( mylist ):
   "Bu değişiklik list'e yansır"
   mylist.append([1,2,3,4]);
   print("Fonksiyon içindeki değerler: ", mylist)
   return
 
mylist = [10,20,30]
print("Fonksiyon çağrılmadan önce list: ", mylist)
beniDegistir( mylist )
print("Fonksiyon çağrılmasından sonra list: ", mylist)

"""
 Değişkenlerin kapsamı
Bir programdaki tüm değişkenlere programın tüm konumlarına erişemeyebilir. Bu tür değişkenler kullandığımız yere bağımlıdır.
 Python’da iki temel değişken kapsamı vardır.

Global (Genel)
Local (Yerel)
Bir fonksiyonun altında tanımlanan değişkenlerin yerel kapsamı vardır. Dışarda tanımlanan değişkenlerin ise genel kapsamı vardır.
Yerel değişkenlere sadece o fonksiyon içinden ulaşılırken, genel değişkenlere program içinde herhangi bir konumdan ulaşabilirsiniz.
 Eğer aynı isimde global ve local değişken tanımlanırsa öncelik local değişkenindir. Örneğin,
"""
toplam = 0; 
# toplama fonksiyonu
def toplama( arg1, arg2 ):
   # Toplama fonksiyonu
   toplam = arg1 + arg2 # Local değişken
   print("Fonksiyonun içi toplam: ", toplam)
   return toplam

# Fonksiyonu çağırma
toplama( 10, 20 )
print("Fonksiyonun dışındaki toplam: ", toplam)

##Aşağıdaki toplam değişkeni global yapılmıştır.

toplam = 0; 
# toplama fonksiyonu
def toplama( arg1, arg2 ):
   # Toplama fonksiyonu
   global toplam # Global değişken yapıldı
   toplam = arg1 + arg2 # Local değişken
   print("Fonksiyonun içi toplam: ", toplam)
   return toplam

# Fonksiyonu çağırma
toplama( 10, 20 )
print("Fonksiyonun dışındaki toplam: ", toplam)
    







