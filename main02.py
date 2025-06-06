def double(n):
    return n * 2


def greet(name, by):
    print(f"{by} said, hi! {name}")


def show_time(h, m, s=0, ms=0):
    print(f"{h:02}:{m:02}:{s:02}.{ms:03}")


def get_price(a, b, rate):
    # global rate  globalキーワードを使うとグローバル変数使えるけど、書き換わってしまうので変数で渡すほうがよい
    if a + b >= 3000:
        rate = 1.05
    total = (a + b) * rate  # 関数定義内で変数を代入するコードがあれば、ローカル変数になる
    return total


def calc(n, func):
    return func(n)


print(double(10))

greet(name="Taro", by="John")  # キーワード引数
greet("Jiro", "Rich")  # 位置引数

show_time(11, 23, 52, 220)
show_time(4, 54, 2, 12)
show_time(12, 3)
show_time(5, 25, 32)

rate = 1.1
print(get_price(300, 700, rate))

print(calc(10, lambda n: n * 2))
print(calc(10, lambda n: n * 3))
