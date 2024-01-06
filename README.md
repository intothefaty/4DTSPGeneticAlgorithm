TSP

Klasik TSP, bir satıcının başlangıç noktasına dönmek üzere verilen şehirlerin hepsini en kısa yoldan bir kez ziyaret etmesi gereken bir optimizasyon problemidir. 
TSP, karmaşıklığı nedeniyle hem teorik hem de pratik öneme sahiptir. 
Problem boyutu büyüdükçe optimal çözümü bulmak için gereken süre üssel olarak artar. 
Bu, büyük ölçekli TSP'ler için tam çözüm bulmanın pratikte imkansız olduğu anlamına gelir. 
Bu nedenle, çeşitli sezgisel ve yaklaşık çözüm yöntemleri geliştirilmiştir. 

4D TSP

4D Gezgin Satıcı Problemi (4D TSP), klasik TSP'nin karmaşıklığını daha da ileri götürür. 
Bu versiyonda, zamansal boyut ve/veya ek kısıtlamalar eklenir, bu da problemin çözümünü daha karmaşık hale getirir. Örneğin, bir noktaya belirli bir zamanda ulaşma gerekliliği veya çeşitli zaman aralıklarında değişen maliyetler gibi faktörler dikkate alınır.
 Bu, algoritma tasarımı ve optimizasyon stratejileri için yeni zorluklar yaratır ve mevcut yöntemlerin bu ekstra boyutu hesaba katması gerekir. 
4D TSP, geleneksel TSP'den daha karmaşık olduğu için, bu yeni yaklaşım, özellikle zaman ve diğer ek kısıtlamaların rol oynadığı durumlarda, daha etkili ve verimli çözümler sunma potansiyeline sahip. 
Bu tür gelişmeler, lojistik, seyahat planlaması ve benzeri alanlarda pratik uygulamalar için önemli katkılar sunar ve karmaşık optimizasyon problemlerine yaklaşımımızı yeniden şekillendirir.

Çok Ebeveynli Genetik Algoritmalar

Çok ebeveynli genetik algoritma, genetik algoritmanın geleneksel iki ebeveynli çaprazlama yaklaşımını genişleterek, çözüm havuzundan birden fazla ebeveynin genetik bilgisini birleştirmeyi içerir. 
Bu yöntem, genetik çeşitliliği artırarak ve gen havuzundan daha fazla bilgi kullanarak, yerel optimumlara takılma riskini azaltır ve genel çözüm kalitesini iyileştirmeye yardımcı olur. 
Çok ebeveynli yaklaşım, özellikle karmaşık optimizasyon problemlerinde, daha geniş bir arama alanını keşfetme ve daha iyi çözümlere ulaşma fırsatı sunar.

Yöntem

Genetik algoritmalarda popülasyon oluşturma, başlangıçta çeşitli çözümlerin rastgele seçilmesiyle başlar. 
Fitness hesaplama, her çözümün problemi ne kadar iyi çözdüğünü değerlendirir. Daha yüksek fitness değerine sahip bireyler, gelecek nesiller için tercih edilir. 
Evrimsel işlemler arasında seçilim, çaprazlama ve mutasyon bulunur. Bu süreçler, zamanla daha uygun çözümlere ulaşmak için popülasyonun evrimini sağlar.

10 şehirli, 10 bireyli popülasyonlu, 10 iterasyonlu ve mutasyon ihtimali 0.01 olan bir örnek output

<img width="412" alt="Screenshot 2024-01-06 at 11 00 27" src="https://github.com/intothefaty/4DTSPGeneticAlgorithm/assets/83587302/a4b81074-9416-4765-b9b8-cfad2c275006">
<img width="484" alt="Screenshot 2024-01-06 at 11 00 38" src="https://github.com/intothefaty/4DTSPGeneticAlgorithm/assets/83587302/51a36f4a-cef5-410d-9a01-eeb4b5f2bed2">
<img width="475" alt="Screenshot 2024-01-06 at 11 00 46" src="https://github.com/intothefaty/4DTSPGeneticAlgorithm/assets/83587302/7f29a91f-8c61-43a7-9130-3eb2fa84fc25">
<img width="456" alt="Screenshot 2024-01-06 at 11 00 55" src="https://github.com/intothefaty/4DTSPGeneticAlgorithm/assets/83587302/edd17d87-fa73-4e33-8982-bbf3c49de0ae">








