testCases = int(input())
orden = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for case in range(testCases):
    strNumber = input()
    cursor = 1
    seconds = 0
    caseSolved = False
    digit = 0  # el testcase tiene 4 digitos (0-3)
    while not caseSolved:
        if digit == 4:
            caseSolved = True
        elif orden[cursor - 1] == int(strNumber[digit]):
            # click
            seconds += 1
            digit += 1
        elif int(strNumber[digit]) < cursor:
            if int(strNumber[digit]) == 0:
                cursor += 1
                seconds += 1
            else:
                cursor -= 1
                seconds += 1
        elif int(strNumber[digit]) > cursor:
            cursor += 1
            seconds += 1
    print(seconds)