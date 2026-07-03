def isArithmetic(lst):
    if len(lst) <= 1:
        return True
    common_diff = lst[1] - lst[0]
    for i in range(1, len(lst) - 1):
        # your turn: compute the difference between lst[i+1] and lst[i]
        # compare it to common_diff
        # what should happen if it doesn't match?
        pass
    return True
