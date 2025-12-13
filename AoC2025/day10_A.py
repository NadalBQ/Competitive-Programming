
suma = 0
machine = input()
while machine != "":
    machine = machine.split()
    final_state = machine[0][1:-1]
    finish_n = 0
    for i in range(len(final_state)):
        if final_state[i] == "#":
            finish_n += 2**i

    buttons_machine = machine[1:-1]
    buttons = []
    for button in buttons_machine:
        button_ints = [int(x) for x in button[1:-1].split(',')]
        button_n = sum(2**n for n in button_ints)
        buttons.append(button_n)

    presses = len(buttons_machine)
    for i in range(2**len(buttons_machine)):
        res = 0
        parc_press_count = 0
        for j in range(len(buttons_machine)):
            if ((i>>j)%2) == 1:
                res ^= buttons[j]
                parc_press_count += 1
        if res == finish_n:
            presses = min(presses, parc_press_count)
    suma += presses
    machine = input()

print(suma)