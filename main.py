import sys

from stats import (
  get_num_words,
  get_chars_dict,
  chars_dict_to_sorted_list,
)

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  path = sys.argv[1]
  text = get_book_text(path)
  words = get_num_words(text)
  chars_dict = get_chars_dict(text)
  chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
  print_report(path,words,chars_sorted_list)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def print_report(path,words,chars_sorted_list):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}...")
  print("----------- Word Count ----------")
  print(f"Found {words} total words")
  print("--------- Character Count -------")
  for c in chars_sorted_list:
    if c["char"].isalpha():
      print(f"{c['char']}: {c['num']}")
  print("============= END ===============")



main()