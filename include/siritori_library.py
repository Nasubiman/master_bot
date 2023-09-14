used_word_list = []

word_list = ["apple", "elephant", "tiger", "rabbit", "cat", "dog"]

current_word = None

def add_used_word(word):
    used_word_list.append(word)

def show_used_word():
    print(used_word_list)
    return used_word_list

def check_first_word(word):
    if(word[0] == "た" or word[0] == "タ"):
        return True
    else:
        return False

def return_word(text):
    if(check_first_word(text)):
        print(text + "is last word")
        add_used_word(text)
        return text + "するますたー"
    elif True:
        return "this is not good"
        
    