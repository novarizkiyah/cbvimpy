import datetime

data_waktu = datetime.datetime.now()
print(f"datetime now: {data_waktu}")
print(f"year now: {data_waktu.year}")
print(f"month now: {data_waktu.month}")
print(f"day now: {data_waktu.strftime('%A')}")

# count = 0
data = ["a", "b", "c", "a", "a", "b"]
# for i in data:
#     if i == "b":
#         count+=1
# print(count)

from collections import Counter

data_counter = Counter(data)
print(f"data counter: {data_counter}")
print(f"data a saja: {data_counter['a']}")
print(f"data b saja: {data_counter['b']}")

import io
file = io.open("file_text.txt", "r")
print(file.read())