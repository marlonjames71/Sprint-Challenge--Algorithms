'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    return count_assist(word, 0)

def count_assist(word, occurences):
    if word == "":
        return occurences
    elif word.startsWith("th"):
        return count_assist(word[:2], occurences + 1)
    else:
        return count_assist(word[1:], occurences)