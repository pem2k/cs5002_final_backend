'''FIND THE MULTIPLICATIVE INVERSE OF A MOD B AND PRINT WORKS
-------------------------------
Functions and Their Description
-------------------------------
find_mod_inverse
    This function takes two positive integers A and B and two bools:
        verbose, and need_json
    It returns a 2-tuple.
    First value is multiplicative inverse of A mod B if it exists, else None.
    Second value is the works,
        if inverse of A mod B exists and verbose is True.
        else None.
        if need_json is True, the second value of the tuple is a json object.
        else it is a tuple of strings.

euclid
    This function takes two integers A and B, and verbose, a boolean.
    If GCD(A, B) 1,
        it returns a 5-tuple of three lists of ints, an integer, and
        a list of strings.
    Else,
        returns None
'''

import json


def find_mod_inverse(A: int, B: int,
                     verbose: bool = False,
                     need_json: bool = False) -> tuple:
    '''
    This function takes two positive integers A and B and a bool verbose
    It returns a 2-tuple.
    First value is multiplicative inverse of A mod B if it exists, else None.
    Second value is the works,
        if inverse of A mod B exists and verbose is True,
        else None.
        if need_json is True, the second value of the tuple is a json object.
        else it is a tuple of strings.
    Params:
    A (int)
    B (int)

    Returns:
    int     x such that Ax = 1 mod B, if it exists, Else None.

    Calls:
    euclidean

    Examples:
    >>> find_mod_inverse(5, 9, verbose=False, need_json=False)
    (2, None)
    >>> find_mod_inverse(50, 90, False)
    (None, None)
    >>> find_mod_inverse(197, 2001, False)
    (1097, None)
    >>> find_mod_inverse(1970, 20010, False)
    (None, None)
    >>> find_mod_inverse(999979, 999983, False)
    (749987, None)
    >>> find_mod_inverse(961748941, 982451653, False)
    (973852246, None)
    '''

    t = euclidean(A, B, True)
    if not t:
        if not verbose:
            return (None, None)
        (None, (f"The multiplicative inverse for {A} mod {B} does not exist."))
    else:
        quotients, first_vars, second_vars, remainders, counter, works = t
        n = counter

    # Reverse
    if verbose:
        works.append('')
        works.append('-'*80)
        works.append('Second Part: Reversing')
        works.append('-'*80)
    # initiate variables
    c1 = 0
    c2 = 1
    v2 = 1
    # reassigning
    q = quotients.pop()
    temp = c2
    c2 = c1 - c2 * q
    c1 = temp
    counter += 1
    v1 = first_vars.pop()
    v2 = second_vars.pop()
    r = remainders.pop()
    if verbose:
        # printing
        works.append(f'Isolating {r} from ({n})')
        n -= 1
        equation_str = f'1 = {v1} * {c1} + {v2} * {c2}'
        counter_str = f'... ({counter})'
        works.append(f'{equation_str:<70}{counter_str:>10}')
    while quotients:
        # reassigning
        q = quotients.pop()
        temp = c2
        c2 = c1 - c2 * q
        c1 = temp
        counter += 1
        v1 = first_vars.pop()
        v2 = second_vars.pop()
        r = remainders.pop()
        if verbose:
            works.append(f'Isolating {r} from ({n}) and putting in \
({counter - 1}).')
            works.append(f'Rearrange to keep as a linear combination of \
{v1} and {v2}:')
            n -= 1
            equation_str = f'1 = {v1} * {c1} + {v2} * {c2}'
            counter_str = f'... ({counter})'
            works.append(f'{equation_str:<70}{counter_str:>10}')
            works.append('')
    if c2 < 0:
        old_c2 = c2
        old_c1 = c1
        k = 0
        while c2 < 0:
            k += 1
            c2 += B
        assert (1 - c2*v2) % v1 == 0
        c1 = (1 - c2*v2)//v1
        if verbose:
            counter += 1
            works.append('Because we want a positive multiplicative inverse')
            works.append(f"    replace {old_c2} with {old_c2} + k * {B}")
            works.append(f"    such that {old_c2} + k * {B} > 0.")
            works.append(f"In this case, k = {k} and we replace {old_c2} \
with {c2}.")
            works.append(f"    Also find new coefficient of {B} as")
            works.append(f"    {old_c1} - k * {A} = {c1}, since k = {k}.")
            works.append('')
            works.append(f"Finally:")
            equation_str = f'1 = {B} * {c1} + {A} * {c2}'

            counter_str = f'... ({counter})'
            works.append(f'{equation_str:<70}{counter_str:>10}')
            works.append('')

    if verbose:
        works.append(f'Bézout\'s coefficients are {c1} and {c2}.')
        works.append('')
        works.append(f'The multiplicative inverse of {A} mod {B} is {c2}.')
        works.append('-'*80)

    multiplicative_inverse = c2
    if verbose:
        if need_json:
            works = json.dumps(works)
            return multiplicative_inverse, works
        return multiplicative_inverse, works
    return multiplicative_inverse, None


def euclidean(A: int, B: int, verbose: bool = False) -> tuple:
    '''
    This function takes two integers A and B, and a bool verbose.
    If GCD(A, B) is 1,
        it returns a 6-tuple of four lists of ints, an integer, and
        a list of strings.
    Else,
        returns None
    '''
    # initiate stacks
    first_vars = list()
    second_vars = list()
    quotients = list()
    remainders = list()
    works = list()
    # initiate variables
    greater = B
    smaller = A
    q = greater // smaller
    mod = greater % smaller
    counter = 1
    # fill stacks
    first_vars.append(greater)
    second_vars.append(smaller)
    quotients.append(q)
    remainders.append(mod)
    if verbose:
        works.append('-'*80)
        works.append('First Part: Euclidean Algorithm')
        works.append('-'*80)
        works.append('Euclidean algorithm gives us the following equations.')
        works.append('')
        equation_str = f'{greater} = {smaller} * {quotients[-1]} + {mod}'
        counter_str = f'... ({counter})'
        works.append(f'{equation_str:<70}{counter_str:>10}')
    while mod > 0:
        # reassign variables
        greater = smaller
        smaller = mod
        q = greater // smaller
        mod = greater % smaller
        # fill stacks
        first_vars.append(greater)
        second_vars.append(smaller)
        quotients.append(q)
        remainders.append(mod)
        counter += 1
        if verbose:
            # print
            equation_str = f'{greater} = {smaller} * {quotients[-1]} + {mod}'
            counter_str = f'... ({counter})'
            works.append(f'{equation_str:<70}{counter_str:>10}')
        if mod == 1:    # early stop if we know GCD(A, B) is 1
            return quotients, first_vars, second_vars, remainders, counter, works
    return None


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    x, m = find_mod_inverse(197, 2001, True, False)
    for line in m:
        print(line)
    # x, works = find_mod_inverse(197, 2001, True, True)
    # with open('works.json', 'w') as f:
    #    f.write(works)