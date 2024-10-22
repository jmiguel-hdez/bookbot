def get_char_count(text):
    char_counts = {}
    for c in text.lower():
        char_counts[c] = char_counts.get(c,0) + 1
    return char_counts

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_num = get_word_count(text)
    print(f"words found in book {words_num}")
    print(get_char_count(text))

main()