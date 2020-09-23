import os

import pandas as pd


class Question:
    """
    The `Question` class takes 1 argument and contains 6 attributes\n

    Argument:\n
          index: The index of the question from the data\n
    Attributes:\n
          question: The question itself
          A: Option A
          B: Option B
          C: Option C
          D: Option D
          answer: The answer to the question
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


path = os.path.abspath("questions.csv")
df = pd.read_csv(path)
