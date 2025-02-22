from stats import get_num_words, get_num_chars
import sys

def get_book_text(file:str) -> str:
    with open(file, "r") as f:
        return f.read()

def sort_dict(d:dict[str, int]) -> list[dict[str, int]]:
    result = [{"letter": char, "count": count} for char, count in d.items()]
    return sorted(result, key=lambda x: x["count"], reverse=True)

def format_report(book_path:str, num_words:int, num_chars:dict[str, int]):
    num_sorted = sort_dict(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing bokk found at {book_path}...")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print("--------- Character Count -------")
    for dict in num_sorted:
        char = dict["letter"]
        count = dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_tom_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    num_words = get_num_words(book)
    num_chars = get_num_chars(book)

    format_report(path, num_words, num_chars)

if __name__ == "__main__":
    main()
