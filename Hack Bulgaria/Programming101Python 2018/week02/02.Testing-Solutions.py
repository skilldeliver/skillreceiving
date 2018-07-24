
def simplify_fraction(fraction):
    nom = fraction[0]
    den = fraction[1]

    for i in range(nom, 1, -1):
        if nom % i == 0 and den % i == 0:
            nom = nom / i
            den = den / i

    return (int(nom), int(den))

def collect_fractions(fractions):
    n1, d1 = fractions[0][0], fractions[0][1]
    n2, d2 = fractions[1][0], fractions[1][1]
    n3, d3 = n1 * d2 + n2 * d1, d1 * d2 

    return simplify_fraction((n3, d3))

def sort_fractions(fractions):
    decimals = [fractions[el][0] / fractions[el][1] for el in range(len(fractions))]
    s_decimals = sorted(decimals)
    indexes = [decimals.index(el) for el in s_decimals]

    return [fractions[i] for i in indexes]        

if __name__ == "__main__":
    print("1. Simplify fractions")
    print("---------------------------------")
    print(simplify_fraction((3,9)))
    print(simplify_fraction((1,7)))
    print(simplify_fraction((4,10)))
    print(simplify_fraction((63,462)))
    print("---------------------------------")
    print("    ")
    print("2. Collect fractions")
    print("---------------------------------")
    print(collect_fractions([(1, 4), (1, 2)]))
    print(collect_fractions([(1, 7), (2, 6)]))
    print("---------------------------------")
    print("    ")
    print("3. Sort array of fractions")
    print("---------------------------------")
    print(sort_fractions([(2, 3), (1, 2)]))
    print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
    print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))
    print("---------------------------------")