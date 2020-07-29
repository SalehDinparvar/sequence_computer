# python program to produce series of the sequence in https://oeis.org/A336533


import math
from operator import itemgetter


def is_prime(n):  # return True if input is prime
    if n <= 1:
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True


def nth_prime(n):  # return nth prime number
    c = -1
    i = 1
    while n != c:
        if is_prime(i):
            c += 1
            i += 1
        else:
            i += 1
    return i - 1


def next_prime(n):  # return the prime number comes after or equal to input
    i = 2
    c = 0
    while i < n:
        i = nth_prime(c)
        c += 1
    return i


def number_portion(num):  # returns the portion of lexical subdivision of natural numbers, that are multiples of input
    if num == 0:
        return "error"
    if num == 1:
        return 1
    portion = 1
    prime = 2
    total = 1
    while num > 1:
        total *= prime
        portion *= prime
        if num % prime == 0:
            num //= prime
            portion //= prime
        else:
            portion -= portion // prime
            prime = next_prime(prime + 1)
    return portion / total


def ordered_naturals_by_portion(n):  # return list of integers ordered by their lexical portion of multiples
    l = []
    for i in range(n):
        i += 1
        l.append([i, number_portion(i)])
    l = sorted(l, key=itemgetter(1))
    l.reverse()
    ll = []
    for i in l:
        ll.append(i[0])
    return ll


def prog():  # program to simplify execution, alo increase accuracy
    num = int(input("\nPrint terms up to number: "))
    x = 1
    while 1 / 2 ** x > number_portion(num):  # it require more terms to be accurate
        x += 1
    sqnc = ordered_naturals_by_portion(2 ** x)
    print(sqnc[:sqnc.index(num) + 1])


while True:
    prog()

#  https://oeis.org/wiki/User:Mohammad_Saleh_Dinparvar , Jul 29 2020
