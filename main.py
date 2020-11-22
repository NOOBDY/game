import os
import time
from random import sample

from tools import Change, Remove, Second, check
from question import df, Question


def start():
    questions_list = sample(range(0, len(df)), 11)
    change = Change(Question(questions_list[-1]))
    remove = Remove()
    second = Second()

    print(questions_list)

    # game starting sequence
    print("遊戲開始")
    print("輸入A、B、C、D作答，E、F、G啟用求救卡\nE:更換題目  F:刪去選項  G:第二條命\n你準備好了嗎?")
    time.sleep(1)
    for i in range(3):
        print(3 - i)
        time.sleep(2)

    for m in range(10):
        print("第{}題:\n".format(m + 1))

        change, remove, second, isCorrect = check(
            Question(questions_list[m]),
            change,
            remove,
            second
        )

        if m == 9:
            print("恭喜挑戰成功\n")
            return None
        elif isCorrect == False:
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
