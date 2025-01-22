from random import choice

def SelectPivotPair(L):
    """Return a pair (P0,P1) of pivot elements

    Select 5 distinct random elements from L, sort them,
    and let P0 be the second smallest and P1 the
    second largest of those 5 elements.
    """
    randoms = []
    while len(randoms) < 5:
        current = choice(L)
        if current not in randoms:
            randoms.append(current)
    
    randoms.sort()

    P0 = randoms[1]
    P1 = randoms[3]

    return (P0, P1)

def ThreePartition(L,P0,P1):
    """Return a triple (L0,L1,L2) of sublists of L

    L0 consists of all elements of L smaller or equal P0,
    L1 of all elements of L larger than P0 but smaller or
    equal P1, and L2 of all elements of L larger than P1
    """
    L0 = []
    L1 = []
    L2 = []
    for i in range(len(L)):
        if L[i] <= P0:
            L0.append(L[i])
        elif L[i] <= P1:
            L1.append(L[i])
        else:
            L2.append(L[i])

    return (L0, L1, L2)

def ThreeWayQuickSort(L):
    """Return a sorted version of L

    Use SelectPivotPair, ThreePartition and recursive
    calls to sort L.
    """
    if len(L) <= 10:
        L.sort()
        return L
    else:
        P0, P1 = SelectPivotPair(L)
        (L0, L1, L2) = ThreePartition(L, P0, P1)
        sorted_L0 = ThreeWayQuickSort(L0)
        sorted_L1 = ThreeWayQuickSort(L1)
        sorted_L2 = ThreeWayQuickSort(L2)
        return sorted_L0 + sorted_L1 + sorted_L2
    


