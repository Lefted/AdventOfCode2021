def part1(lines): 
    lines = zip(lines, lines[1:])
    return len([1 for x,y in lines if y > x])

levels = list(map(int, open('1/input.txt')))
packages = [x + y + z for x, y, z in zip(levels, levels[1:], levels[2:])]
print(f"Day one\nPart one: {part1(levels)}\nPart two: {part1(packages)}")
