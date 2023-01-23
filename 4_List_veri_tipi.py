###     LİSTELER     ###
###                  ###
###                  ###
########################  


#https://neave.com/


''''
Python Programlama Dilinde 4 tür dize (array) bulunur. Bunlar;

List, sıralanabilir ve değiştirilebilir dizeler. Bu tarz dizelere aynı üyeler tekrar eklenebilir.
Tuple, sıralanabilir ancak değiştirilemez dizelerdir. Aynı üyeler birden fazla eklenebilir.
Set sıralanamaz ve aynı üyeleri kabul etmez.
Dictionary sıralanamaz ancak değiştirilebilir ve listelenebilir. Aynı üyeler eklenemez.
Bir dize kullanırken dizelerin özelliğini bilmek ve ona göre kullanmak hem zaman kazandırır, hem işimizi kolaylaştırır.

List
Sıralanabilir ve değiştirilebilir veriler topluluğudur. Nesneler köşeli parantezler arasına yazılır.


Normal şartlarda değişken oluştma ve değişkenlere değer atama yapısı şöyleidr;'''


sayi_1=1
sayi_2=2
sayi_3=3
'''
Bunların hepsi bir sayıyı ifade etmektedir, peki biz bu sayıları bir arda tutsak dha mantıklı olmaz mı?
* List veri tipi, birden çok veriyi gruplayıp bir arada tutmak istediğimizde kullanabileceğimiz bir yapıdır.
* List ler [] parantzler ile belirtilir. [sayi_1,sayi_2,sayi_3]
* list ler içsel yapı içerdiği için  non-scalar veri tipidir.
* Elemanları arasına virgül koyarak farklı eleman belirtmeye başladığımı ifade ediyorum.
* List lerin içerisinde tutulacak verilerin tiplerinin bir şartı yoktur. Bütün veri tipleri tutulabilir (int, float, bool, string vs.)
* List içerisinde liste bile tutulabilir.
* Listeler mutable(değişkebilir) veri tipleridir. Elemanları güncellenebilir.
'''
notlar1 = [75, 80, 50, 65, 90]
notlar = [sayi_1, sayi_2, sayi_3]
["a","b"]
[True, False]
[[1,2],[3,4,5]]
l = [1,2, "sayi",True, [4,5]] # şeklinde de liste olabilir.


#Indexing ve Slicing
print(notlar1)
print(notlar[0]) # 0. indexte bulunan değer
print(notlar[-1]) #Listenin sonuncu elemanını verir

######Slicing########
#Bundan başla son elemana kadar git demektir slicing

print(notlar[1:])
print(notlar[1:3]) #Son elemanı dahil etmez

#Listelerin Elemanları Değiştirilebilir.
#Listeler mutable veri tipleridir. Elemanları güncellenebilir. Stringlerde bu geçerli değildir stringler immutable içeriği değiştirilemez.

####->len()
len(notlar) 
####->Listenin sonuna eleman eklemek
l = [1,2,3]
l.append(20)
print(l)

####->İçine yazılan birden çok elelmanı listenin içine ekler.
l = [1,2,3]
l.extend([200,300,400])
print(l)

####-> Spesifik bir indexe eleman eklemek
l = [1,2,3]
l.insert(0,100)
print(l)

####-> remove() Remove sadece ilk gördüğü 2 değerini siler. Listede birden fazla 2 varsa onları silmez.
l = [1,2,3]
l.remove(2)
print(l)

####-> pop() Listenin belirli bir indexindeki elemanı silmeye ve o değeri döndürmeye yarar. remove() sadece siler, pop() aynı zamanda o değeri döndürür.
l = [1,2,3]
l.pop(1) #index değerini parametre alır.
print(l)

####-> count() Belli bir değer listenin içinde kaç defa görünüyor?

l= [1,2,3,1,2,2]
print(l.count(2))

####-> ALIASING Kutular değil etiketler isimlendirilir. 

####->Listelerde Concatenation, listeelri birbirilyle birleştirmek için + operatorü concatenation yapar.
l=[1,2,3]
l2=[4,5,6]
print(l+l2)

#############Döngülerle Listeler######
my_list = ["elma", "armut", "muz"]
for x in my_list:
  print(x)

#############

my_list = ["elma", "armut", "muz"]
for i in range(len(my_list)):
   print(my_list[i])


############################
i = 0
while i < len(my_list):
   print(my_list[i])
i = i + 1

#### my_list adlı listemizdeki meyvelerin içerisinde “a” harfi olan elemanları yeni listemize ekle anlamı taşıyor. Kullanımı daha kısa şekilde yazmamız da mümkün,
my_list = ["elma", "armut", "muz"]
new_list = []

for x in my_list:
    if "a" in x:
        new_list.append(x)

print(new_list)
