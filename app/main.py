#!/usr/bin/env python
# coding: utf-8

# # Scraping Topito Top 10 des mangas les plus vendus

# Import des librairies 
import requests # Pour récupérer le code source de la page
from bs4 import BeautifulSoup # Pour scraper les données
from models.Manga import Manga # Import classe Manga
import pandas as pd
import matplotlib.pyplot as plot
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--number", type=int, help="Classement souhaité (entre 1 (le moins vendu) et 10 (le plus vendu))")
args = parser.parse_args()

# Récupère le code source et le sauvegarde dans une variable (request_text)
request_text = requests.get("https://www.topito.com/top-manga-vente-monde-temps")

# Instancie BeautifulSoup avec le request_text
soup = BeautifulSoup(request_text.content, "html.parser")

# Trouve les items et les sauvegardes dans une liste (items)
items = soup.find("div", class_="items").find_all("div", class_="item")
items

df = pd.DataFrame(columns=["name","url_img", "nb_sold"])


for item in items:
    if item.find("a"):
        url = item.find("img").get("data-src")
        str_nb_sold = str.split(item.find("h2").getText(),"(")
        nb_sold = int(str.split(str_nb_sold[1]," ")[0])
        name = item.find("a").getText()
        df = df.append(Manga.to_dict(url_img=url, name=name, nb_sold=nb_sold), ignore_index=True)

def getRanking(df : pd.DataFrame, nb):

    df = df.head(nb)

    df = df.sort_values(by=["nb_sold"] ,ascending=True)

    df.plot.bar(x="name", y="nb_sold", rot=70, title="Les mangas les plus vendus")

    plot.show(block=True)

    print(df.to_dict)


if args.number:
    getRanking(df, args.number)
else:
    getRanking(df, 10)