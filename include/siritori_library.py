class SiritoriLibrary:

    def add_used_word(self,word):
        self.used_word_list.append(word)

    def show_used_word(self):
        words = ", ".join(self.used_word_list)
        return words

    def check_first_word(self, word):
        if (word[0] in { "た", "タ"}):
            return True
        else:
            return False
    
    def check_last_word(self, word):
        if (not word[-1] in { "ん", "ン"}):
            return True
        else:
            return False

    def return_word(self, text):
        if(self.check_first_word(text) and self.check_last_word(text) and not text in self.used_word_list):
            print(text + "is last word")
            self.add_used_word(text)
            return text + "ますたー"
        elif True:
            return "その言葉はだめです"
        
    def __init__(self):
        self.used_word_list = []
        self.word_list = ["アイヌ", "異次元", "餓えた", "英断", "落ちぶれた", "蚊取り線香"]
            
        