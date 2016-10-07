def productSum(bound):
    """ Return the sum of the distinct minimum product sum numbers
    from 2 to <bound>.

    @type bound: int
    @rtype: int
    """
    multiples = [[x] for x in range(2, bound // 2 + 2)]
    factors = findFactors(multiples, bound)
    temp = {}
    ps = set()
    for numbers in factors:
        prod = product(numbers)
        s = sum(numbers)
        count = len(numbers) + prod - s
        if count in temp:
            temp[count] = min(temp[count], prod)
        else:
            temp[count] = prod
    for key in temp:
        if key > bound:
            break
        else:
            ps.add(temp[key])
    return sum(ps)


def findFactors(multiples, bound):
    """ Return a list containing the lists of factors for each
    list in <multiples>.

    This is a helper function for productSum.

    @type multiples: list of lists[int]
    @type bound: int
    @rtype: list of lists[int]
    """
    if findProducts(multiples, bound):
        return []
    else:
        factorsLst = []
        for lst in multiples:
            prod = product(lst)
            if prod < 2 * bound:
                factors = []
                for num in range(lst[0], 2 * bound // prod + 1):
                    new_lst = list(lst)
                    new_lst.append(num)
                    factors.append(new_lst)
                factorsLst += factors
                factorsLst += findFactors(factors, bound)
        return factorsLst

def product(lst):
    """ Return the product of the integers in <lst>.

    This is a helper function for productSum.
    @type lst: list[int]
    @rtype: int
    """
    prod = 1
    for num in lst:
        prod = prod * num
    return prod

def findProducts(multiples, bound):
    """ Return True if the product of every list in <multiples> is greater than
    or equal to 2 * <bound>. Otherwise, return False.

    @type multiples: list of lists[int]
    @type bound: int
    @rtype: bool
    """
    for lst in multiples:
        if product(lst) < 2 * bound:
            return False
    return True

x = productSum(12000)
print(x)
