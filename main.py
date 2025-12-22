def get_book_text (filepath) :
    with open(filepath) as f :
        return f.read()
    
from stats import split_text
from stats import count_character

def main () :
    text = get_book_text("books/frankenstein.txt")
    num_words = len(split_text(text))
    print (f"Found {num_words} total words")
    num_characters = count_character(text)
    print(num_characters)

    return

main()
