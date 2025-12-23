import sys
from stats import split_text, count_character, sort_list, print_letter

if len(sys.argv) > 1  :
    filepath = sys.argv[1]
else :
    print("============ BOOKBOT ============")
    print("You need to add the filepath")
    print("of the book you want to analyse.")
    print("Usage: python3 main.py <path_to_book>")
    print("============= END ===============")
    filepath = None
    sys.exit(1)
"""elif sys.argv[1] != None :
    filepath = sys.argv[1]"""


def get_book_text (filepath) :
    with open(filepath) as f :
        return f.read()
    

def main () :
    text = get_book_text(filepath)
    num_words = len(split_text(text))
    num_characters = count_character(text)
    #print(num_characters)
    sorted_list = sort_list(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_letter(sorted_list)
    print("============= END ===============")



    return

main()
