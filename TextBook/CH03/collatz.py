def collatz(number): # コラッツ関数
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def main(): # メインのプログラム
    try:
        number = int(input("正の整数を入力してください"))
        if number <= 0: #　故意にErrorを出してプログラムの終了
            raise ValueError("You are idiot!!") 
    except ValueError as e:
        print(e)
        return

    while number != 1:
        number = collatz(number)
        print(number)
main()