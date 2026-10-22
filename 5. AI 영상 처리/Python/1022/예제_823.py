while True:
    input1 = int(input('number? '))
    if input1 == 0:
        break

    if input1 > 0:
        print('positive integer')
    elif input1 < 0:
        print('negative number')