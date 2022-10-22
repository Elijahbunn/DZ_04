import random

#k = int(input('Enter k: '))
k = 5
coef = []
i = 0
while i <= k:
    coef.append(random.randint(0, 5))
    i += 1
print(f'{k} to {coef}')

i = 0
my_str = ''
print(f'{my_str}')
while i <= k:
    if i <= (k-1):
        step = int(len(coef))-(i+1)
        str_step = str(step)
        str_coef = str(coef[i])
        if coef[i] > 1:
            if step > 1:
                my_str = my_str + str_coef + 'X^' + str_step + ' + '
            elif step == 1:
                my_str = my_str + str_coef + 'X' + ' + '
            else:
                my_str = my_str
        elif coef[i] == 1:
            if step > 1:
                my_str = my_str  + 'X^' + str_step + ' + '
            elif step == 1:
                my_str = my_str  + 'X' + ' + '
            else:
                my_str = my_str
        #print(f'{step} - {my_str}')
    else:
        str_coef = str(coef[i])
        if coef[i] > 0:
            my_str = my_str + str_coef + " = 0"
        elif coef[i] == 0:
            my_str = my_str[0:(int(len(my_str))-3)] + " = 0"
    i += 1

print(f'{my_str}')
path = 'DZ4_4.txt'
data = open(path, 'a')
data.writelines(f'{my_str}\n')
data.close()