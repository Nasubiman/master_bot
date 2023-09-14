# discord.pyをインポート
import discord
from include import gobi, japantime, eagle , joke , siritori ,help

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



def contains_target(text , target):
    return target in text


# Botがメッセージを読み込んだ際のイベント設定
@client.event
async def on_message(message):
    global flag
    global siritori_flag
    global siritori
    obj = siritori.ClassName("hoge", "piyo")
    if not message.author.bot:
        print(obj.instance_method())
        if flag == False:
            if contains_target(message.content, '!start'):
                await message.channel.send('今から言葉の語尾にいちいち「ますたー」をつけてあげるよ！\n「!end」で終了するよ!')
                flag = True
            
            elif contains_target(message.content, '!end'):
                await message.channel.send('マスターモードは始まってないよ！')
            
        elif flag == True:
            if contains_target(message.content, '!start'):
                await message.channel.send('マスターモードはすでに始まってるよ！')
            
            elif contains_target(message.content, '!end'):
                await message.channel.send('マスターモードを終了するよ！')
                flag = False

            elif contains_target(message.content, '!help'):
                await message.channel.send(help.help())
            
            elif contains_target(message.content , "!siritori") or siritori_flag == True:
                result = siritori.siritori(message.content , siritori_flag)
                siritori_flag = result[1]
                await message.channel.send(result[0])
            
            elif (contains_target(message.content, '!joke')):
                await message.channel.send(joke.joke())
            
            elif (contains_target(message.content, '!eagle')):
                await message.channel.send(eagle.suppot())

            elif (contains_target(message.content, '!japantime')):
                await message.channel.send(japantime.japantime())
            
            elif (contains_target(message.content, '!bangladeshtime')):
                await message.channel.send(japantime.bangladeshtime())
            
            elif True:
                await message.channel.send(gobi.gobi(message.content))

    # 上記と同様に2個目の設定

# TOKENの値を読み込み、Botを起動させる
client.run(os.getenv('TOKEN'))