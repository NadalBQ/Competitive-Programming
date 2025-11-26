vowels = ["a", "e"]
consonants = ["b", "c", "d"]

ntest = int(input())

for test in range(ntest):
    chars = int(input())
    line = input()
    palabra = ""
    silaba = ""
    index = 0
    for char in line:
        index += 1

        try:
            char2 = line[index]
        except:
            char2 = "d"
        
        if len(silaba) < 1:
            silaba += char
        elif silaba[-1] not in vowels and char in vowels:
            silaba += char
        elif silaba[-1] in vowels and char not in vowels and char2 in vowels:
            palabra += silaba
            silaba = char
            if index != chars:
                palabra += "."
        elif silaba[-1] in vowels and char not in vowels and char2 not in vowels:
            silaba += char
            palabra += silaba
            silaba = ""

            if index != chars:
                palabra += "."
                
        if index == chars:
            palabra += silaba
    print(palabra)