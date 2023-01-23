"""
* Set leri kümeler olarak düşünebiliriz.
* Sadece özgün değerleri tutan, içerisinde
 bir eleman var mı yok mu, başka bir
  setle hangi elemanları farklı gibi 
  işlemleri performaasnlı bir şekilde 
yapabileceğimiz bir veri yapısı.
* Dictionary ler gibi eleman sorgusu yapmak hızlıdır.
 Dictionary lerde key-value çift olarak bulunduğu
  için aynı uzunluktaki bir set ten daha fazla 
  yer kaplar.
* Set ler indexlenemez.
* Set ler mutabledır

"""
####-> Set yaratma {1,2,3,4,5}
s = {1,2,3,4,5}
print(s) 
####-> {1,2,3,4}
s2= {1,2,2,3,3,4}
print(s2)
####->Set yaratma
a={} #tipi dictionarydir
s = set() #tipi settir.
s.add(6)  #set e eleman ekleme
s.remove(2) #set in içinden silme
s.discard(10) #Eğer içeriisnde olmayan bir değeri hata almadan silmek istiyorsak discard kullanırız.

############# Differance (fark) ##################
s1 = set([1,5,10])
s2 = set([2,5,3])

s1.differance(s2) #s1 in s2 den farkı. Çıktı olarak set tipinde verir.
s1-s2 #yine farkını verir.

