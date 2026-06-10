def getInPlaceDiff(A):
    result = []

    for i in range(len(A)):
        diff = A[i] - A[len(A) - 1 - i]
        result.append(diff)

    return result


# Example
print(getInPlaceDiff([1, 2, 3, 4, 5]))
print(getInPlaceDiff([1]))
print(getInPlaceDiff([1, 2]))