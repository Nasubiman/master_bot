import random

def joke():
    random_integer = random.randint(1, 7)

    if random_integer == 1:
        return "「(gitに)上げません 動くまでは」"
    elif random_integer == 2:
        return "「ファームウェア1億総玉砕」"
    elif random_integer == 3:
        return "「京繊人なら贅沢(テスト勉強)はできないはずだ」"
    elif random_integer == 4:
        return "マスターは嘘をつかない。その口から発せられる言葉は、すべて真実となるからだ。"
    elif random_integer == 5:
        return "安全ヒモを解除した状態でステアを動かしたマスターは、暴走した機体を止めるために自らの指をステアに捧げた。"
    elif random_integer == 6:
        return "この世界の創造主であるマスターは、自分自身が物理法則の根拠となる。\n物理学実験の課題の期限が迫っている中、マスターは表紙に自分の名前を書いただけのレポートを提出した。"
    elif random_integer == 7:
        return "この電波\n防ぐと君が\n言ったから\n3月8日は\nアルミ記念日\n\n            「アルミ記念日」"