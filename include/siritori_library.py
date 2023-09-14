class SiritoriLibrary:

    def __init__(self):
        self.used_word_list = []
        self.word_list = ["apple", "elephant", "tiger", "rabbit", "cat", "dog"]
        self.current_word = None

    def add_used_word(self,word):
        self.used_word_list.append(word)

    def show_used_word(self):
        words = ", ".join(self.word_list)
        return words

    def check_first_word(self, word):
        if (word[0] in { "た", "タ"}):
            return True
        else:
            return False

    def return_word(self, text):
        if(self.check_first_word(text) and not text in self.used_word_list):
            print(text + "is last word")
            self.add_used_word(text)
            return text + "するますたー"
        elif True:
            return "this is not good"
            
        