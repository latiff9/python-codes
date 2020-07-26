word = 'omadamo'


def palindrom(word):
    n = len(word)
    stillTrue = True
    for i in range(int(n/2)):
        print(word[i], word[n-1-i])
        if word[i] != word[n-1-i]:
            stillTrue = False
    return stillTrue


print(palindrom(word))
