#Finding the sum of positive and negative numbers separately.
def positive_negative_sum(arr):
    positive = 0
    negative = 0

    for i in arr:
        if i > 0:
            positive += i
        else:
            negative += i

    return positive, negative

p, n = positive_negative_sum([10, -5, 7, -3])

print("Positive Sum =", p)
print("Negative Sum =", n)