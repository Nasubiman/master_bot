import requests
from bs4 import BeautifulSoup
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
        if(self.check_first_word(text) and self.check_last_word(text) and not text in self.used_word_list) and self.word_exists(text):
            print(text + "is last word")
            self.add_used_word(text)
            last_word : str = text[-1]
            result = self.find_word(last_word)
            if not result == None:
                self.add_used_word(self.word_list[result] + "ますたー")
                list_text = self.word_list[result]
                self.word_list.pop(result)
                return list_text + "ますたー" , True
            else:
                return "負けますたー", False
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
    
    def word_exists(self, word:str):
        url = f"https://sakura-paris.org/dict/%E5%BA%83%E8%BE%9E%E8%8B%91/prefix/{word}" 

        response = requests.get(url)

        # HTTPステータスコードが200（成功）であれば、ページ内容を解析
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # 検索結果が存在しないことを示す特定のテキストを検索
            not_found_text = "検索結果は見つかりません"
            if not_found_text in soup.get_text():
                print(f"みつからないよぉで始まる要素は見つかりませんでした")
                return False  # 検索結果が存在しない場合
            else:
                print(f"見つかったよぉで始まる要素は見つかりませんでした")
                return True   # 単語が存在する場合
        else:
            print(f"やっぱ見つからないよぉで始まる要素は見つかりませんでした")
            return False  # HTTPステータスコードが200以外の場合も単語が存在しないとみなします
    
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
            "こうもり", "こうもく",
            ]
            
        