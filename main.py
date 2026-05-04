from stats import get_num_words, get_num_times, sorted_list
import sys

def get_book_text(books):
    with open(books) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_times = get_num_times(book_text)
    sorted_char = sorted_list(num_times)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_char:
        if not char["char"].isalpha():
            continue
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

  
main()