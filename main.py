def get_book_text (filepath) :
    with open(filepath) as f :
        return f.read()
    
from stats import split_text, count_character, sort_list, print_letter

def main () :
    text = get_book_text("books/frankenstein.txt")
    num_words = len(split_text(text))
    num_characters = count_character(text)
    #print(num_characters)
    sorted_list = sort_list(num_characters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_letter(sorted_list)
    print("============= END ===============")



    return

main()
