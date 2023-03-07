# -*- encoding: utf-8 -*-
import logging 
from collections import Counter

""" 
La fonction world_count prend en parametre un text (string)
le split par espace et compte le nombre d'occurence de chaque mot
"""

def format_text(text):
    for charcter in "-.',\n":
        text = text.replace(charcter,' ')

    return text.lower()

def word_count(text):
    logging.info("DEBUT DU COMPTAGE DES MOTS...")
    words = list(map(lambda word : word.strip(), format_text(text).split()))
    logging.info( words)
    logging.info("LE NOMBRE DE MOTS TOTAL EST DE "+ str(len(words)))
    logging.info(Counter(words).most_common())
    return Counter(words).most_common()




