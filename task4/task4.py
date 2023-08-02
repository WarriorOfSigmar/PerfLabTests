import sys
numbers = sys.argv[1]

with open(numbers, "r") as numbers:
    list_of_nums = [int(line.rstrip()) for line in numbers]


arithmetic_mean = round(sum(list_of_nums)//len(list_of_nums))
count = 0
for i in list_of_nums:
    while i != arithmetic_mean:
        if i < arithmetic_mean:
            i += 1
            count += 1
        elif i > arithmetic_mean:
            i -= 1
            count += 1
print(count)
