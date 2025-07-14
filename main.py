import sys
from stats import get_num_words , get_num_char, list_dict
def get_book_text (file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main ():
   if len(sys.argv) == 2:
      text = get_book_text(sys.argv[1])    
      word_count = get_num_words(text)
      char_count = get_num_char(text)
      print("============ BOOKBOT ============")
      print(f"Analyzing book found at {sys.argv[1]} ...")
      print("----------- Word Count ----------")
      print(f"Found {word_count} total words")
      print("--------- Character Count -------")
      sorted_chars = list_dict(char_count)
      for char_dict in sorted_chars:
          if char_dict["char"].isalpha():
             print(f"{char_dict["char"]}: {char_dict["num"]}")
      print("============= END ===============")
   else:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)       
main()


