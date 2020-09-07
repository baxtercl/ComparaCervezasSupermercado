from bs4 import BeautifulSoup
import requests
import json

URL_BASE ="https://www.lider.cl{}"
URL = URL_BASE.format("/supermercado/category/Bebidas-Licores/Cervezas/_/N-1mi8n3m?N=&No=0&Nrpp=500&isNavRequest=Yes")
FILEJSON = "cervezas-lider.json"
TOTAL=0

def beerLider(url, np=1):
    global TOTAL
    data = {}
    data['cervezas'] = []

    req = requests.get(url)
    statusCode = req.status_code

    if statusCode == 200:
        html = BeautifulSoup(req.text, "html.parser")
        entradas = html.find('div', {"id": "content-prod-boxes"})

        for entrada in entradas.findAll("div",{"class":"box-product"}):
            name = entrada.find("span",{"class" : "product-name"}).text
            desc = entrada.find("span",{"class" : "product-description"}).text
            regularPrice = entrada.find("span",{"class" : "price-sell"}).text
            currentPrice = entrada.find("span",{"class" : "product-round"}).text
            image = entrada.find("img",{"class" : "img-responsive"})["src"]

            data['cervezas'].append({
                'name': name,
                'description': desc,
                'regularPrice': regularPrice.replace('$', '').replace('.', ''),
                'currentPrice': currentPrice.replace('$', '').replace('.', ''),
                'image': image
            })

            with open(FILEJSON, 'w', encoding='utf8') as outfile:
                json.dump(data, outfile, indent = 4, ensure_ascii=False)

            TOTAL+=1
        print('Se obtuvieron {} productos'.format(TOTAL))
        # Paginación en caso que fuese necesaria
        try:
            np+=1
            number="&page="+str(np)
            pagination = list(set([ x["href"] for x in html.find("ul",{"class" : "pagination pull-right"}).findAll("a",href=True) if number in x["href"]]))[0]
            grocery(URL_BASE.format(pagination),np)
        except Exception as e:
            pass

beerLider(URL)