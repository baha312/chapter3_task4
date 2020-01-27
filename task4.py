# Find minimal positive integer that is not in list. If list contains only n

n = input("Enter a digits:  \n").split(" ")
numbers = n
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers.sort()
print(numbers)

for i in range(1, max(numbers)+2):
    if i > 0 and i not in numbers:
        print(i)
        break
    else:
        continue


