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
        \tindex: The index of the question from the data\n
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

    def useCard(self):
        """
        If a card has not been activated, activate each cards ability.\n
        Else, inform the player the card has been activated.
        """
        if self.isUsed is False:
            self.isUsed = True
            self._activate()
        else:
            print("\n此求救卡已使用過\n")


class ChangeQuestionCard(ActivationCard):
    """
    Skips the current question without answering or penalty
    """

    def __init__(self):
        super().__init__()

    def useCard(self):
        super().useCard()
        print("test")


class RemoveOptionCard(ActivationCard):
    """
    Removes one incorrect option `useCard()` method takes a `question` arguement
    """

    def useCard(self, question):
        super().useCard()

        # show one wrong option by convert correct answer to ASCII code and add a random int then convert back to chr
        wrongOption = chr(
            (ord(question.answer) + randint(0, 2)) % 4 + 65)

        print(f"\n{wrongOption}選項是錯的\n")


class SecondChanceCard(ActivationCard):
    """
    Offers a second answering chance if the answer is incorrect\n
    *Needs to be activated before answering so could be a waste
    """

    def __init__(self):
        super().__init__()
        self.isActivated = False

    def useCard(self):
        super().useCard()
        self.isActivated = True


def check(question: Question, c: ChangeQuestionCard, r: RemoveOptionCard, s: SecondChanceCard):
    while True:
        answer = input("請選擇答案:").strip().upper()
        isCorrect = False

        if len(answer) == 1 and answer[0] in "ABCDEFG":
            # change question
            if answer[0] == "E":
                print("------------\n   換一題\n------------\n")
                e = True
                c, r, s, isCorrect = generate(c, r, s)
                break

            # remove one option
            if answer[0] == "F":
                r.useCard(question)

            # second chance
            if answer[0] == "G":
                s.useCard()

            # check answer
            if answer[0] == question.answer:
                print("\n答案正確\n")
                isCorrect = True
                break
            elif s.isActivated == True:
                print("\n答案錯誤，還有一次機會\n")
                s.isActivated = False
            else:
                print("\n答案錯誤\n")
                print(f"正確答案應為:{question.answer}\n")
                isCorrect = False
                break

        else:
            print("\n資料錯誤，請重新輸入\n")

    return isCorrect, c, r, s


def generate(e: ChangeQuestionCard, f: RemoveOptionCard, g: SecondChanceCard):
    index = randint(0, len(df))
    question = Question(index)
    question.printQuestion()
    isCorrect, e, f, g = check(question, e, f, g)
    return e, f, g, isCorrect


def start():
    c = ChangeQuestionCard()
    r = RemoveOptionCard()
    s = SecondChanceCard()
    existedQuestions = []

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

        c, r, s, b = generate(c, r, s)

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
