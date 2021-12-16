# Topito_Scraping

## Présentation

Ce projet consistait à scraper les données d'un site de notre choix, dans mon cas j'ai choisi de scraper le top 10 des mangas les plus vendus sur le site topito (https://www.topito.com/top-manga-vente-monde-temps).

## Technologies utilisées

- Python 3.8
- Docker
- Librairie BeautifulSoup 4

## Comment le lancer

Pour lancer le projet, il suffit d'entrer la commande suivante, qui va créer le conteneur

```bash
    docker-compose up --build -d
```
Une fois le conteneur lancé, entrer la commande suivante :

```bash
    docker exec scrap_topito_container python3 main.py [--number TOP_VOULU]
```
Si --number n'est pas entré, cela retournera le top 10 directement par defaut

Vous trouverez ensuite l'image du graphique en baton montrant le top voulu en fonction des ventes dans le dossier <b>data/analytics</b>
