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
    temp_str = ""
    pointer_one, pointer_two = 0, 0
    temp_str = str[pointer_one]
    while pointer_one < len(str)-1:
        if pointer_one == pointer_two:
            if str[pointer_one].lower() in vowels:
                Kevin_vowels.append(temp_str)
            else:
                Stuart_consonants.append(temp_str)
            pointer_two += 1
        else:
            if pointer_two <= len(str) - 1:
                temp_str = temp_str + str[pointer_two]
                if str[pointer_one].lower() in vowels:
                    Kevin_vowels.append(temp_str)
                else:
                    Stuart_consonants.append(temp_str)
                pointer_two += 1
        if pointer_two > len(str) - 1:
            pointer_one += 1
            pointer_two = pointer_one
            temp_str = str[pointer_one]

    print(len(Kevin_vowels), len(Stuart_consonants))
    if len(Kevin_vowels) > len(Stuart_consonants):
        print('Kevin', len(Kevin_vowels))
    elif len(Stuart_consonants) > len(Kevin_vowels):
        print('Stuart', len(Stuart_consonants))
    else:
        print("Draw")

if __name__ == '__main__':
    # s = input()
    s = "NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANA"
    minion_game(s)