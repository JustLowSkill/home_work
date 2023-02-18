def multiplicity_check(i):
    if i % 3 == 0 and i % 5 ==0:
        return 2*i
    elif i % 3 == 0 or i % 5 ==0:
        return i
    else:
        return 0
def main():
    for j in range(3):
        try:
            i = int(input('Введите, до какого числа:'))
            break
        except:
            print('Э, слыш, баребушек, цыферки напешы!')
            if j == 2:
                print('ERROR, USER IS DOLBAYOB')
                exit()
    print(f'Итоговая сумма: {sum([multiplicity_check(k) for k in range(i)])}')

while 1:
    main()