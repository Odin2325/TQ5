sentence = 'Ein toller Satz mit einigen interessanten Feinheiten!!!!!'
#sentence = 'Dieser Satz kein Verb'
letter_count = 0
longest_word = ''

word_list = sentence.split(' ')

for i in range(0, len(word_list)):
    word = word_list[i].strip(',."!')
    if len(word) > letter_count:
        letter_count = len(word)
        longest_word = word

print(longest_word)
