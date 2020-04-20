# python program to produce series of the sequence in https://oeis.org/A188429


def range_n(n):  # returns set of 1 to n
    n_list = []
    for i in range(n):
        n_list.append(i + 1)
    return n_list


def subset(a_list):  # returns all subsets of a set, except null
    result = []
    n = len(a_list)
    for i in range(2**n):
        list2 = []
        s = bin(i)
        s = s[2:]
        while len(s) < n:
            s = "0"+s
        for ii in range(len(s)):
            if s[ii] == "1":
                list2.append(a_list[ii])
        result.append(list2)
    res = []
    for i in result:
        if len(i) > 0:
            res.append(i)
    return res


def are_sets_equal(set_a, set_b):  # returns True if both given sets are equal
    for i in set_a:
        if i not in set_b:
            return False
    for i in set_b:
        if i not in set_a:
            return False
    return True


def sum_of_subsets(a_set):  # returns the set of summation of all elements within all subsets of a set
    r=[]
    for i in subset(a_set):
        r.append(sum(i))
    return r


def nfull(n):  # returns set of all n-full sets for a given number
    result = []
    for i in subset(range_n(n//2+1)):  # omitting entries greater than [n/2]+1
        if are_sets_equal(sum_of_subsets(i), range_n(n)):
            result.append(i)
    return result


def sequence_term(n):  # returns the minimum of the set {max A: (sum A)=[n] }
    max_nfull = []
    for i in nfull(n):
        max_nfull.append(max(i))
    if len(max_nfull) == 0:
        return 0
    else:
        return min(max_nfull)


def prog():  # enter number of the terms to process
    n = int(input("Enter number of elements: "))
    for i in range(n):
        i += 1  # offset=1
        print(sequence_term(i), end=" ")
    return 0


prog()

#  https://oeis.org/wiki/User:Mohammad_Saleh_Dinparvar , APR 20 2020

