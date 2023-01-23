"""
* Tuple veri tipi listeler gibi birden çok veri tipini bir arada tutmamızı sağlar.
* Listelerden farklı olarak tuple' lar immutable dır.

* Mesela bir deniz fenerinin konumunu belirtmek istiyoruz. Bunun x ve y koordinat değerleri var (x,y). Deniz fenerini söküp götüremiyoruz, 
ben bu iki değerin sabit, değiştirilemez olmasını istiyorum. Burada bu iki değeri tutmak için tuple kullanmam mantıklı olabilir. 
Değişmeyeceğini bildiğim değerleri bir arada tutmak için;

* Tuple lar listeler gibi farklı veri yapılarında elemanlardan oluşabilir. Elemanları tuple bile olabilir.
* Tuple larda bir kere yapıyı belirledikten sonra güncelleme işlemi yapamıyoruz. Sabit kalıyor.
* tuple içerisinde tuple velirlenebilir
* Tuple içinde liste veri tipi olabilir.



"""
###-> Güncellenemez - item assignment hata verir
x=10
y=20
konum=(10,20)
konum[0]=100
print(konum)

####-> Tuple içerisinde bulunan listenin elmanının güncellenmesi
t = ([1,2,3], [4,5,6])
print(t)
t[0][0]= 100
print(t)

#################### List ve Tuple IN kullanımı #################
l = [1,2,3,4]
print(40 in l) # liste içinde 40 var mı?

####->
if 2 in l:
    print("hello world")
else:
    print("2 yok çıkış yapılıyor.")