import json
import random

# Charger les citations depuis un fichier JSON
with open("quotes.json", "r") as file:
    quotes = json.load(file)

# Afficher une citation aléatoire
print("Voici une citation inspirante pour vous :")
print(random.choice(quotes))
