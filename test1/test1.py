import bs4, requests, webbrowser
from flask import Response
from pprint import pprint


LINK = "https://www.subito.it/annunci-emilia-romagna/vendita/hobby-collezionismo/reggio-emilia/?q=yu+gi+oh"
PRE_LINK = "https://www.subito.it/hobby-collezionismo/"

response=requests.get(LINK)
response.raise_for_status()

soup=bs4.BeautifulSoup(response.text, 'html.parser')
div_annunci=soup.find('div', class_="ItemListContainer_container__D_wWL")
a_annunci=div_annunci.find_all("a")
link_annunci=[]
for annuncio in a_annunci:
    link_annuncio=str(annuncio.get("href"))
    if PRE_LINK in link_annuncio:
        link_annunci.append(link_annuncio)

#pprint(link_annunci)

f = open("risultati_salvati.txt","a")
link_annunci_vecchi = [riga.rstrip("\n") for riga in open("risultati_salvati.txt")]
link_annunci_nuovi = []
for link_annuncio in link_annunci:
    if link_annuncio not in link_annunci_nuovi:
        link_annunci_nuovi.append(link_annuncio)
        f.write("%s\n" % link_annuncio)
f.close()
if link_annunci_nuovi:
    print("Nuovi annunci... apertura annunci...")
    for nuovo_link in link_annunci_nuovi:
        webbrowser.open(nuovo_link)
else:
    print("Non ci sono nuovi annunci")

input("\n Fine ")
