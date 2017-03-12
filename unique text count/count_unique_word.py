def unique_word():
    lst = []
    signs = [',', '.', '!', '?', '(',')','[',']']
    with open('default_text.txt') as f:
        for line in f:
            for word in line.split():
                if word.isalpha():
                    if word not in lst:
                        lst.append(word)
                elif word[-1:] in signs and word[0] in signs:
                    if len(word) >3:
                        lst.append(word[1:-1])
                    else:
                        continue
                elif word[-1:] in signs:
                    if word[:-1] not in lst:
                        lst.append(word[:-1])
                elif word[0] in signs:
                    if word[1:] not in lst:
                        lst.append(word[1:])
                else: continue
    print(sorted(lst))
    print('Unique words count: %s' % len(lst))

unique_word()