import requests
from bs4 import BeautifulSoup
from math import *##utilisation de floor et ceil pour larrondi a lunité
from urllib.parse import urljoin
import time
import csv


url='http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html'
response=requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text,'html.parser')
    resulta_raw=soup.select_one(".form-horizontal strong")###stock le tag strong qui a la valeur du nombre de "result"
    resultaVrai=int(resulta_raw.text)#ont extrai le nombre du resulta puis on le converti en int pour pouvoir lexploiter
    nombreOfPages=floor(resultaVrai/20 +1)###ont divise le tout par 20 +1 pour compter le nombre de pages disponibles
    print("il y a "+str(nombreOfPages)+' pages disponibles!')
    ### ont connais le nombre de pages, let extrat some value
    
    #####################getting product page url##########
    link=[]#les url seront stockée dans link
    product_page_url=soup.select("section ol li h3 a[href]")
    for pdpu in product_page_url:
        #print(pdpu['href'])
        #####tout les liens sont extrait dans une liste
        #response=requests.get(link[0])
        #print(urljoin(url,pdpu['href']))# comme nous avont affaire à des urls relatives nous utilisont urljoint pour pallier au probleme
        link.append(urljoin(url,pdpu['href']))

else:
    print("response not ok")
## tout les lien sont bel et bien dans la variable link, sans faute de chemin d accès
response2=requests.get(link[0])
if response2.ok:
    soup2=BeautifulSoup(response2.text,'html.parser')
    tableau=soup2.select("table tr td")#bug avec tbody
    product_info=['UPC','PDT','PriceEx','PriceInc','Tax','Avail','NOR']
    tableaulist=[]
    for tab in tableau:
        tableaulist.append(tab.text)
    product_dict=dict(zip(product_info,tableaulist))
    print(product_dict)
    
    ########tout le tableau est stocké dans la variable product_dict
    title=soup2.select("article h1")
    for tit in title:

        print(tit.text)
    ##########we got the title now#########
    description=soup2.select('.product_page>p')
    for desc in description:
        print(desc.text)
    ####we got now the text########
    category=soup2.select("ul>li:nth-child(n+3)>a")
    for cat in category:
        print(cat.text)
    #####"we got the category now#####
    image_url=soup2.select("article div>img")
    for img in image_url:
        image_url_real=img['src']
        #print(img['src'])
    image_url_complete = urljoin(link[0],image_url_real)
    print(image_url_complete)
    ##### we got the image_url now####
    rating=soup2.select('div>p:nth-child(n+4)')
    for rate in rating:
        print(rate['class'][1])
    #we got the rate too
    #affichage du nombre available
    product_dict['Avail']=product_dict["Avail"].split()
    print(product_dict['Avail'][2][1:])

    with open('info.csv', 'w') as csvfile:
        fieldnames = ['title', 'upc','pdt','priceEx','priceInc','avail','url','rate','img_url','category','description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'title': 'Baked'})
        writer.writerow({'upc': 'Lovely'})
        writer.writerow({'pdt': 'Wonderful'})


else:
    print('response not ok')
        



