while True:
    number=int(input('0 to ?? : '))
    if number > 0:
        for ZeroToNumber in range(0, number+1):
            if ZeroToNumber & 0b1 == True:
                print('%d = Odd Number' % (ZeroToNumber))
            else:
                print('%d = Even Number' % (ZeroToNumber))
    else:
        print('Error')
        break