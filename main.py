# discord.pyをインポート
import discord
import siritori
import joke

# .envファイルからTOKENの値を読み込み
import os
from dotenv import load_dotenv
load_dotenv()

# 初期化
client = discord.Client(intents=discord.Intents.all())


flag = False
siritori_flag = False
# Botが正常に起動した際のイベント設定
@client.event
async def on_ready():
    print('Startup Success!!!')


def ends_with_target(text , target):
    return text.endswith(target)

def contains_target(text , target):
    return target in text


# Botがメッセージを読み込んだ際のイベント設定
@client.event
async def on_message(message):
    global flag
    global siritori_flag
    global siritori
    obj = siritori.ClassName("hoge", "piyo")
    # Botが出力したメッセージじゃ無い場合（この条件でBotのメッセージを弾く）
    if not message.author.bot:
        print(obj.instance_method())
        if contains_target(message.content, '!start'):
            if flag == False:
                await message.channel.send('今から言葉の語尾にいちいち「ますたー」をつけてあげるよ！\n「!end」で終了するよ!')
                flag = True
            else:
                await message.channel.send('マスターモードはすでに始まってるよ！')

        elif contains_target(message.content, '!end'):
            if flag == True:
                await message.channel.send('マスターモードを終了するよ！')
                flag = False
            else:
                await message.channel.send('マスターモードは始まってないよ！')

        elif contains_target(message.content, '!help'):
            await message.channel.send('helpなんて存在しない、そんなものマスターにきけばいいと思うよ!')
        
        elif siritori_flag == True:
            if ends_with_target(message.content, '!end'):
                await message.channel.send('helpなんて存在しない、そんなものマスターにきけばいいと思うよ!')

        elif (contains_target(message.content, '!しりとり') or contains_target(message.content , "!siritori")) and flag == True:
            await message.channel.send('しりとりを始めるよ！まずは自分から\n しりとりますたー')
            siritori_flag = True
        
        elif (contains_target(message.content, '!joke')) and flag == True:
            await message.channel.send(joke.joke())
        
        elif flag == True:
            if ends_with_target(message.content, 'ま'):
                await message.channel.send(message.content + 'すたー')
            elif ends_with_target(message.content , 'ます'):
                await message.channel.send(message.content + 'たー')
            elif ends_with_target(message.content , 'ますた'):
                await message.channel.send(message.content + 'ー')
            elif ends_with_target(message.content , 'ますたー'):
                await message.channel.send(message.content + 'ーーーーーー!!!!!!!!!!!!!!!')
            else:
                await message.channel.send(message.content + 'ますたー')

    # 上記と同様に2個目の設定

# TOKENの値を読み込み、Botを起動させる
client.run(os.getenv('TOKEN'))