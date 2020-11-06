import requests
from bs4 import BeautifulSoup

girdi = input("Ip adresini girin")
url = requests.get("https://www.ip-adress.com/ip-address/ipv4/" + str(girdi))
urlcon = url.content 
soup = BeautifulSoup(urlcon , "html.parser")
ipadress = soup.find_all("td")
results = []
for ip in ipadress : 
    results.append(ip.text)

ipadd = results[0]
sehir = results[3]
ulke = results[4]
isp = results[6]
sehircode = results[15]

print("Ip adresi : " , ipadd)
print("Ulke : " , ulke)
print("Sehir : " , sehir)
print("Internet saglayicisi : " , isp)
print("Sehir kodu : " , sehircode)