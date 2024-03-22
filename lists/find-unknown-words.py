def find_unknown_words(vocab, book_words):
    """
    Finds words in the book that are not in the vocabulary list.
    
    Args:
    vocab (list): The vocabulary list.
    book_words (list): The list of words in the book.
    
    Returns:
    list: A list of words in the book that are not in the vocabulary list.
    """
    unknown_words = []
    for word in book_words:  # O(n)
        if word not in vocab:  # O(n) in the worst-case
            unknown_words.append(word)  # O(1) average, O(n) worst-case
    return unknown_words

# Test cases
vocab = ["apple", "boy", "dog", "down", "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()

# Test if words in the book not in the vocabulary list are correctly identified
print("Unknown words:", find_unknown_words(vocab, book_words))  # Output should be: ['from', 'to']

# Test if all words are returned if vocabulary list is empty
print("Unknown words with empty vocabulary:", find_unknown_words([], book_words))  # Output should be the same as book_words

# Test if no unknown words are returned when all words in the book are in the vocabulary list
print("No unknown words:", find_unknown_words(vocab, ["the", "boy", "fell"]))  # Output should be an empty list

# Time Complexity: O(n^2)
# Space Complexity: O(m)
