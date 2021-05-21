import requests
from bs4 import BeautifulSoup
from math import *##utilisation de floor et ceil pour larrondi a lunité
from urllib.parse import urljoin

url='http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html'
response=requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text,'html.parser')
    resulta_raw=soup.select_one(".form-horizontal strong")###stock le tag strong qui a la valeur du nombre de "result"
    resultaVrai=int(resulta_raw.text)#ont extrai le nombre du resulta puis on le converti en int pour pouvoir lexploiter
    nombreOfPages=floor(resultaVrai/20 +1)###ont divise le tout par 20 +1 pour compter le nombre de pages disponibles
    print(nombreOfPages)
    ### ont connais ke nombre de page let extrat some value
    #####################getting product page url##########
    link=[]#les url seront stockée dans link
    product_page_url=soup.select("section ol li h3 a[href]")
    for pdpu in product_page_url:
        #print(pdpu['href'])
        #####tout les liens sont extrait dans une liste
    
        #response=requests.get(link[0])
        print(urljoin(url,pdpu['href']))# comme nous avont affaire à des urls relatives nous utilisont urljoint pour pallier au probleme
        link.append(urljoin(url,pdpu['href']))

    for a in link:
        print(a)

        ## tout les lien sont bel et bien dans la variable link, sans faute de chemin d accès
    response2=requests.get(link[0])
    if response2.ok:
        soup2=BeautifulSoup(response.text,'html.parser')
        print(soup2)

