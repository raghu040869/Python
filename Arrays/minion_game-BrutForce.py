# Game Rules
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
# s = BANANA
def minion_game(str):
    # your code goes here
    vowels = ['a','e','i','o','u']
    Kevin_vowels = []
    Stuart_consonants = []
    for i, c in enumerate(str):
        temp_str = c
        if c.lower() in vowels:
            Kevin_vowels.append(temp_str)
        else:
            Stuart_consonants.append(temp_str)
        for j in range(i+1, len(str)):
            temp_str += str[j]
            if c.lower() in vowels:
                    Kevin_vowels.append(temp_str)
            else:
                    Stuart_consonants.append(temp_str)

    if len(Kevin_vowels) > len(Stuart_consonants):
        print(('Kevin', len(Kevin_vowels)))
    else:
        print(('Stuart', len(Stuart_consonants)))




if __name__ == '__main__':
    s = input()
    minion_game(s)