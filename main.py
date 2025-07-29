import sys
from stats import number_of_words, character_count, character_sort

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    try:
        book_text = get_book_text(path)
    except FileNotFoundError:
        print(f'Error: File not found at path: {path}')
        sys.exit[1]

    number = number_of_words(book_text)
    count_result = character_count(book_text)
    sorted_characters = character_sort(count_result)
    
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {path}...')
    print("----------- Word Count ----------")
    print(f'Found {number} total words')
    print("--------- Character Count -------")
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()