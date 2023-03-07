from src.core import *


def test_format_text():
     """ GIVEN """
     input_text = "j'aime Bien-sur la data, et l'informatique"
     output = "j aime bien sur la data  et l informatique"
     """ WHEN """
     result = format_text(input_text)
     """ THEN """
     assert result == output

def test_wordcount():
     """ GIVEN """
     input_text = "Ceci est un simple projet python pas le python"
     output = [('python',2),('ceci',1),('est',1),('un',1),('simple',1),('projet',1), ('pas',1),('le',1)] 
     """ WHEN """   
     result = word_count(input_text)
     """ THEN """
     assert result == output

def test_core():
     """ GIVEN """
     input_text = "ceci-Ceci est Un Micro-test d'informatique"
     output = [('ceci',2),('est',1),('un',1),('micro',1),('test',1),('d',1), ('informatique',1)] 
     """ WHEN """
     result = word_count(format_text(input_text))
     logging.info(result)

     """ THEN """
     assert result ==output 