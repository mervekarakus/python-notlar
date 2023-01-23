"""
* Listeler bize bir arada tutulması anlamlı olacak verileri bir arada tutma gücü verir.
* Mesela bir sınıftaki 3 öğrencinin sınavdan aldıkları notlar

notlar = [80, 72, 55]

* Bu listedeki 1. eleman ilk öğrenciyi, 2. eleman 2. öğrenciyi, 3. eleman 3. öğrenciyi....
* Ben aynı zamanda bu öğrencilerin isimlerini de tutmak istiyorsam, isimleri için ayrı bir liste oluşturmam lazım. Kuracağım
mantık için bu iki listenin elelman sayısı aynı olmalıdır. notlar[0] bana ilk öğrencinin notunu verecek.
"""
notlar = [50,70,100]
isim= ["Ege","Deniz","Gizem"]

print(isim[0]," adlı öğrencinin notu",notlar[0])


"""
* Dictionay yapısının elemanlarına erişmek için belirli key ler kullanıcağız ve o da bize value ler verecek.
* Dictionaryleri süslü parantez {} ile belirteceğiz.
* Formumuz {key1:value1,key2:value2...}
* Elemanlarına ulaşmak için önür non-scalar veri tiplerinde yaptığımız gibi [ ] kullanacağız. 
* Dictionayrlerin elemanlarına ulaşmak için belirlediğimiz key leri kullanacağız., integer indexing değil.
* Dictionaylerin keyleri immutable herhangi bir yapıda olabilir. value lar mutable(değiştirilebilir) da immutable(değiştirilemez) da olabilir.. 
* int, float, bool, string, list,tuple, set, even dictionary itself !
* keyler sadece stringlerden oluşmayabilir. 0:50 şeklinde bir sözlük elemanı tanımlanabilir.

"""
notlar = {"Deniz":80, "Ege":60,"Gizem":100}
print(notlar["Ege"])

####->
ogrenciler = {"Deniz": {"not":80, "ogrenci_no":703}, "Ege":{"not":72, "ogrenci_no":408}, "Gizem": {"not":95, "ogrenci_no":690}}

####-> mutable, değiştirilebilir elemanları olabilir.
notlar = {"Deniz":80, "Ege":60,"Gizem":100}
notlar["Ege"] = notlar["Ege"]+5
print(notlar["Ege"])

####-> len() fonksiyonu dictionarylerde kullandığımız zaman bize kaç tane key  varsa onun sayısını veriyor.
print(len(notlar))

####-> Eleman EKlemek
notlar["Mert"]=58
print(notlar)

####-> Sİlme işlemi
del notlar["Mert"]