import re

with open("input.txt") as f:
    data = f.read()

print(
    sum(int(nb[0] + nb[-1]) for nb in [re.findall("\d", x) for x in data.split("\n")])
)
