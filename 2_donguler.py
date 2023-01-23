#DÖNGÜLER
#if- elif- else ile koda bir durumsallık kattık. 
# Yani programımızı dallandırmayı öğrendik ama kod akışı hala lineer. 
# Bir işlemi birden çok kere yapmak istiyorsam bunu kolaylaştıracak bir ypım yok henüz.
#Bir şeyi defalarca yapmak istediğimde kullanabileceğim bir yapıya ihtiyacım var. 
#Mesela bir siteye girmek için şifrenizi girdiğinizi düşünün. Site siz şifrenizi yanlış girdikçe şifrenizi bir daha girin diyor. Siteyi kodlayan kişinin
#önceden isizn kaç kere yanlış gireceğinizi bilmesi mümkün değil. Bu nedenle kodun o parçasının şifre doğrulanana kadar çalışmasını isteyebiliriz. ya da belirli koşullar koyabiliriz. 
#Bu durum için döngüleri kullanabiliriz.

 ### WHILE DÖNGÜSÜ ###
##                   ##
##                   ##
 #####################
#Örnek 1 -Kullanıcıdan pozitif bir tamsayı alma.
x = int(input("Bir sayi giriniz:"))

while x < 0:
    print("Sayı negatif pozitif bir sayı giriniz ! ")
    x= int(input("Bir sayı girin:"))
print("Sayınız Pozitif",x)

#Örnek 2 - ' dan 3 ' e kadar olan sayıların ekrana yazdırılması.
x = 0

while x < 3:
    print(x)
    x = x + 1

#Örnek 3 - 100' e kadar olan sayıların toplamını yazdıralım.
x = 0
toplam = 0

while x < 101:
    toplam += x #toplam = toplam + x -> toplamın değerini x kadar artır.
    x += 1      # x = x + 1 
    print(x)
print(toplam)

#Infinite Loop -Sonsuz döngü
#Artırma değeri olmadığı için sürekli 1 olarak devam eder.
sayi = 1

while sayi == 1:
    print(sayi)

 ### FOR   DÖNGÜSÜ ###
##                   ##
##                   ##
 #####################  
# for döngüdü in' den sonra ayzdığımız yapının bütün değerleri üzerinde dolanıp, eleman sayısı kadar içindeki kodu çalıştıracak.
# x in <obje> ile tanımlandığında, x döngünün her adımında in den sonra tanımlanan yapının elmanlarının değerini alacak.

# for değişken in <obje>

#for döngüsünün başında <değişken>, <obje>' nin ilk elmanının değerini alıyor. İçindeki kod 1 kere çalışıp bittikten sonra ikinci kere çalıştırılıyor ve
# <değişken>, <obje>' nin ikinci elmanının değerini laıyor. Bu <obje>' nin tüm elemanları bitene kadar devam ediyor.

#Örnek 1 - string içerisinde dolaşrak elamnları ekrana yazdırır.
for c in "heyyoo":
    print(c)

#Örnek 2 - 1 den 100 e kadar olan sayıların toplamını yazdırır.
toplam=0
for x in range(1,101):  #range metodu aralık belirtmemize yarar.
    toplam += x
    print("{} + {}".format(toplam,x))
print(toplam)

#Örnek 3
toplam = 1
for i in range(5):
    toplam *= 5
print(toplam)

#Örnek 4
toplam = 1
for _ in range(5):
    toplam *= 5
print(toplam)

  ### FOR vs WHILE DÖNGÜSÜ ###
   ##                      ##
    ##                   ##
     #####################  
#while yapısında kaç kere iterasyon yapacağımızı bilmiyoruz, for' da eleman sayısı kadar iterasyon var. (Break ve continue ile bölünmezse)
# Aslında for döngüsünü while döngüsü kullanarak yazabiliriz ama while döngüsünü for döngüsü kullanarak ayzamayız. Çünkü for' da test mekanizması yok.

#Örnek  - for döngüsü ile yazdığımız sörneğin while ile yazımı.

s= "hey"
for c in s:
    print(c)
###############################

s = "hey"
n= len(s)
index = 0
while index < n: 
    print(s[index])
    index += 1