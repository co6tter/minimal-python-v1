scores = [10, 20, 30, 20, 40]
scores.append(60)

scores.extend([70, 80])
scores += [70, 80]

scores *= 3

scores.insert(1, 15)


# scores.clear() # → []

scores.remove(20)

# popped_item = scores.pop(2)
# del scores[2]

popped_item = scores.pop()  # 末尾の要素になる

print(scores)
print(popped_item)

print(scores.count(20))
# 最初に20のindex
print(scores.index(20))
print(20 in scores)

# scores.reverse() # 破壊的
# scores.sort()
# scores.sort(reverse=True) # 破壊的
scores_sorted = sorted(scores, reverse=True)  # 非破壊的
print(scores)
print(scores_sorted)

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[2:5] = [200, 300, 400]

nums[2:2] = [1.5]

# sliced_list = nums[2:5]
# 非破壊的に逆にする
sliced_list = nums[::-1]

print(nums)
print(sliced_list)

prices = [100, 200, 150, 200, 100]

for index, price in enumerate(prices):
    print(f"{index}: {price * 1.1:.2f}")

# prices_with_tax = [price * 1.1 for price in prices]  # リスト内包表記
prices_with_tax = [price * 1.1 for price in prices if price != 200]

print(prices_with_tax)

# タプル
# 値を変更できない
# in, len(), index(), count() ... → 使える
# append(), insert(), pop() ... → 使えない

# tokyo = ("JPY", 36, 140)
tokyo = "JPY", 36, 140  # 丸括弧省略可

# 変更するときはlistに変換
tokyo = list(tokyo)
tokyo[0] = "YEN"
tokyo = tuple(tokyo)
print(tokyo)
print(tokyo[0])

# currency, lat, long = tokyo  # アンパック
_, lat, long = tokyo
print(lat)
print(long)

currency, *location = tokyo
print(location)  # listになる

scores2 = {"math": 62, "english": 91, "physics": 84}

for key in scores2.keys():
    print(key)

for value in scores2.values():
    print(value)

for key, value in scores2.items():
    print(f"{key:8} {value:3}")

eng_members = ["Taro", "Jiro", "Saburo"]
math_members = ["Jiro", "Saburo", "Shiro"]

eng_members = set(eng_members)
math_members = set(math_members)

print(eng_members | math_members)  # 和集合
print(eng_members & math_members)  # 積集合
print(eng_members - math_members)  # 差集合

# Mutable
# リスト、辞書、集合

# Immutable
# タプル、文字列、集合(fronzenset)、数値、真偽値、None

nums1a = [10, 20, 30]
# nums1a_bak = nums
nums1a_bak = nums1a.copy()
nums1a[0] = 100

print(nums1a)
print(nums1a_bak)

keys1a = ["math", "english", "physics"]
values1a = [62, 91, 84]

for item in zip(keys1a, values1a):
    print(item)

# scores1a = {}
# # for item in zip(keys1a, values1a):
# #     # print(item)
# #     key, value = item
# #     # scores1a["math"] = 62
# #     scores1a[key] = value
# for key, value in zip(keys1a, values1a):
#     scores1a[key] = value

scores1a = {key: value for key, value in zip(keys1a, values1a)}

print(scores1a)

scores1b = [
    {"name": "Taro", "math": 70, "english": 82},
    {"name": "Jiro", "math": 67, "english": 61},
    {"name": "Saburo", "math": 81, "english": 58},
]

print("Name     Math     English")
print("-------- -------- --------")


# def compare(score):
# return score["math"]


# scores1b.sort(key=compare, reverse=True)
scores1b.sort(key=lambda score: score["math"], reverse=True)

for score in scores1b:
    # print(f"{score['name']:8} {score['math']:8} {score['english']:8}")
    for value in score.values():
        print(f"{value:8} ", end="")
    print()
