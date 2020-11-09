import os
import time
from random import randint

from tools import (ChangeQuestionCard, RemoveOptionCard, SecondChanceCard,
                   generate)


def start():
    change = ChangeQuestionCard()
    remove = RemoveOptionCard()
    second = SecondChanceCard()
    existedQuestions = []

    # game starting sequence
    print("遊戲開始")
    print("輸入A、B、C、D作答，E、F、G啟用求救卡\nE:更換題目  F:刪去選項  G:第二條命\n你準備好了嗎?")
    time.sleep(1)
    for i in range(2):
        print(3 - i)
        time.sleep(2)

    for m in range(10):
        print("第{}題:\n".format(m + 1))

        isCorrect, change, remove, second = generate(change, remove, second)

        if m == 9 and isCorrect:
            print("恭喜挑戰成功\n")
            return None
        elif not isCorrect:
            print("\nGAME OVER\n")
            return None
        else:
            print("------------\n   下一題\n------------\n")


while True:
    start()

    while True:
        i = input("\n是否要再來一局?(y/n)").lower()
        if i == "n":
            os.system("pause")
            exit(0)
        elif i == "y":
            os.system("cls")
            break
        else:
            print("資料錯誤，請重新輸入\n")
