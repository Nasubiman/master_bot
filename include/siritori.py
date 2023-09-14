from include import siritori_library
def siritori(text , flag):
    if(not flag):
        return 'しりとりを始めるよ！ 終わりたかったら!owari と打ってね  まずは自分から\n しりとりますたー', True

    elif(text == '!owari'):
        return "しりとりを終了するよ！ またね！\n あなたのスコアは無しです", False
    
    elif True:
        return siritori_library.hoe(text[0] , text[-1]) , True