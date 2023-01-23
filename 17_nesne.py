# class Person:
#   pass

# p1 =Person()

class Person:
    #pass
    #constractur(yapıcı metot __init__)
    ##Oluşturulan her bir obje için mutlaka çalıştırılır. Başlatıcı, başlatmak analamı katıyor gibi düşünülebilir.
    def __init__(self, name, surname, year):
        self.name = name
        self.surname = surname
        self.year = year
        print("__init__ metodu çalıştı.")
    def info(self):
      print("name : {} surname: {} year:{}".format(self.name,self.surname,self.year))


p1 = Person("Merve","Karakuş",24)

print(p1)


###############################
sesli_harfler = 'aeıioöuü'
sayaç = 0

def kelime_sor():
    return input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır(sayaç, kelime):
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

def ekrana_bas(kelime):
    mesaj = "{} kelimesinde {} sesli harf var."
    print(mesaj.format(kelime, artır(sayaç, kelime)))

def çalıştır():
    kelime = kelime_sor()
    ekrana_bas(kelime)


çalıştır()
#############
class Çalışan():
    personel = []

    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.personele_ekle()

    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))

    def personeli_görüntüle(self):
        print('Personel listesi:')
        for kişi in self.personel:
            print(kişi)

    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyetleri.append(kabiliyet)

    def kabiliyetleri_görüntüle(self):
        print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)
ç1 =Çalışan('Ahmet')