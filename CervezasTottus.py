from bs4 import BeautifulSoup
import requests
import json

URL_BASE ="https://www.tottus.cl{}"
URL = URL_BASE.format("/api/product-search/by-category-slug?slug=cervezas-cat010403&sort=score&page=1&perPage=500")
FILEJSON = "cervezas-tottus.json"
TOTAL=0

def beerTottus(url, np=1):
    global TOTAL
    
    data = {}
    data['cervezas'] = []

    req = requests.get(url)
    statusCode = req.status_code

    if statusCode == 200:
        html = BeautifulSoup(req.text, "html.parser")
        entradas = json.loads(html.text)

        for entrada in entradas['results']:
            #Nombre
            name = entrada['name']
            #Descripción
            desc = entrada['description']
            #Precios
            if len(entrada['prices']) > 0:
                regularPrice = entrada['prices']['regularPrice']
                currentPrice = entrada['prices']['currentPrice']
            else:
                regularPrice = ''
                currentPrice = ''
            #Imagenes
            if len(entrada['images'])>0:
                image = entrada['images'][0]
            else:
                image = 'https://www.tottus.cl/static/images/temp/placeholder-image.jpg'

            data['cervezas'].append({
                'name': name,
                'description': desc,
                'regularPrice': regularPrice,
                'currentPrice': currentPrice,
                'image': image
            })

            with open(FILEJSON, 'w', encoding='utf8') as outfile:
                json.dump(data, outfile, indent = 4, ensure_ascii=False)

            TOTAL+=1
        print('Se obtuvieron {} productos'.format(TOTAL))

# Ejecutar función para traer los datos desde el sitio tottus.cl
beerTottus(URL)