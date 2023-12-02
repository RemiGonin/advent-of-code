with open("input.txt", "r") as f:
    data = f.read().splitlines()
    f.close()

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

calibrationValueSum = 0
for line in data:
    left = 0
    right = len(line) - 1

    firstNum = None
    lastNum = None
    while firstNum is None or lastNum is None:
        for num in numbers:
            if firstNum is None:
                if left + len(num) <= len(line):
                    if line[left : left + len(num)] == num:
                        firstNum = numbers.index(num) + 1

                if line[left].isdigit():
                    firstNum = int(line[left])

            if lastNum is None:
                if right - len(num) >= 0:
                    if line[right - len(num) + 1 : right + 1] == num:
                        lastNum = numbers.index(num) + 1

                if line[right].isdigit():
                    lastNum = int(line[right])

            if lastNum is not None and firstNum is not None:
                calibrationValueSum += int(str(firstNum) + str(lastNum))
                break

        left += 1
        right -= 1


print(calibrationValueSum)
