sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

#! Using a simple method

# Iterating through the list `words` and appending the length of each
# word to the list `word_lengths` if the word is not "the".

word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
          
#! Using a list comprehension method

# A list comprehension that is iterating through the list `words` and 
# appending the length of each
# word to the list `word_lengths` if the word is not "the".

word_lengths = [len(word) for word in words if word != "the"]       
          
print(words)
print(word_lengths)