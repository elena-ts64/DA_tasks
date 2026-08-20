def prime_factors(n: int) -> list[int]:
    '''
    Функция при введении натурального числа n разбивает его на простые множители \n
    На вход принимает натуральное число n \n
    Возвращает список простых множителей

    Алгоритм работает за O(√n) по времени
    '''

    if n < 1:
        return print('n не является натуральным числом')

    factors = []

    # обработка множителя 2
    while n % 2 == 0 and n > 1:
        factors.append(2)
        n //= 2

    # проверка нечётных делителей
    divisor = 3

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor

        divisor += 2

    # если осталось число больше 1, оно простое
    if n > 1:
        factors.append(n)

    return factors

if __name__ == '__main__':
    n = 56
    print(prime_factors(n))  # [2, 2, 2, 7]
