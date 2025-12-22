def get_book_text (filepath) :
    with open(filepath) as f :
        return f.read()
    
def split_text (file) :
    return file.split()

def main () :
    text = get_book_text("books/frankenstein.txt")
    num_words = len(split_text(text))
    print (f"Found {num_words} total words")
    return

main()
