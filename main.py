import os
import time
from random import sample

from tools import ChangeQuestionCard, RemoveOptionCard, SecondChanceCard
from question import df, Question


def start():
    change = ChangeQuestionCard()
    remove = RemoveOptionCard()
    second = SecondChanceCard()
    questions_list = sample(range(0, len(df)), 11)

    # game starting sequence
    print("遊戲開始")
    print("輸入A、B、C、D作答，E、F、G啟用求救卡\nE:更換題目  F:刪去選項  G:第二條命\n你準備好了嗎?")
    time.sleep(1)
    for i in range(3):
        print(3 - i)
        time.sleep(2)

    for m in range(10):
        print("第{}題:\n".format(m + 1))

        change, remove, second, isCorrect = generate(
            change,
            remove,
            second,
            questions_list[m]
        )

        if m == 9:
            print("恭喜挑戰成功\n")
            return None
        elif isCorrect == False:
            print("\nGAME OVER\n")
            return None
        else:
            print("------------\n   下一題\n------------\n")


def generate(change: ChangeQuestionCard, remove: RemoveOptionCard, second: SecondChanceCard, index: int):
    question = Question(index)
    question.printQuestion()
    isCorrect, change, remove, second = check(question, change, remove, second)
    return change, remove, second, isCorrect


def check(question: Question, change, remove, second):
    while True:
        userInput = input("請選擇答案: ").strip().upper()
        isCorrect = False

        if len(userInput) == 1 and userInput[0] in "ABCDEFG":
            # change question
            if userInput[0] == "E":
                change, remove, second, isCorrect = change.useCard(
                    change, remove, second)
                if isCorrect is not None:
                    break

            # remove one option
            if userInput[0] == "F":
                remove.useCard(question)

            # second chance
            if userInput[0] == "G":
                second.useCard()

            # check answer
            if userInput in "ABCD":
                if userInput[0] == question.answer:
                    print("\n答案正確\n")
                    isCorrect = True
                    break
                elif second.isActivated == True:
                    print("\n答案錯誤，還有一次機會\n")
                    second.isActivated = False
                else:
                    print("\n答案錯誤\n")
                    print(f"正確答案應為:{question.answer}\n")
                    isCorrect = False
                    break

        else:
            print("\n資料錯誤，請重新輸入\n")

    return isCorrect, change, remove, second


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
