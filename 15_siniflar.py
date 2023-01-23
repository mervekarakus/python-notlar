"""
Python Sınıflar/Nesneler
Python, nesne tabanlı bir programlama dilidir. Python'da neredeyse her şey bir sınıftır.

Bir sınıf (class), kendisinden örnek oluşturulabilen bir nesnedir (object). Bu sınıflara özellik ve yöntemler atanabilir.
####
Bir Sınıf Oluşturmak
Sınıf oluşturmak için class ifadesi kullanılır. Bu ifadeden sonra sınıfın adına yer verilir ve iki nokta üst üste kullanılarak
 sınıf yapısı yazılmaya başlanır:

Eğer Sinifim isimle tek özellikli bir sınıf oluşturmak isteseydim;
class Sinifim:
  x = 5

Sınıfın Bir Örneğini (Nesne) Oluşturmak
Yukarıdaki örnekte bir sınıf tanımladık. Peki bu sınıfı nasıl nesne olarak oluşturup kullanacağız? Bunun için aşağıdaki örneği inceleyin:
class Sinifim:
  x = 5

p1 = Sinifim()
print(p1.x)

__init__() Fonksiyonu
Bundan önceki örnekler bir sınıfın temel bileşenleriydi. Şimdi bahsedilecek olan __init__() fonksiyonu ise sınıfın temel bileşenidir. Nesne oluşturulduğunda ilk olarak bu 
fonksiyon çalıştırılır.

class Kisi:
  def __init__(self, isim, yas):
    self.isim = isim
    self.yas = yas

p1 = Kisi("Murat", 36)

print(p1.isim)
print(p1.yas)

Nesne Yöntemleri/Metotları
Nesneler için sınıfa özgü yöntemler/metotlar geliştirilebilir. Nesne yaratıldıktan sonra bu yöntemler .yontemAdi() şeklinde çalıştırılabilir.

 PYTHON Kodu
class Kisi:
  def __init__(self, isim, yas):
    self.isim = isim #self.a
    self.yas = yas  #self.b
  def yazdir(self):
    print("Merhaba, adım ", self.isim, ", yaşım ", self.yas);

p1 = Kisi("Murat", 36)
p1.yazdir()
NOT: Yukarıdaki örneklerde geçen self, sınıfın kendisini ifade eden bir parametre olup nesneye ait özellik ve yöntemlerle işlem yaparken kullanılır. İstenilirse bunun yerine farklı adlandırmalar yapılabilir. Ancak __init__() ve yöntemlerde kullanılması zorunludur. Aşağıdaki örnekte önce kendisi, sonradan da kisi şeklinde adlandırılıp kullanılmıştır:
class Kisi:
  def __init__(kendisi, isim, yas):
    kendisi.isim = isim
    kendisi.yas = yas
  def yazdir(kisi):
    print("Merhaba, adım ", kisi.isim, ", yaşım ", kisi.yas);

p1 = Kisi("Murat", 36)
p1.yazdir()

Nesne Özelliklerini Değiştirmek
Nesne özelliğinden sonra eşittir yazılarak yeni değer ifade edilebilir:

 PYTHON Kodu
class Kisi:
  def __init__(self, isim, yas):
    self.isim = isim
    self.yas = yas

p1 = Kisi("Murat", 36)
p1.yas = 40
print(p1.yas)
Nesnenin Bir Özelliğini Ya Da Nesneyi Silmek
Bunun için del ifadesi kullanılabilir:

 PYTHON Kodu
kisi = new Kisi("Murat", 36)

del kisi.yas # yas özelliğini siler

del kisi # nesneyi tamamen siler



"""

class Ucus: #Class artık kendine ait bir veri tipi diyebiliriz aslında
  havayolu ="THY"
ucus1 = Ucus() #Burada ucus tipinde ucus1 isimli bir değişken oluşturdum.
print(ucus1.havayolu)

###########
#Self : objenin kendini refere etmesi gerektiğini belirten bir anahtar keliemdir.Self sinif icerisinde metotlara, parametrelere ulasmak icin siklikla kullanilabilinir.
#parametreleri verme
class Ucus: #Class artık kendine ait bir veri tipi diyebiliriz aslında
  havayolu ="THY"
  def __init__(self,kod,kalkis,varis, sure, kapasite, yolcu): #Özelliklerin tanımlanması.
    self.kod = kod
    self.kalkis = kalkis
    self.varis = varis
    self.sure = sure
    self.kapasite = kapasite
    self.yolcu = yolcu
  def anons_yap(self):
    return "{} sefer sayılı {}-{} ucususmuz {} dakika sürecektir".format(
    self.kod,
    self.kalkis,
    self.varis,
    self.sure)
#ucus2 = Ucus() #Parametrelere değer ister
ucus2 = Ucus('TK123','ANK','IST',60,200,50)
print(ucus2.kod)
ucus3 = Ucus('TH46','IST','IZMR',40,400,100)
print(ucus3.kod)
ucus4 = Ucus('THK06','ADN','KYSR',40,400,100)
print(ucus3.kod)
print(ucus3.anons_yap())
  
