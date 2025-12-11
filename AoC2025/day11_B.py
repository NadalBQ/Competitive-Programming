from functools import lru_cache

@lru_cache(maxsize=None)
def count_paths_from(device, passed_dac = False, passed_fft = False):
    if device == "dac":
        passed_dac = True
    if device == "fft":
        passed_fft = True
    if device == "out" and passed_dac and passed_fft:
        return 1
    elif device == "out":
        return 0
    else:
        suma = 0
        for output in dic[device]:
            suma += count_paths_from(output, passed_dac, passed_fft)
        return suma
    

dic = {}
message = input()
while message != "":
    device, output = message.split(":")
    output = output.split()
    dic[device] = output
    message = input()

print(count_paths_from("svr"))