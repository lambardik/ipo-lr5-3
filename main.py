filename = 'text.txt'
with open(filename, 'r') as file:
  text = file.read()
  words = text.split()
  word_count = len(words)
print(f"В файле '{filename}' {word_count} слов.")
