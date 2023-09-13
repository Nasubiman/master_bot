import pytz
from datetime import datetime

jst = pytz.timezone('Asia/Tokyo')
bst = pytz.timezone('Asia/Dhaka')

def japantime():
    current_time_jst = datetime.now(jst)
    return current_time_jst.strftime('日本は今%Y年%m月%d日 %H時%M分%S秒') + "です。"

def bangladeshtime():
    current_time_bst = datetime.now(bst)
    return current_time_bst.strftime('バングラデシュは今%Y年%m月%d日 %H時%M分%S秒') + "です。"
