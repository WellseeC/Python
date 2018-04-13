def is_alternating(word):
    word1 = word.lower()
    i = 0
    u = 1
    o = 1
    if len(word1)>=8:#To check the length of words
        while i+1<len(word1) and u+1<len(word1) and o+2<len(word1):#Giving limit to while loop to let str stay in range
            if word1[i] in 'aeiou':#To check if vowels are in correct position
                i+=2
                if word1[u] not in 'aeiou':#To check if consanants are in correct position
                    u+=2
                    if word1[o]<word1[o+2]:
                        o+=2
                    else:
                        return False
                else:
                    return False
            else:
                return False
    else:
        return False




word = input('Enter a word => ')
print(word)
is_alternating(word)#Call the function
if is_alternating(word) is False:#Using the result of function to check the word is alternating or not
    print('The word','\''+word+'\'','is not alternating')
else:
    print('The word','\''+word+'\'','is alternating')