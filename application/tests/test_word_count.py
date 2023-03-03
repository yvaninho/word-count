from src.core import *



def test_wordcount():
     input_text = "Ceci est un simple projet python pas le python"
     output = [('python',1),('Ceci ',1),('est',1),('un',1),('simple',1),('projet',1), ('pas',1),('le',1)] 
     
     result = world_count(input_text)

     assert result == output