def diamond(number):
    number_2 = number // 2
    number_3 = 1
    result_1 = ''

    if number <= 0 or number % 2 == 0:
        return None
    else:
        for x in range(0, number + 1):
            if x % 2 != 0:
                result_1 = result_1 + ' ' * number_2 + ('*' * x) + '\n'
                number_2 = number_2 - 1
        for y in reversed(range(0, number - 1)):
            if y % 2 != 0:
                result_1 = result_1 + ' ' * number_3 + ('*' * y) + '\n'
                number_3 = number_3 + 1

        return result_1
