def gobi(text):
    if text.endswith('ま'):
        return text + 'すたー'
    elif text.endswith( 'ます'):
        return text + 'たー'
    elif text.endswith( 'ますた'):
        return text + 'ー'
    elif text.endswith('ますたー'):
        return text + 'ーーーーーー!!!!!!!!!!!!!!!'
    else:
        return text + 'ますたー'