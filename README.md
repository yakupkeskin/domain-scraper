# domain-scraper

#Domain Scraping:
Subdomain bulma kısmı için 50 tane subdomain bulunan bir txt dosyası kullanıldı.(sub.txt) 
find_subdomains.py scripti çalıştırıldığında kullanıcıdan bir domain girilmesi istenir. 
Girilen domaine sub.txt dosyasındaki subdomainler eklenerek bir get request isteği atılır.
Atılan istek bir try except bloğunda kontrol edilir. 
Requestten connection error alınırsa subdomainin olmadığı anlamına gelir, eğer hata alınmazsa isteğin başarılı olduğu anlaşılır.
Bazı istekler çok vakit aldığı için burada thread kullandım. Bu sayede istekten gelecek cevaba kadar başka istekler de atılır.
Bulunan subdomainler mysql veritabanına ve found.txt dosyasına yazılır.


#Whois Parser:
Whois kütüphanesi kullanıldı.
Bulunup found.txt'ye yazılmış subdomainler üzerinde çalıştırıldı.
Raw data, creation_date, expiration_date, company_name,regitrar alanlarını database'e yazıldı.


#Flask App:
Database'e yazılan değerleri görüntüleyebilmek için bir flask uygulaması yazıldı.
Home page'de database'deki whois tablosuna ve domains tablosuna erişim sağlayan sayfalara ait linkler mevcuttur.
Bu linklerdeki sayfalarda database'deki whois ve domains verileri tablolar halinde gösterilir.

Kullanım senaryosuna örnek:
https://www.youtube.com/watch?v=bCJNuVyH0Ww
