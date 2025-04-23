import sys



def get_book_text(path):
    with open(path) as f:
        return f.read()
    
from stats import count_words
from stats import count_characters
from stats import sort_characters
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    char_list = sort_characters(char_counts)
    print("============ BOOKBOT ==============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    for char_dict in char_list:
        char = char_dict["char"]  # Adjust this key name based on your dictionary structure
        count = char_dict["count"]     # Adjust this key name based on your dictionary structure
        if char.isalpha():
            print(f"{char}: {count}")

main()