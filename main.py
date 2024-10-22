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

def print_report(num_words, char_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for c in char_dict:
        print(f"The {c} character was found {char_dict[c]} times")
    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_num = get_word_count(text)
    char_dict = get_char_count(text)
    print_report(words_num, char_dict)

main()