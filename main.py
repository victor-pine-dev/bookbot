import sys
from stats import get_words_count, get_characters_count, get_chars_report

def get_book_text(filepath):
    with open(file=filepath) as f:
        content = f.read()
        return content
    

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]

    print("============ BOOKBOT ============")
    content = get_book_text(path)
    print(f"Analyzing book found at {path}")

    print("----------- Word Count ----------")
    num_words = get_words_count(content)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    chars_count = get_characters_count(content)
    report = get_chars_report(chars_count)
    for item in report:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

main()