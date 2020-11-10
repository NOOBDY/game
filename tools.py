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


class ChangeQuestionCard(ActivationCard):
    """
    Skips the current question without answering or penalty
    """

    def useCard(self, change, remove, second):
        if super().useCard():
            print("------------\n   換一題\n------------\n")
            return generate(change, remove, second, questions_list[-1])

        else:
            return change, remove, second, None


class RemoveOptionCard(ActivationCard):
    """
    Removes one incorrect option `useCard()` method takes a `question` argument
    """

    def useCard(self, question):
        if super().useCard():
            print("\n刪去一個錯誤選項")
            # show one wrong option by convert correct answer to ASCII code and add a random int then convert back to chr
            wrongOption = chr(
                (ord(question.answer) + randint(0, 2)) % 4 + 65)

            print(f"{wrongOption}選項是錯的\n")


class SecondChanceCard(ActivationCard):
    """
    Offers a second answering chance if the answer is incorrect\n
    *Needs to be activated before answering so could be a waste
    """

    def __init__(self):
        super().__init__()
        self.isActivated = False

    def useCard(self):
        if super().useCard():
            print("\n啟用第二次機會\n")
            # Once activated, a wrong answer can bypass the checking system at line 132
            self.isActivated = True
