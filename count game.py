
import random
import os
number = random.randint(1,100)
count = 0
print('猜数字游戏：猜一个0~100之间的数')
while True:
    #进入猜数字环节 while循环
    guess = int(input('请输入您要猜的数字：'))
    count = count + 1
    if guess == number:
        print('恭喜你猜对了')
        break
    elif guess > number:
         print('猜大了')
    else :
        print('猜小了')
print('你一共猜了%d'% count,'次')
os.system("pause")
