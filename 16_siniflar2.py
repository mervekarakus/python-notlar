#Yapıcı Fonksiyonlar
#Bir sınıftan üretilen her bir nesnenin aynı özelliklere sahip olmaması
"""
Python’da Yapıcı Fonksiyon __init__
Mon, Aug 22, 2011
Python’da bir nesne çağırdığınızda otomatik olarak çalışacak ve sadece nesneyi ilk oluşturduğunuzda çalışacak olan 
bir fonksiyon tanımlayabilirsiniz. Bu fonksiyonun adı Python yapımcıları tarafından __init__() olarak belirlenmiş.
 Dışarıdan ulaşılmasını istediğimiz her fonksiyona self parametresini eklememiz gerektiğini de belirtelim.

Nesne oluşturduğumuzda ekranda Merhaba Dünya! yazısını göreceğiz. Burda self kullanılmazsa hata vereceğini de söyleyelim. Hata alttaki gibi olacaktır:

Traceback (most recent call last):

  File “C:Python27dsd.pyw”, line 10, in

    x=sinifim()

TypeError: init() takes no arguments (1 given)
"""
class Dusman:
  kalan_can = 3
  def saldir(self): #kendi nesnemize ulaşmak için kullandığımız bir anahtar kelime.
    print("Hücuuuuuummmmm")
    self.kalan_can -=1
  def hayatta_mi(self):    
    if (self.kalan_can <= 0):
      print("Öldü")
    else:
      print(str(self.kalan_can) + " canım kaldı")
 ##Burası sınıf tanımlama işlemlerimiz ardından bu sınıftan bir nesne oluşturmamız gerekmekte.
dusman1 = Dusman() #Dusman sınıfından dusman1 isminde bir nesne oluşturduk.
dusman2 = Dusman()

dusman1.saldir()
dusman1.saldir()
dusman1.hayatta_mi()

dusman2.saldir()
dusman2.saldir()
dusman2.saldir()
dusman2.hayatta_mi()

# Nesne tabanlı programlamanın temel mantığı budur. Bir sınıf oluşturuyoruz o sınıflardan nesneler oluşturuyoruz ve bu nesnelerin fonk, özelliklerini kullnarak işlemerlimi yapıyorum.
#Düşman1 in değerleri ali vs benim burda gönderdiğim 4 değer parametreler ile eşleşti
class Dusman:
    def __init__(self, isim, kalan_can,saldiri_gucu,mermi_sayisi):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi
    def print(self):
        print("Basılıyor..................")
        print("İsim:",self.isim,"Kalan Can:",self.kalan_can,"Saldırı Gücü:",self.saldiri_gucu,"Mermi Sayısı:",self.mermi_sayisi)

dusman1 = Dusman("Ali",2000,30,50)
dusman2 = Dusman("Veli",500,40,10)
print("Düşman1************************")
dusman1.print()
print("Dişman2************************")
dusman2.print()
