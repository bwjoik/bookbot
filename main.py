from stats import get_num_words, get_each_character_count, get_sorted_character_list
import sys

def get_book_text(path):
    # Simulate getting book text
    with open(path, 'r') as file:
        text = file.read()
    return text


def main(get_book_text, path):
    # Simulate the main function
    book_text = get_book_text(path)
    count_words_result = get_num_words(book_text)
    count_characters_result = get_each_character_count(book_text)
    sorted_characters = get_sorted_character_list(count_characters_result)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words_result} total words")
    print("---------- Character Count -------")
    for entry in sorted_characters:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Use the second argument as the path to the book file
    path = sys.argv[1]

    # Call the main function with the get_book_text function and path
    main(get_book_text, path)