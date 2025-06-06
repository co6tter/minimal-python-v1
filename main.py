print("It's \na \npen.")
print("""It's
a
pen.""")
print("""\
It's
a
pen.""")

print("*-" * 10)
print("Taro" " " "Yamada")
print("Taro" + " " + "Yamada")
print("*-" * 10)

fname = "Taro"
lname = "Yamada"
age = 32
print("I am {} {}, {} years old!".format(fname, lname, age))
print(f"I am {fname} {lname}, {age} years old!")  # f文字列

num = input("NUmber? ")
print(type(num))
# print(int(num) * 2)
print(float(num) * 2)

signal = input("Signal color? ")
match signal:
    case "red":
        print("Stop!")
    case "yellow":
        print("Slow down!")
    case "blue" | "green":
        print("Go!")
    case _:
        print("Invalid signal color...")

initial_balance = int(input("Initial Balance? "))

match initial_balance:
    case n if n >= 100_000:
        RATE = 1.1
    case n if n >= 80_000:
        RATE = 1.08
    case n if n >= 60_000:
        RATE = 1.06
    case _:
        RATE = 1.01
print(f"Current rate: {RATE:.2f}")

for i in range(8, 5, -1):  # 8, 7, 6
    print(f"{i} Hello!")

# 真偽値
# True それ以外の値
# False 0 0.0 '' None

try:
    initial_balance = int(input("Initial Balance? "))
except ValueError:
    print("Invalid input, exiting ... ")
    exit()
RATE = 1.1
for year in range(3):
    print(f"Year {year}: {initial_balance * RATE ** year:,.2f}")
