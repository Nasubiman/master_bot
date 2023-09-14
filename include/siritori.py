def greet():
    print("Hello from language.py")

class ClassName:
    # クラス変数（クラス全体で共有される変数）
    class_variable = "This is a class variable"

    # イニシャライザ（クラスのインスタンスを初期化するメソッド）
    def __init__(self, param1, param2):
        # インスタンス変数（各インスタンスに固有の変数）
        self.param1 = param1
        self.param2 = param2

    # インスタンスメソッド（インスタンスに対して操作を行うメソッド）
    def instance_method(self):
        return f"This is an instance method with param1={self.param1} and param2={self.param2}"

    # クラスメソッド（クラス全体に対して操作を行うメソッド）
    @classmethod
    def class_method(cls):
        return f"This is a class method with class_variable={cls.class_variable}"

    # スタティックメソッド（特定のクラスまたはインスタンスに依存しないメソッド）
    @staticmethod
    def static_method():
        return "This is a static method"

# クラスのインスタンスを作成
obj = ClassName("Value1", "Value2")

# インスタンスメソッドを呼び出し
result1 = obj.instance_method()
print(result1)

# クラスメソッドを呼び出し
result2 = ClassName.class_method()
print(result2)

# スタティックメソッドを呼び出し
result3 = ClassName.static_method()
print(result3)

word_list = ["apple", "elephant", "tiger", "rabbit", "cat", "dog"]

current_word = None
player_score = 0

def siritori(text , flag):
    if(not flag):
        return 'しりとりを始めるよ！ 終わりたかったら!owari と打ってね  まずは自分から\n しりとりますたー', True

    elif(text == '!owari'):
        return "しりとりを終了するよ！ またね！\n あなたのスコアは" + str(player_score) + "です", False
    elif True:
        return "hoge", True