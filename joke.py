import random

def joke():
    random_integer = random.randint(1, 3)

    if random_integer == 1:
        return "「(gitに)上げません 動くまでは」"
    elif random_integer == 2:
        return "「ファームウェア1億総玉砕」"
    elif random_integer == 3:
        return "「京繊人なら贅沢(テスト勉強)はできないはずだ」"