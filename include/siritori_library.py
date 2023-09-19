class SiritoriLibrary:
    def add_used_word(self,word:str):
        self.used_word_list.append(word)

    def show_used_word(self):
        words = ", ".join(self.used_word_list)
        return words

    def check_first_word(self, word:str):
        if (word[0] in { "た", "タ"}):
            return True
        else:
            return False
    
    def check_last_word(self, word:str):
        if (not word[-1] in { "ん", "ン"}):
            return True
        else:
            return False

    def return_word(self, text:str):
        if(self.check_first_word(text) and self.check_last_word(text) and not text in self.used_word_list):
            print(text + "is last word")
            self.add_used_word(text)
            last_word : str = text[-1]

            return text + "ますたー"
        elif True:
            return "その言葉はだめです"
    
    def __find_word__(self, word:str):
        if word in self.word_list:
            return True
        else:
            return False
        
    def __init__(self):
        self.used_word_list = []
        self.word_list = [
            "アイヌ",
            "異次元",
            "餓えた",
            "英断",
            "おもしろい",
            "かわいい",
            "きょどり"
            ]
            
        