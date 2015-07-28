# YgPay Atinlay Anslatortay
pyg = 'ay'

# Get the word
original = raw_input('Enter a word:')

# Shuffle word
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word
    new_word = new_word[1:len(new_word)] + first + pyg
    # Print result
    print new_word
else:
    print 'empty'
