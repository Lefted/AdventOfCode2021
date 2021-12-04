# lol
# niceLines = [[direction, int(number)] for direction, number in [
#     line.split() for line in open("2\input.txt").readlines()
# ]]
# print(niceLines)

# read the lines of the file
with open("2\input.txt") as f:
    lines = f.read().splitlines()
depth = 0
aim = 0
pos = 0

for line in lines:
    words = line.split()
    if words[0] == "forward":
        pos += int(words[1])
    elif words[0] == "down":
        depth += int(words[1])
    elif words[0] == "up":
        depth -= int(words[1])

print(f"Part 1{depth*pos}")

depth = 0
aim = 0
pos = 0

for line in lines:
    words = line.split()
    if words[0] == "forward":
        pos += int(words[1])
        depth += aim * int(words[1])
    elif words[0] == "down":
        aim += int(words[1])
    elif words[0] == "up":
        aim -= int(words[1])

print(f"Part 2{depth*pos}")
