def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            ++score ## just change this to score = 1
    return score


n = int(input())
words = input().split()
print(score_words(words))

better approach :
def has_vowel(letters):
    v_sum =sum([['a', 'e', 'i', 'o', 'u', 'y'].count(l) for l in letters]) 
    return  2 if  v_sum %2 == 0 else 1
    
def score_words(words):
    return sum([has_vowel(w) for w in [[*map(str,word)] for word in words]])


n = int(input())
words = input().split()
print(score_words(words))
