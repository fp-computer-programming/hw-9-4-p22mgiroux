# Author: MOG 1/18/22

words = ["word", "dog", "piano", "red", "sweatshirt","running", "reviewing"]

def smash(lst):
    sent = ""
    for word in lst:
        if word != lst[len(lst) - 1]:
            sent += word + " "
        else:
            sent += word + "."
    print(sent)

smash(words)