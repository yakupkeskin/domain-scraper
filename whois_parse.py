import whois
from database import Database
#w = whois.whois('webscraping.com')
#w.creation_date
#w.expiration_Date
#registrar = w.registrar
#print(registrant_name)
#print(w)

db = Database()



with open('found.txt', 'r') as file:
    domains = file.read().split("\n")
    for domain in domains:
        w = whois.whois(domain)
        print('Whois Parsing: ', domain)
        raw = w.text
        creation_date = w.creation_date
        expiration_date = w.expiration_date
        registrar = w.registrar
        company = w.domain_name
        db.add_whois({'domain':domain,'creation_date':creation_date,'expiration_date':expiration_date,'registrar':registrar,'company':company,'raw':raw})



