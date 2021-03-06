import time
import re

#番号を追加する関数
def add_of_file():
    with open("1000_yen.txt","a",encoding="utf-8") as write:
        write.write("{}\n".format(number))

#番号を読み、リストにする
def read_of_file():
    global line
    with open("1000_yen.txt","r",encoding="utf-8") as check:
        line=[s.strip() for s in check.readlines()]
#閲覧の関数
def view():
    read_of_file()
    line.sort()
    print(line)

def add():
    print("番号を入力")
    print("例:GX563636M 等")
    global number
    number=input()
    pattern=r"[A-Z]{2}[0-9]{6}[A-Z]{1}"
    if re.fullmatch(pattern,number):
        read_of_file()
        check_result=number in line

        if check_result == False:
            add_of_file()
            print("入力完了")

        else:
            print("その番号は既に存在します！")
    else:
        print("正しい番号かな？")

def run():
    print("このプログラムを終えたいときは、CTRL + C もしくは CTRL + Z を押してください")
    print("追加したいですか？　閲覧したいですか？")
    print("追加:0, 閲覧:1")
    dochira=int(input())
    if dochira==0:
        while True:
            add()
            time.sleep(0.5)
    elif dochira==1:
        view()
    else:
        pass
