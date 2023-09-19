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
            result = self.find_word(last_word)
            if not result == None:
                self.add_used_word(self.word_list[result] + "ますたー")
                return self.word_list[result] + "ますたー" , True
            else:
                return "その言葉は負けますたー", False
        elif True:
            return "その言葉はだめです" , True
    
    def find_word(self, first_word:str):
        indices = [index for index, word in enumerate(self.word_list) if word.startswith(first_word)]
        if indices:
            print(f"'{first_word}'で始まる要素のインデックス: {indices}")
            return indices[0]
        else:
            print(f"'{first_word}'で始まる要素は見つかりませんでした")
            return None
        
    def __init__(self):
        self.used_word_list = []
        self.word_list = [
            "アイヌ", "あいしてる",
            "異次元", "いろいろ",
            "餓えた", "うるさい",
            "英断", "えんぴつ",
            "おもしろい", "おかしい",
            "かわいい", "かわいそう",
            "きょどり" , "きょうりゅう",
            "くだらない", "くり食べる",
            "けちょんけちょん", "けんかする",
            ]
            
        