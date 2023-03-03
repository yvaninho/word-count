# -*- encoding: utf-8 -*-
import logging 
import re 

""" 
La fonction world_count prend en parametre un text (string)
le split par espace et compte le nombre d'occurence de chaque mot
"""

def world_count(text):

    logging.info("DEBUT DU COMPTAGE DES MOTS...")
    words = text.split()
    word_dic ={}
    pivot_words=[]
    for word in words:
        if word not in pivot_words:
            word_dic[word]=words.count(word)
            pivot_words.append(word)
    logging.info("FIN DU COMPTAGE...")
    logging.info("LE NOMBRE DE MOTS TOTAL EST DE "+ len(words))
    return word_dic




