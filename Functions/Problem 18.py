#Counting odd and even in a list


def counting_odd(num):
    count_even = 0
    count_odd =0

    for i in num:
        if i % 2 == 0:
            count_even += 1

        else:
            count_odd += 1

    return count_even,count_odd

lst = [1,2,3,4,5]
count_even, count_odd = counting_odd(lst)

print(count_even)

