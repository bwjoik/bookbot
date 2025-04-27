def get_num_words(text):
    """
    Count the number of words in a given text.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    # Split the text into words and return the count
    words = text.split()
    return len(words)
    
def get_each_character_count(text):
    """
    Returns a dictionary with the count of each character in the text.
    Characters are converted to lowercase to avoid duplicates.
    """
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_list(get_num_words, get_each_character_count):
    """
    Returns a sorted list of tuples containing the character and its count.
    """
    # Get the character count dictionary
    char_count = get_each_character_count()
    
    # Sort the dictionary by character
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[0])
    
    return sorted_char_count

def get_sorted_character_list(char_count):
    """
    Returns a sorted list of dictionaries containing characters and their counts.
    The list is sorted from greatest to least by the count.
    Non-alphabetical characters are skipped.

    Args:
        char_count (dict): A dictionary with characters as keys and their counts as values.

    Returns:
        list: A sorted list of dictionaries with "char" and "num" keys.
    """
    sorted_list = []
    for char, count in char_count.items():
        if char.isalpha():  # Skip non-alphabetical characters
            sorted_list.append({"char": char, "num": count})
            
    # Sort the list from greatest to least by count
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
    
if __name__ == "__main__":
    # Example usage
    text = "This is a sample text with several words."
    print(f"Number of words: {get_num_words(text)}")
