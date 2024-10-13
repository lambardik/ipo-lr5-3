def count_words_in_file(filename):

  with open(filename, 'r') as file:
    text = file.read()
    words = text.split()
    return len(words)

filename = 'text.txt'
word_count = count_words_in_file(filename)
print(f"В файле '{filename}' {word_count} слов.")
