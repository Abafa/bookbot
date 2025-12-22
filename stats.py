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

def sort_on(item) :
    return item["num"]


def sort_list (dictionaries):

    unsorted_list = []
    for c in dictionaries :
        unsorted_list.append({
            "char" : c,
            "num" : dictionaries[c]
        })
    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list

def print_letter (sorted_list) :
    for i in range(1, len(sorted_list)) :
        if sorted_list["char"].isalpha() :
            
            
            return

        """check si char est alphabetique
           si oui, print (f"{char[i]}: {num[i]})
           si non, skip
        """

    return