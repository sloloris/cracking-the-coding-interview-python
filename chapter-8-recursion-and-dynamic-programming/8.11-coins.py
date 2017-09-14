""" 8.11 Coins: Given an infinite number of quarters, dimes, nickels, and pennies, write code to calculate the number of ways of representing n cents. """

# def coins(n, index):
#     denoms = [25, 10, 5, 1]
#     

def combos(amt):
    bills = [25, 10, 5, 1]
    possibilities = []
    def _combos(amt, min_bill_index, change, possibilities):
        for i in range(min_bill_index, len(bills)):
            change_so_far = change[:]
            s = amt
            while s > 0:
                s -= bills[i]
                if s >= 0:
                    change_so_far.append(bills[i])
                    if (s > 0):
                        _combos(s, i + 1, change_so_far, possibilities)

            if s == 0:
                possibilities.append(change_so_far)
    _combos(amt, 0, [], possibilities)
    return possibilities

if __name__ == "__main__":
    for i in range(1, 100, 5):
        print i, len(combos(i))