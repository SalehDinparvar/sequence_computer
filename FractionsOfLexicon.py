# Python program to code and decode with the help of fractions of lexicon of positive integers k<=n subdivided
# lexicographically by their prime factorization.

# Prime lexicon(lexicon): Whole set of positive integers k<=n subdivided lexicographically by their prime
# factorization, which contains set of multiples of a particular integer at a given resolution, in its fraction.

# Reference: https://oeis.org/A336533

import math

eng = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z", " "]


def text_int(s, l):  # convert text to number
    n = 0
    s = list(s)
    c = 0
    for i in range(len(s)):
        n += (len(l) + 1) ** i * (l.index(s[i]) + 1)
    return n


def int_text(n, l):  # convert number to text
    s = ""
    while n > len(l):
        s += l[n % (len(l) + 1) - 1]
        n //= len(l) + 1
    s += l[n - 1]
    return s


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


def nth_prime(n):  # return n-th prime number
    c = -1
    i = 1
    while n != c:
        if is_prime(i):
            c += 1
            i += 1
        else:
            i += 1
    return i - 1


def next_prime(n):  # return smallest prime >= n
    i = 2
    c = 0
    while i < n:
        i = nth_prime(c)
        c += 1
    return i


def integer_fractionOfLexicon(num):  # return at which fraction of lexicon are set of multiples of an integer
    numberLexicalFraction = 1
    seenFraction = 0
    prime = 2
    total = 1
    if num == 1:
        return 1
    while num > 1:
        total *= prime
        seenFraction *= prime
        numberLexicalFraction *= prime
        if num % prime == 0:
            num //= prime
            numberLexicalFraction //= prime
        else:
            seenFraction += numberLexicalFraction // prime
            numberLexicalFraction -= numberLexicalFraction // prime
            prime = next_prime(prime + 1)
    seenFraction += numberLexicalFraction
    return seenFraction / total


def fractionOfLexicon_integer(fraction, resolution):
    # return the integer which its set of multiples are at the given fraction of lexicon for given resolution
    seenFraction = 0
    prime = 1
    unseenFraction = 1
    numberLexicalFraction = 0
    extract = 1
    counter = 0
    if fraction == 1:
        return 1
    if 0 < fraction < 1 and 0 < resolution < 1:
        while not (seenFraction - resolution < fraction < seenFraction + resolution):
            counter += 1
            if counter > 5000:
                return "error"
            if fraction > seenFraction:
                prime = next_prime(prime + 1)
                numberLexicalFraction = unseenFraction / prime
                seenFraction += numberLexicalFraction
                unseenFraction -= numberLexicalFraction
            if seenFraction - resolution < fraction < seenFraction + resolution:
                extract *= prime
                return extract
            if fraction < seenFraction:
                seenFraction -= numberLexicalFraction
                unseenFraction = numberLexicalFraction
                numberLexicalFraction /= prime
                unseenFraction -= numberLexicalFraction
                seenFraction += numberLexicalFraction
                extract *= prime
        extract *= prime
        return extract
    else:
        return fractionOfLexicon_integer(float(input("\nEnter positive value <=1 for fraction:\n  ")),
                                         float(input("\nEnter positive value <=1 for resolution:\n  ")))


def prog():  # main program
    state = input(
        "\n\"cn\" to code numbers\n\"dn\" to decode numbers\n\"ct\" to code texts\n\"dt\" to decode texts\nEnter:  ")
    if state.lower() == "cn":
        s = int(input("\nType an integer:\n  "))
        num = integer_fractionOfLexicon(s)
        resolution = 1 / 10
        if num != "error":
            while s != fractionOfLexicon_integer(num, resolution):
                if resolution < 1 / 10 ** 16:
                    print("Try smaller input, it takes too long!")
                    return prog()
                else:
                    resolution /= 2
            print("\nFraction of lexicon:", num, "\nResolution:", resolution)
        else:
            print("Try smaller input, takes too long!")
            return prog()
    if state.lower() == "dn":
        num = float(input("\nEnter fraction of lexicon:\n  "))
        resolution = float(input("\nEnter resolution:\n  "))
        print("\nOriginal number: ", fractionOfLexicon_integer(num, resolution))
    if state.lower() == "ct":
        s = input("\nEnter text (a few english characters plus space):\n  ")
        num = integer_fractionOfLexicon(text_int(s, eng))
        resolution = 1 / 10
        if num != "error":
            while s != int_text(fractionOfLexicon_integer(num, resolution), eng):
                if resolution < 1 / 10 ** 16:
                    print("Try smaller input, it takes too long!")
                    return prog()
                else:
                    resolution /= 2
            print("\nFraction of lexicon:", num, "\nResolution:", resolution)
        else:
            print("Try smaller input, it takes too long!")
            return prog()
    if state.lower() == "dt":
        num = float(input("\nEnter fraction of lexicon:\n  "))
        resolution = float(input("\nEnter resolution:\n  "))
        print("\nOriginal text: ", int_text(fractionOfLexicon_integer(num, resolution), eng))


while True:
    prog()


# https://oeis.org/wiki/User:Mohammad_Saleh_Dinparvar , SEP 6 2020
