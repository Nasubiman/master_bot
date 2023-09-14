from include import siritori_library
def siritori(text , flag):
    if(not flag):
        siritori_library.add_used_word(text)
        return 'しりとりを始めるよ！ 終わりたかったら!owari と打ってね  まずは自分から\n しりとりますたー', True

    elif(text == '!owari'):
        return "しりとりを終了するよ！ またね！\n あなたのスコアは無しです", False
    
    elif(text == "!showlist"):
        return siritori_library.show_used_word, True
    
    elif True:
        return siritori_library.return_word(text) , True