import csv
from math import *  ##utilisation de floor et ceil pour larrondi a lunité
from urllib.parse import urljoin
import os
import requests
from bs4 import BeautifulSoup
##final

os.makedirs("img/", exist_ok = True)
image_index = 0
file_index = 0

###########recuperation de toute les url des differente category#######
siteToscrap = 'https://books.toscrape.com/'
url = []
response = requests.get(siteToscrap)
if response.ok:
    soup = BeautifulSoup(response.content, 'html.parser')
    resulta_raw = soup.select(".nav ul>li>a")
    for res in resulta_raw:
        url.append(urljoin(siteToscrap, res['href']))

# url='http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html'
for url in url:
    file_index += 1
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        resulta_raw = soup.select_one(
            ".form-horizontal strong")  ###stock le tag strong qui a la valeur du nombre de "result"
        resultaVrai = int(
            resulta_raw.text)  # ont extrai le nombre du resulta puis on le converti en int pour pouvoir lexploiter
        nombreOfPages = floor(
            resultaVrai / 20 + 1)  ###ont divise le tout par 20 +1 pour compter le nombre de pages disponibles
        print("il y a " + str(nombreOfPages) + ' pages disponibles!')
        ### ont connais le nombre de pages, let extrat some value

        #####################getting product page url##########
        link = []  # les url seront stockée dans link

        nombrePage = 1

        while nombrePage <= int(nombreOfPages):
            # url='http://books.toscrape.com/catalogue/category/books/mystery_3/page-'+str(nombrePage)+'.html'
            if nombrePage == 1:
                url2 = url.replace("page-" + str(nombrePage), 'page-' + str(nombrePage))
            else:
                url2 = url.replace("page-" + str(nombrePage - 1), 'page-' + str(nombrePage))
            print(url2)
            print("boucle")
            response = requests.get(url2)
            nombrePage += 1
            if response.ok:
                soup = BeautifulSoup(response.content, 'html.parser')
                product_page_url = soup.select("section ol li h3 a[href]")
                for pdpu in product_page_url:
                    # print(pdpu['href'])
                    #####tout les liens sont extrait dans une liste
                    # response=requests.get(link[0])
                    # print(urljoin(url,pdpu['href']))# comme nous avont affaire à des urls relatives nous utilisont urljoint pour pallier au probleme
                    link.append(urljoin(url2, pdpu['href']))

    else:
        print("response not ok")

    with open('info' + str(file_index) + '.csv', 'w') as csvfile:
        fieldnames = ['title', 'upc', 'pdt', 'priceEx', 'priceInc', 'avail', 'url', 'rate', 'img_url', 'category',
                      'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    ## tout les lien sont bel et bien dans la variable link, sans faute de chemin d accès
    for link in link:
        image_index += 1
        response2 = requests.get(link)
        if response2.ok:
            soup2 = BeautifulSoup(response2.content, 'html.parser')
            tableau = soup2.select("table tr td")  # bug avec tbody
            product_info = ['UPC', 'PDT', 'PriceEx', 'PriceInc', 'Tax', 'Avail', 'NOR']
            tableaulist = []
            for tab in tableau:
                tableaulist.append(tab.text)
            product_dict = dict(zip(product_info, tableaulist))
            print(product_dict)

            ########tout le tableau est stocké dans la variable product_dict

            title = soup2.select("article h1")
            titlelist = ""
            for tit in title:
                titlelist = tit.text
                print(tit.text)

            ##########we got the title now#########

            description = soup2.select('.product_page>p')
            descriptionlist = ""
            for desc in description:
                descriptionlist = desc.text
                print(desc.text)

            ####we got now the.text########

            category = soup2.select("ul>li:nth-child(n+3)>a")
            categorylist = ""
            for cat in category:
                categorylist = cat.text
                print(cat.text)

            #####"we got the category now#####

            image_url = soup2.select("article div>img")

            for img in image_url:
                image_url_real = img['src']
                # print(img['src'])
            image_url_complete = urljoin(link, image_url_real)  #
            print(image_url_complete)
            ##### we got the image_url now####
            rating = soup2.select('div>p:nth-child(n+4)')
            ratelist = ""
            for rate in rating:
                ratelist = rate["class"][1]
                print(rate['class'][1])
            # we got the rate too
            # affichage du nombre available
            product_dict['Avail'] = product_dict["Avail"].split()
            print(product_dict['Avail'][2][1:])  #

            ##############parametrage d une fonction pour lecriture des fichier csv###############

            def write_csv(title, upc, pdt, priceEx, priceInc, avail, url, rate, img_url, category, description):
                with open('info' + str(file_index) + '.csv', 'a') as csvfile:
                    fieldnames = ['title', 'upc', 'pdt', 'priceEx', 'priceInc', 'avail', 'url', 'rate', 'img_url',
                                  'category', 'description']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'title': title, 'upc': upc, 'pdt': pdt, 'priceEx': priceEx,
                                     'priceInc': priceInc, 'avail': avail, 'url': url, 'rate': rate, 'img_url': img_url,
                                     'category': category, 'description': description})

                return print('ouverture faite correctement')


            write_csv(titlelist, product_dict["UPC"], product_dict["PDT"], product_dict["PriceEx"][1:],
                      product_dict["PriceInc"][1:], product_dict['Avail'][2][1:],
                      link, ratelist, image_url_complete, categorylist, descriptionlist)
            imgdata = requests.get(image_url_complete)
            with open("img/image" + str(image_index) + '.jpg', "wb") as imagefile:  ####opening in binary mode
                imagefile.write(imgdata.content)
        else:
            print('response not ok')
