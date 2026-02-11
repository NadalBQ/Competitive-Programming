no_suit = {"T": 10, "J": 2, "Q": 3, "K": 4, "A": 11, "9": 0, "8": 0, "7": 0}
yes_suit = {"T": 10, "J": 20, "Q": 3, "K": 4, "A": 11, "9": 14, "8": 0, "7": 0}

n, k = input().split()
total = 0
for i in range(4*int(n)):
    x = input()
    a, suit = x[0], x[1]
    if suit == k:
        n_points = yes_suit[a]
    else:
        n_points = no_suit[a]
    total += n_points
    
print(total)