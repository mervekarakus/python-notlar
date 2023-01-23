"""

Fonksiyonlar: Girilen inputlardan işlemler yapıp bir output yani çıktı yaratıyor.


* Bir fonksiyonu çalıştırdığımızda onun sonucuyla bir şeyler yapmak isteyebilirim. Sonucu bana versin diye özellikle söylemem lazım ve bunu return 
keyword(anahtar kelime)'u ile sağlayacağız.
* return yazmasaydık fonksiyon hiç bir şey döndürmezdi.
* fonksiyon tanımladığımı Python'a anlatmak için yapım:

def fonksiyonun_adı(input):

* öbür yapılarda da olduğu gibi, bir kod bloğunun belirttiğimiz yapıya ait olduğunu anlatmak için boşluk bırakarak içine yazmamız gerekiyor.
Verdiğimiz değerin karesini alan bir fonksiyon yazalım

"""
def square(x):
    return x*x

# Fonksiyonu tanımladıktan sonra tanımladığımız adla onu çağırabiliriz. Yapımız şöyle olacak: fonksiyonun_adı(input),
# bir fonksiyonu çağırmak için inputları ()'ın içine yazmalıyız. Bazı durumlarda hiç input olmayabilir, bazı durumlarda birden çok olabilir.
print(square(3))
a = square(5)
print(a)

####-> içiçe fonksiyon kullanılabilir

c = square(square(3)) #81
print(c)

####-> Hiçbir inputu olmayabilir.

def weird():
    return 5 # 5 döndürür.

#####-> Fonksiyonlar return' e geldikten sonrasına bakmıyor, return ün sağına yazılan değeri veriyor ve fonksiyonları çıkıyor.

def square(x):
    result = x*x
    return result

    print("Square of" + str(x) +":" + str(res)) #Burada print işlemi yapmaz yani çıktı vermez. return' in altınd aolduğu için 

a = square(4)
print(a)

####-> Print return den önce yazılırsa...
def square(x):
    result = x*x
    print("Square of" + str(x) +":" + str(result))
    return result


####-> Fonksiyon içerisinde koşullar ve döngüler kullanılabilir.

def f(x):
    res = x*x

    if x % 2 == 0:
        return res
    else:
        return res + 10
    print("Square of "+ str(x) + ":"+ str(res))

print(f(11))

####-> Fonksiyon içeriisnde döngü mantığı da olabilir.

def f(x): # x in değeri 10 girdi
    res = x * x # x in değeri 10 * 10 = 100 oldu
    
    for i in range(10): # i nin değerleri 0,1, .....,9
        res += 20       # x+20 = 120 
        return res      # return gördükten sonra döngüden çıktı.
        print("hey")    #Döngüye devam etmedi.
print(f(10))


####->  300 olur. For 9 a kadar döner ve her eferinde 20 eklenir x in değerine 
def f(x):
    res = x * x 
    
    for i in range(10):
        res += 20
    return res 

print(f(10)) # 300 olur. For 9 a kadar döner ve her eferinde 20 eklenir x in değerine 

####-> [120, 140, 160, 180, 200, 220, 240, 260, 280, 300]
def f(x):
    l = []
    res = x * x
    for i in range(10):
        res += 20
        l.append(res)
    return l
print(f(10))

####-> VOID FONKSİYONLARI - Değer döndürmeyen fonksiyonlar

def f(x):
    x = 2
####-> bu fonksiyon x' in karesini değer olarak bize vermiyor sadece ekrana bastırıyor
def square(x):
    print(x,"'in karesi:",x*x)

####-> Hem bir deer bastırıp hem de aynı anda o değeri döndürebilirdi.

def square(x):
    res = x * x
    print(x,"'in karesi:", x*x)

    return res
(4)

## Birden Çok İnput ##
def power(x, y):
    return x ** y
print(power(2,3))
# 2 nin 3. kuvveti


