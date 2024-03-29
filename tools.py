import os
from random import randint

from question import Question


class ActivationCard:
    """
    A base class for all activation cards
    """

    def __init__(self):
        self.isUsed = False

    def useCard(self) -> bool:
        """
        If a card has not been activated, activate each cards ability.\n
        Else, inform the player the card has been activated.
        """
        if not self.isUsed:
            self.isUsed = True
            return True
        else:
            print("\n此求救卡已使用過\n")
            return False


class Change(ActivationCard):
    """
    Skips the current question without answering or penalty\n
    The `useCard()` method takes in the `change`, `remove`, and `second` objects
    """

    def __init__(self, question: Question):
        super().__init__()
        self.question = question

    def useCard(self, change, remove, second):
        if super().useCard():
            print("------------\n   換一題\n------------\n")
            return check(self.question, change, remove, second)
        else:
            return change, remove, second, None


class Remove(ActivationCard):
    """
    Removes one incorrect option\n
    The `useCard()` method takes a `question` argument
    """

    def useCard(self, question: Question):
        if super().useCard():
            print("\n刪去一個錯誤選項")
            # show one wrong option by convert correct answer to ASCII code and add a random int then convert back to chr
            wrongOption = chr(
                (ord(question.answer) + randint(0, 2)) % 4 + 65)

            print(f"{wrongOption}選項是錯的\n")


class Second(ActivationCard):
    """
    Offers a second answering chance if the answer is incorrect\n
    Needs to be activated before answering so could be a waste
    """

    def __init__(self):
        super().__init__()
        self.isActivated = False

    def useCard(self):
        if super().useCard():
            print("\n啟用第二次機會\n")
            # Once activated, a wrong answer can bypass the checking system at line 132
            self.isActivated = True


def check(question: Question, change: Change, remove: Remove, second: Second):
    question.printQuestion()

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

    return change, remove, second, isCorrect


# will add unix support in the future
def clear():
    os.system("cls")


def pause():
    os.system("pause")
