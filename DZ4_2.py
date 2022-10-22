number = int(input('Enter number: '))
mn = []
numbers = []
i = 2
while i <= number:
    if number != 1:
        if (number % i == 0):
            mn.append(i)
            numbers.append(number)
            number //= i
        else:  i += 1
mn.append(1)
numbers.append(1)
print(f'Numbers is: {numbers} \nDelitel is: {mn}')
