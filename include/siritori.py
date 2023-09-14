import siritori_library.siritori as siritori



def siritori(text , flag):
    if(not flag):
        return 'しりとりを始めるよ！ 終わりたかったら!owari と打ってね  まずは自分から\n しりとりますたー', True

    elif(text == '!owari'):
        return "しりとりを終了するよ！ またね！\n あなたのスコアは無しです", False
    elif True:
        return "hoge", True