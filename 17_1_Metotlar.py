"""
Python Metot Türleri
Python sınıflarında, temel olarak 3 farklı şekilde metot tanımı yapılabilir.

Örnek (Instance) metotları -Python'da yeni bir sınıf tanımlandığınız, yazdığınız metotlar öntanımlı olarak, örnek (instance) metotlarıdır.
 Örnek metotları, ilk argüman olarak, kendisini çağıran örneğe bir referans alır. Böylece, geçerli örneğin niteliklerine erişim ve müdahale imkanı bulurlar.

Statik (@staticmethod) metotlar - Statik Metotlar, kendisini hangi sınıf veya örneğin çağırdığını bilmez. Sadece kendine verilen argümanları bilir,
 örnek veya sınıf metotları gibi, gizli bir ilk argüman almazlar. Bu yönden bakıldığında, bu fonksiyonun sınıf içinde yazılmasıyla, sınıf dışında yazılması arasında,
hiçbir fark yoktur. Ancak, aynı modül içerisindeki birçok fonksiyonu anlamsal bütünler içinde toplamak gerektiğinde kullanılabilir.
 Bunları tanımlamak için, metot tanımından önce @staticmethod dekoratörü kullanılır.

Sınıf (@classmethod) metotları - 
Diğer yandan, sınıf metotları, ilk argüman olarak, kendisini çağıran sınıfa veya kendisini çağıran örneğin sınıfına mecburi/otomatik bir referans alır. Bunu o sınıfın
bir örneğini oluşturmak istediğiniz durumlarda (bkz: Factory) kullanabilirsiniz. Kendisini çağıran sınıfa bir referans aldığı için, alt sınıflarda da istenildiği gibi çalışacaktır. 

Bunların arasındaki başlıca fark, aldıkları argümanlardır. Örnek metotlarına, ilk argüman olarak, objenin kendisine bir referans gönderilir. 
Bu argümana, geleneksel olarak self adı verilir. Statik metotlar, kendisini çağıran sınıf veya örnek hakkında herhangi bir bilgiye sahip değildir. 
Bunlar, işlevini kaybetmeden, sınıf dışında da aynı şekilde tanımlanabilir.
Sınıf metotları ise, otomatik olarak, kendisini çağıran sınıfa veya örneğin sınıfına bir referans alır. Bu argümana da geleneksel olarak cls adı verilir.
Örnek (Instance) Metotları



"""