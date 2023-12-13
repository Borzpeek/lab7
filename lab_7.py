# task1
# def read_display_text_file(file_path):
#    with open(file_path, 'r') as file:
#          for line in file:
#             print(line, end='')
#
# file_path = r"C:\Users\nurzhan\Downloads\lab_7\lab_7.txt"
# read_display_text_file(file_path)

# task2
# import random
#
# def random_line_read(file_path):
#       with open(file_path, 'r') as file:
#          lines = file.readlines()
#          print(random.choice(lines).strip())
#
# file_path = r"C:\Users\nurzhan\Downloads\lab_7\lab_7.txt"
# random_line_read(file_path)

# task 3
# def number_uppercase_symbols(file_path):
#    with open(file_path, 'r') as file:
#       content = file.read()
#       uppercase_count = sum(1 for char in content if char.isupper())
#       print(uppercase_count)
#
# file_path = r"C:\Users\nurzhan\Downloads\lab_7\lab_7.txt"
# number_uppercase_symbols(file_path)

# task 4
# def lines_not_start_D(file_path):
#    with open(file_path, 'r') as file:
#       count = sum(1 for line in file if not line.strip().startswith('D'))
#       print(count)
#
# file_path = r"C:\Users\nurzhan\Downloads\lab_7\lab_7.txt"
# lines_not_start_D(file_path)

# task 5
# def words_end_F(file_path):
#       with open(file_path, 'r') as file:
#          words = file.read().split()
#          count = sum(1 for word in words if word.endswith(('F', 'f')))
#          print(count)
#
# file_path = r"C:\Users\nurzhan\Downloads\lab_7\lab_7.txt"
# words_end_F(file_path)

# task 6
# def count_all_none_words(file_path):
#    with open(file_path, 'r') as file:
#       content = file.read()
#       count_all = content.lower().split().count('all')
#       count_none = content.lower().split().count('none')
#       print(count_all)
#       print(count_none)
#
# file_path = r"C:\Users\nurzhan\Downloads\lab_7\all.none.txt"
# count_all_none_words(file_path)

# task 7
# def count_word_frequency(file_path):
#    with open(file_path, 'r') as file:
#       content = file.read().lower()
#       words = content.split()
#       word_frequency = {}
#
#       for word in words
#          word_frequency[word] = word_frequency.get(word, 0) + 1
#       for word, frequency in word_frequency.items():
#          print(f"{word}: {frequency}")
#
# file_path = r"C:\Users\nurzhan\Downloads\lab_7\lab_7.txt"
# count_word_frequency(file_path)

# task 8
# def longest_word(file_path):
#    with open(file_path, 'r') as file:
#       content = file.read().lower()
#       words = content.split()
#       long_word = max(words, key=len)
#
#       print(long_word)
#
# file_path = r"C:\Users\nurzhan\Downloads\lab_7\lab_7.txt"
# longest_word(file_path)

# task 9
# def replace_symb(file_path):
#    with open(file_path, 'r') as file:
#       content = file.read()
#       correct_cont = content.replace('B', 'J').replace('b', 'j')
#       print(correct_cont)
#
# file_path = r"C:\Users\nurzhan\Downloads\lab_7\lab_7.txt"
# replace_symb(file_path)

# task 10
# def count_a_b_occur(file_path):
#    with open(file_path, 'r') as file:
#       content = file.read().lower()
#       count_a = content.count('a')
#       count_b = content.count('b')
#       print(f"a={count_a}, b={count_b}")
#
# file_path = r"C:\Users\nurzhan\Downloads\lab_7\lab_7.txt"
# count_a_b_occur(file_path)