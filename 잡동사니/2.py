def calc(num1, num2):
    asum = num1 + num2
    asub = num1 - num2
    amulti = num1 * num2
    try:
        adiv = num1 / num2
    except ZeroDivisionError:
        print('문자열 "0"으로는 나눌 수 없습니다.')
    else:
        return asum, asub, amulti, adiv
    return asum, asub, amulti


print(calc(10,0))