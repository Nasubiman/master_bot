from include import siritori_library

siritori_lib = siritori_library.SiritoriLibrary()
def siritori(text , flag):
    global siritori_lib
    if(not flag):
        siritori_lib = siritori_library.SiritoriLibrary()
        siritori_lib.add_used_word(text)
        return 'しりとりを始めるよ！ 終わりたかったら!owari と打ってね  まずは自分から\n しりとりますたー', True

    elif(text == '!owari'):
        return "しりとりを終了するよ！ またね！\n あなたのスコアは無しです", False
    
    elif(text == "!showlist"):
        return siritori_lib.show_used_word(), True
    
    elif True:
        return siritori_lib.return_word(text) , True