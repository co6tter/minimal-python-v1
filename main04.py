import random
import math
from math import pi as PI
import datetime
import calendar
import os
from pprint import pprint
from collections import defaultdict
from collections import Counter
import copy

# n = random.random()  # 0以上1未満
n = random.randint(1, 6)
print(n)

names = ["Taro", "Jiro", "Saburo", "Shiro", "Goro"]
winner = random.choice(names)
print(winner)

# winners = random.choices(names, k=3)
names = list(set(names))
winners = random.sample(names, 3)
print(winners)

# 最大公約数
print(math.gcd(12, 20, 8))  # 4

print(math.isclose(0.1 * 3, 0.3))

print(PI)

now = datetime.datetime.now()
print(now)

birthday = datetime.datetime(year=2000, month=4, day=11)
print(birthday)

birthday2 = datetime.datetime.strptime("2000-04-11", "%Y-%m-%d")
print(birthday2)

day1 = datetime.datetime(year=2000, month=4, day=11)
day2 = datetime.datetime(year=2001, month=1, day=1)

# diff = day2 - day1  # timedelta
# diff_seconds = diff.total_seconds()
# diff_days = diff_seconds / 60 / 60 / 24
# print(diff_seconds)
# print(diff_days)

delta = datetime.timedelta(days=3, hours=5)
day3 = day1 + delta
print(day3)

calendar.setfirstweekday(calendar.SUNDAY)

cal_str = calendar.month(2001, 1)
print(cal_str)

cal_data = calendar.monthcalendar(2001, 1)
print(cal_data)

print(calendar.isleap(2000))
print(calendar.isleap(2001))

file_name = "names.txt"

f = open(file_name, mode="w")
f.write("Taro\n")
f.close()

if not os.path.isfile(file_name):
    with open(file_name, mode="w") as f:
        f.write("Jiro\n")
else:
    print("File exists!")

try:
    with open(file_name, mode="x") as f:
        f.write("Saburo\n")
except FileExistsError:
    print("File exists!")

names = ["Jiro", "Saburo", "Shiro"]

with open(file_name, mode="a") as f:
    for name in names:
        f.write(f"{name}\n")

with open(file_name, mode="r") as f:
    # names = f.read()
    names = f.read().splitlines()

# print(names, end="")
print(names)

scores = [
    {"name": "Taro", "math": 70, "english": 82},
    {"name": "Jiro", "math": 67, "english": 61},
    {"name": "Saburo", "math": 81, "english": 58},
]

pprint(scores)

results = ["pass", "pass", "fail", "pass", "fail", "pass"]
# stats = {"pass": 4, "fail": 2}

stats = {}
# stats["pass"] += 1
# stats["fail"] += 1
for result in results:
    if result not in stats:
        stats[result] = 0
    # stats["pass"] = stats["pass"] + 1
    stats[result] += 1

print(stats)

# def init():
#     return 0

# stats = defaultdict(init)
# stats = defaultdict(lambda: 0)
stats2 = defaultdict(int)
for result in results:
    # if result not in stats:
    #     stats[result] = 0
    stats2[result] += 1

print(dict(stats2))

stats3 = Counter(results)
print(dict(stats3))

# nums = [10, 20, 30]
# nums_bak = nums.copy() # 浅いコピー
# nums[0] = 100
# print(nums) # [100, 20, 30]
# print(nums_bak) # [10, 20, 30]

nums = [10, 20, 30, [40, 50]]
nums_bak = copy.deepcopy(nums)  # 深いコピー
nums[3][0] = 100
print(nums)  # [10, 20, 30, [100, 50]]
print(nums_bak)  # [10, 20, 30, [40, 50]]
