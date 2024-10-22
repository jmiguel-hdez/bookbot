def get_char_count(text):
    char_counts = {}
    for c in text.lower():
        if c.isalpha():
            char_counts[c] = char_counts.get(c,0) + 1
    return char_counts

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def convert_to_list(dict):
    new_list = []
    for k in dict:
        new_list.append({"name":k, "num":dict[k]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def print_report(num_words, lst):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for d in lst:
        print(f"The '{d['name']}' character was found {d['num']} times")
    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_num = get_word_count(text)
    char_dict = get_char_count(text)
    dict_list = convert_to_list(char_dict)
    print_report(words_num, dict_list)

main()