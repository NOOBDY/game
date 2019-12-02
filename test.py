print("hello world")
# token = open("token.txt", "r")
with open("token.txt", "r") as token:
    print(token.read())