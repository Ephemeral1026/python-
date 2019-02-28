 #Word Jumble 猜单词游戏
import random
#创建单词序列
WORD=("python","jumble","easy","difficult","answer","continue","phone","position","game") #从序列中随机挑出一个单词
#start the game
print(
"""
    欢迎参加猜单词游戏
    把字母组合成一个正确的单词
"""
)
iscontinue="y"
while iscontinue=="y" or iscontinue=="Y":
    #从序列中随机挑出一个单词
    word=random.choice(WORD)
    #一个用于判断玩家是否猜对的变量
    correct=word
    #创建乱序后的单词
    jumble=""
    while word: #word不是空串时的循环
        #根据word的长度，产生word的随机位置
        position=random.randrange(len(word))
        #将position位置字母组合到混乱后单词
        jumble+=word[position]
        #通过切片，将position位置字母从原单词中删除
        word=word[:position]+word[(position+1):]
    print("乱序后单词:",jumble)
    guess = input("\n请你猜:")
    while guess != correct and guess != "":
        print("对不起不正确.")
        guess = input("继续猜:")
    if guess == correct:
        print("真棒，你猜对了!\n")
iscontinue = input("\n\n是否继续(Y/N):")
