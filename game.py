from random import randint
import pandas as pd
import os
import time

# os.system("color f0")
path = os.path.abspath("questions.csv")
df = pd.read_csv(path)


class Question:
    """
    The Question class takes 1 arguement and contains 6 attributes\n

    Arguement:\n
        \tindex: An int specifying the index of the question from the data\n
    Attributes:\n
        \tquestion: The question itself
        \tA: Option A
        \tB: Option B
        \tC: Option C
        \tD: Option D
        \tanswer: The answer to the question
    """

    def __init__(self, index: int):
        self.question: str = df["題目"][index]
        self.A: str = df["A選項"][index]
        self.B: str = df["B選項"][index]
        self.C: str = df["C選項"][index]
        self.D: str = df["D選項"][index]
        self.answer: str = df["答案"][index]

    def printQuestion(self):
        print(self.question)
        print(f"A:{self.A} B:{self.B} C:{self.C} D:{self.D}")


class ActivationCard:
    """
    A base class for all activation cards
    """

    def __init__(self):
        self.isUsed = False

    def useCard(self, question: Question):
        """
        If a card has not been activated call each cards _activate() method.\n
        Else, inform the player the card has been activated.
        """
        if self.isUsed is False:
            self.isUsed = True
            self._activate(question)
        else:
            print("\n此求救卡已使用過\n")


class ChangeQuestionCard(ActivationCard):
    """
    Skips the current question without answering or penalty
    """

    def __init__(self):
        super().__init__()

    def _activate(self):
        print("test")


class SecondChanceCard(ActivationCard):
    """
    Offers a second answering chance if the answer is incorrect\n
    *Needs to be activated before answering so could be a waste
    """

    def __init__(self):
        super().__init__()
        self.activated = False

    def _activate(self):
        pass


class RemoveOptionCard(ActivationCard):
    def __init__(self):
        super().__init__()

    def _activate(self, question: Question):
        # show one wrong option by convert correct answer to ASCII code and add a random num then convert back to chr
        wrongOption = chr(
            (ord(question.answer) + randint(0, 2)) % 4 + 65)

        print(f"\n{wrongOption}選項是錯的\n")


def check(question: Question, e, f: RemoveOptionCard, g):
    activate = False
    while True:
        answer = input("請選擇答案:").upper()
        b = False

        if len(answer) == 1 and answer[0] in "ABCDEFG":
            # change question
            if answer[0] == "E" and e == False:
                print("------------\n   換一題\n------------\n")
                e = True
                e, f, g, b = generate(e, f, g)
                break
            elif answer[0] == "E" and e == True:
                print("\n此求救卡已使用過\n")

            # delete one option
            if answer[0] == "F":
                f.useCard(question)

            # second chance
            if answer[0] == "G" and g == False:
                print("\n啟用第二次機會\n")
                g = True
                activate = True
            elif answer[0] == "G" and g == True:
                print("\n此求救卡已使用過\n")

            # check answer
            if answer[0] == question.answer:
                print("\n答案正確\n")
                b = True
                break
            elif answer[0] != question.answer and activate == True:
                print("\n答案錯誤，還有一次機會\n")
                activate = False
            else:
                print("\n答案錯誤\n")
                print(f"正確答案應為:{question.answer}\n")
                b = False
                break

        else:
            print("\n資料錯誤，請重新輸入\n")

    return b, e, f, g


def generate(e: ChangeQuestionCard, f: RemoveOptionCard, g: SecondChanceCard):
    i = randint(0, len(df))
    question = Question(i)
    question.printQuestion()
    b, e, f, g = check(question, e, f, g)
    if b == False:
        return e, f, g, False
    return e, f, g, True


def start():
    changeQuestionCard = ChangeQuestionCard()
    removeOptionCard = RemoveOptionCard()
    secondChanceCard = SecondChanceCard()

    # game starting sequence
    # TODO: add this back
    # print("遊戲開始")
    # print("輸入A、B、C、D作答，E、F、G啟用求救卡\nE:更換題目  F:刪去選項  G:第二條命\n你準備好了嗎?")
    # time.sleep(1)
    # for i in range(4):
    #     print(3 - i)
    #     time.sleep(2)

    for m in range(10):
        print("第{}題:\n".format(m + 1))

        e_used, f_used, g_used, b = generate(
            changeQuestionCard, removeOptionCard, secondChanceCard)

        if m == 9:
            print("恭喜挑戰成功\n")
            return None
        elif b == False:
            print("\nGAME OVER\n")
            return None
        else:
            print("------------\n   下一題\n------------\n")


while True:
    start()

    i = input("\n是否要再來一局?(y/n)").lower()
    if i == "n":
        os.system("pause")
        exit(0)
    elif i == "y":
        os.system("cls")
        break
    else:
        print("資料錯誤，請重新輸入\n")
