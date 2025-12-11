
def count_paths_from(device):
    if device == "out":
        return 1
    else:
        for output in dic[device]:
            suma += count_paths_from(output)
        return suma
    

dic = {}
message = input()
while message != "":
    device, output = message.split(":")
    output = output.split()
    dic[device] = output
    message = input()

print(count_paths_from("you"))