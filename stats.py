def split_text (file) :
    return file.split()

def count_character (file) : 

    characters = {}
    lowered_file = file.lower()  # prend file et lower() tout.


    for i in lowered_file :      # itere sur toute la string et compare si :
        if i in characters :     # si lettre checkée présente dans characters => characters =+
            characters[i] += 1
        else :                   # sinon add le nouveau truc dans le dico et set le a 1 
            characters[i] = 1 
    
    return characters