import sys
from stats import get_num_words
from stats import get_book_text
from stats import count_book_char
from stats import pair_char_and_count
from stats import get_num

       
def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        raise sys.exit(1)
    else:
         num_words = get_num_words(sys.argv[1])
         #print(f"Found {num_words} total words")
         file_contents = get_book_text(sys.argv[1])
         #print(file_contents)
         char_count_dict = count_book_char(file_contents)
         #print(char_count_dict)
         list_of_char_num_dicts = pair_char_and_count(char_count_dict)
         #print(list_of_char_num_dicts)

         list_of_char_num_dicts.sort(reverse=True, key=get_num)
         print("============ BOOKBOT ============")
         print(f"Analyzing book found at {sys.argv[1]}...")
         print("----------- Word Count ----------")
         print(f"Found {num_words} total words")
         print("--------- Character Count -------")
         #print(list_of_char_num_dicts)
         for item in list_of_char_num_dicts:
             if not item["char"].isalpha():
                continue
             print(f"{item['char']}: {item['num']}")
    
main()