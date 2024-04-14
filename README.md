
Fizibilite Raporu: Lyapunov Exponents Analizi – Nisasu Bozkurt (210541062)

1. Giriş

Bu fizibilite raporu, dinamik sistemlerde Lyapunov Exponents kullanarak kaotiklik derecesini değerlendirmeyi, sistemdeki stabiliteyi analiz etmeyi ve öngörülebilirliği belirlemeyi amaçlamaktadır. Lyapunov Exponents, bir sistemin başlangıç koşullarındaki küçük değişikliklerin zaman içinde nasıl büyüdüğünü ölçerek sistemdeki karmaşık davranışları anlamamıza yardımcı olur.

2. Amaç ve Hedefler

Bu analizdeki ana amaçlar şunlardır:
   - Sistemimizin kaotik olup olmadığını belirlemek.
   - Kaotiklik derecesini ölçmek ve sistemdeki karmaşıklığı değerlendirmek.
   - Sistemdeki stabiliteyi analiz etmek ve öngörülebilirliği değerlendirmek.
   - Analiz sonuçlarına dayanarak kararlarımızı güçlendirmek ve sistem performansını iyileştirmek için öneriler sunmak.

3. Lyapunov Exponents Hesaplama Yöntemi

Lyapunov Üstelleri
Bir sinyalin faz uzayı boyunca takip ettiği yol yörünge olarak adlandırılır. Lyapunov üsteli, komşu yörüngelerin birbirlerinden ayrılma miktarının niceliksel ölçütüdür. Wolf tarafından Lyapunov üstellerine bakılarak sistemin kaotikliğinin değerlendirmesi yapılmıştır. Faz uzayının farklı yönelimleri için ayrılma miktarı farklılık göstermektedir. Neticede, faz uzayının boyutu miktarınca Lyapunov üstelinden oluşan bir spektrum elde edilir. Pozitif bir üstel başlangıçta birbirine yakın olan yörüngelerin zamanla uzaklaştığı anlamına gelir ayrıca pozitif üstelin büyüklüğü yörüngelerin ne kadar hızlı oranda birbirlerinden uzaklaştığını belirtir. Benzer şekilde üstelin negatif olması da yörüngelerin birbirlerine zamanla yaklaştığı anlamına gelir. Üstel değerlerinin büyük olması sistemin daha fazla tahmin edilemez olduğunu gösterir.

 <img width="256" alt="image" src="https://github.com/nisasubozkurt/YMGK-Modelling/assets/95681404/ea8758a6-02ac-4519-9afe-f07d51f9988a">



Lyapunov Exponents hesaplamak için aşağıdaki adımlar izlenir
   - Sistemimizin diferansiyel denklemlerini tanımlayacağız.
   - Başlangıç koşullarını belirleyeceğiz ve sistemimizi sayısal olarak çözeceğiz.
   - Başlangıç noktalarındaki küçük değişikliklerin zaman içinde nasıl büyüdüğünü izleyeceğiz.
   - Lyapunov Exponents yöntemini kullanarak başlangıç noktalarındaki ayrılma oranlarını hesaplayacağız.
   - Son olarak, hesaplanan Lyapunov Exponents değerlerini analiz ederek sistemimizin kaotiklik derecesini, stabilitesini ve öngörülebilirliğini değerlendireceğiz.

Python kodları:
```
      import numpy as np
      import chaotic_maps as cm
      
      cm.bifurcation_and_lyapunov_plots(
          cm.sin_map,
          init=0.2,
          parameter_range=np.linspace(0.6, 1, num=10000),
          deriv_generator=cm.sin_map_deriv,
          y_points=500,
          xlabel=r"$\mu$",
          ylabel=r"$x$",
          file_name="sine.png",
      )

```

![sine](https://github.com/nisasubozkurt/YMGK-Modelling/assets/95681404/57ef1868-5026-4d1d-b8e9-8d07b1e37545)


4. Analiz Adımları ve Teknikler

 <img width="375" alt="image" src="https://github.com/nisasubozkurt/YMGK-Modelling/assets/95681404/440835a1-288a-4336-aeae-696fdf5f2f6f">


Lyapunov Exponents analizi adımları şu şekildedir:
   a. Sistem denklemlerinin tanımlanması ve başlangıç koşullarının belirlenmesi.
   b. Sistem denklemlerinin sayısal çözümü ve sonuçların kaydedilmesi.
   c. Başlangıç noktalarındaki küçük değişikliklerin izlenmesi ve ayrılma oranlarının hesaplanması.
   d. Pozitif veya negatif Lyapunov Exponents değerlerinin belirlenmesi.
   e. Analiz sonuçlarının değerlendirilmesi ve yorumlanması.

5. Sonuçlar ve Değerlendirme

   1. Tanım: Lyapunov Exponents, bir dinamik sistemdeki farklı yönlere doğru olan ayrılma oranlarını ölçen bir matematiksel kavramdır. Bu oranlar, başlangıçta birbirine yakın olan iki noktanın sistem içinde zamanla birbirinden ne kadar ayrıldığını gösterir.

   2. Kaotik Davranışın Belirlenmesi: Bir sistemdeki Lyapunov Exponents pozitif ise, bu genellikle o sistemin kaotik davranış sergilediğini gösterir. Çünkü pozitif Lyapunov Exponents, başlangıçtaki küçük hataların zamanla büyüyerek sistemdeki öngörülemezliği artıracağını işaret eder.

   3. Negatif Lyapunov Exponents: Eğer bir sistemdeki Lyapunov Exponents negatif ise, bu sistemdeki noktaların zaman içinde birbirine yakınlaşacağı ve sistemdeki düzenin korunacağı anlamına gelir. Bu durumda sistem daha stabil ve öngörülebilirdir.

   4. Hesaplama Yöntemleri: Lyapunov Exponents hesaplamak için çeşitli yöntemler kullanılır. Bu hesaplama genellikle sistemdeki diferansiyel denklemlerin sayısal çözümleriyle yapılır. Birçok matematiksel modelleme aracı ve yazılım, Lyapunov Exponents hesaplamaları için özel fonksiyonlar veya modüller içerir.

   5. Fizibilite Raporunda Kullanımı: Lyapunov Exponents, özellikle kaotik sistemlerin incelendiği fizibilite raporlarında önemli bir yer tutar. Bu göstergeler, sistemdeki kaotik davranışın derecesini, stabiliteyi ve öngörülemezlik düzeyini analiz ederek raporunuzun teknik ve matematiksel temellerini güçlendirebilir.

Lyapunov Exponents ve diğer kaotik sistem analiz araçları, genellikle matematiksel modelleme, fizik, mühendislik ve ekonomi gibi alanlarda kullanılır. Bu göstergelerin doğru ve güvenilir şekilde hesaplanması, kaotik sistemlerin özelliklerini anlamak ve doğru kararlar almak için önemlidir.

6. Öneriler ve Sonuç

   1. Kaotiklik Derecesi:
   - Sistemimizin kaotik olduğuna dair pozitif Lyapunov Exponents değerleri elde edilirse bu, sistemdeki küçük başlangıç hatalarının zamanla büyüyerek öngörülemezlik düzeyini artırdığını göstermektedir.

   2. Stabilite:
   - Lyapunov Exponents analizi, sistemde negatif değerlerin de bulunduğunu göstererek belirli koşullarda sistemin stabil olduğunu ortaya koyar. Ancak pozitif Lyapunov Exponents değerleri, sistemdeki belirsizlikleri ve kararlı olmayan davranışları da işaret etmektedir.

   3. Öngörülebilirlik:
   - Sistemdeki pozitif Lyapunov Exponents değerleri, öngörülebilirlik açısından zorluklar yaratabilir. Bu durum, sistemdeki değişkenliklerin ve karmaşıklıkların dikkatle yönetilmesi gerektiğini gösterir.

   4. Öneriler ve İyileştirmeler:
   - Sistemdeki kaotik davranışları ve öngörülemezlikleri azaltmak için stabiliteyi artırmaya yönelik adımlar atılabilir. Bu, sistemdeki parametrelerin ve koşulların dikkatle kontrol edilmesini gerektirir.
   - Lyapunov Exponents analizinden elde edilen veriler, sistemin belirli koşullar altında kaotik olabileceğini göstermektedir. Bu nedenle, sistem üzerindeki değişikliklerin ve güncellemelerin dikkatle değerlendirilmesi önemlidir.
   - Sistemdeki kaotiklik derecesini azaltmak ve stabiliteyi artırmak için gerekli olan teknik ve stratejik düzenlemelerin yapılması tavsiye edilmektedir.
   - Analiz sonuçlarına dayanarak, sistemin gelecekteki davranışlarını öngörmeye yönelik daha kapsamlı bir analiz yapılması ve sürekli olarak izlenmesi önerilir.

7. Kaynaklar ve Referanslar
https://dergipark.org.tr/tr/download/article-file/324275

