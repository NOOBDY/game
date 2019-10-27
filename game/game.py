from random import randint
import pandas as pd
import os
import time


path = os.path.abspath("game\\questions.csv")
df = pd.read_csv(path)


def pick(i):
    print(df['題目'][i])
    print("A:{} B:{} C:{} D:{}\n".format(
        df["A選項"][i], df["B選項"][i], df["C選項"][i], df["D選項"][i]))


def check(x, e, f, g):
    activate = False
    while True:
        a = input("請選擇答案:").upper()
        options = ["A", "B", "C", "D"]

        try:
            if a[0] in "ABCDEFG":

                # change question
                if a[0] == "E" and e == False:
                    print("------------\n   換一題\n------------\n")
                    e = True
                    generate(e, f, g)
                    return True, e, f, g
                elif a[0] == "E" and e == True:
                    print("\n此求救卡已使用過\n")

                # delete one option
                if a[0] == "F" and f == False:
                    q = (options.index(df["答案"][x]) + randint(1, 3)) % 4
                    print("\n{}選項是錯的\n".format(options[q]))
                    f = True
                elif a[0] == "F" and f == True:
                    print("\n此求救卡已使用過\n")

                # second chance
                if a[0] == "G" and g == False:
                    print("\n啟用第二次機會\n")
                    g = True
                    activate = True
                elif a[0] == "G" and g == True:
                    print("\n此求救卡已使用過\n")

                # check answer
                if a[0] == df["答案"][x]:
                    print("\n答案正確\n")
                    return True, e, f, g

                elif a[0] in "EFG":
                    pass

                elif a[0] != df["答案"][x] and activate == True:
                    print("\n答案錯誤，還有一次機會\n")
                    activate = False

                else:
                    print("\n答案錯誤\n")
                    print("正確答案應為:{}\n".format(df["答案"][x]))
                    return False, e, f, g

            else:
                print("資料錯誤，請重新輸入\n")
        except:
            print("資料錯誤，請重新輸入\n")


def generate(e, f, g):
    i = randint(0, len(df))
    pick(i)
    b, e, f, g = check(i, e, f, g)
    if b == False:
        print("GAME OVER")
        os.system("pause")
        exit(0)
    return e, f, g


def start():
    e_used = False
    f_used = False
    g_used = False

    print("遊戲開始")
    print("輸入A、B、C、D作答，E、F、G啟用求救卡\nE:更換題目  F:刪去選項  G:第二條命\n你準備好了嗎?")
    time.sleep(1)
    for i in range(4):
        print(3 - i)
        time.sleep(2)

    for m in range(10):
        print("第{}題:\n".format(m + 1))

        e_used, f_used, g_used = generate(e_used, f_used, g_used)

        if m == 9:
            print("恭喜挑戰成功")
            os.system("pause")
            exit(0)
        else:
            print("------------\n   下一題\n------------\n")
