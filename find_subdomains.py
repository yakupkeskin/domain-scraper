import threading
from database import Database
import requests
import concurrent.futures

found_list = []

def read_subdomains():
    with open('sub.txt', 'r') as file:
        # reading the file
        name = file.read()

        # using spilitlines() function storing the list
        # of spitted strings

        sub_dom = name.splitlines()
        # printing number of subdomain names present in
        # the list

        print(f"Number of subdomain names present in the file are: {len(sub_dom)}\n")
        return sub_dom


def domain_scanner(domain_name, subdomain):
    url = f"https://{subdomain}.{domain_name}"
    # using try catch block to avoid crash of the
    # program
    try:
        # sending get request to the url
        requests.get(url)

        # if after putting subdomain one by one url
        # is valid then printing the url
        print(f'[+] {url}')
        # if url is invalid then pass it
        return url, subdomain
    except requests.ConnectionError:
        pass
    return " "


def write_found_domains(found_list):
    with open('found.txt', 'w') as file:
        for subdomain in found_list:
            file.write(subdomain+"\n")


def use_threads(subdomains, domain_name, threads):  # Threads
   
    print('----FOUND URLS ----')
    num_of_subdomains_for_each_thread = int(len(subdomains) / threads)
    mod = len(subdomains) % threads
    list_of_threads = []
    thread_images = []
    number_sayac = 0
    for i in range(threads):
        if number_sayac + num_of_subdomains_for_each_thread + mod == len(subdomains):  # Tam bölünmeyen durumlarda kalanı son threadin listesine ekle.
            thread_images = subdomains[number_sayac:]
            list_of_threads.append(thread_images)
            break
        else:
            thread_images = subdomains[
                            number_sayac:number_sayac + num_of_subdomains_for_each_thread]  # Threadlere gönderilecek listeleri eşit böl.
            number_sayac += num_of_subdomains_for_each_thread
            list_of_threads.append(thread_images)

    thread_results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(domain_scanner, domain_name, subdomain) for subdomain in subdomains]
        db = Database()
        for f in concurrent.futures.as_completed(results):
            if f.result() != " ":
                thread_results.append(f.result()[0])
                db.add_sub(f.result())
                write_found_domains(thread_results)
    return thread_results


if __name__ == '__main__':
    # inputting the domain name
    dom_name = input("Enter the Domain Name:")
    # read the subdomain text file
    subdomains = read_subdomains()
    results = use_threads(subdomains, dom_name, 10)
    
    
    

