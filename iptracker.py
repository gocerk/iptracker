import requests
from bs4 import BeautifulSoup

bruh = input("Enter ip adress")
url = requests.get("https://www.ip-adress.com/ip-address/ipv4/" + str(bruh))
urlcon = url.content 
soup = BeautifulSoup(urlcon , "html.parser")
ipadress = soup.find_all("td")
results = []
for ip in ipadress : 
    results.append(ip.text)

ipadd = results[0]
city = results[3]
country = results[4]
isp = results[6]
citycode = results[15]

print("Ip adress : " , ipadd)
print("Country : " , country)
print("City : " , city)
print("ISP : " , isp)
print("City code : " , citycode)
