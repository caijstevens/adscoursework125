def extendMultiple(solutions, current, k):

    length = len(current)
    if length > 2:
        if (current[length-1] - current[length-2]) % k < (current[length-2] - current[length-3]) % k:
            return None
    
    for i in range(0,k):
        if i not in current:
            current.append(i)
            extendMultiple(solutions, current, k)
            current.remove(i)

    if len(current) == k:
        solutions.append(current.copy())
    
    return solutions



def all_orderings(k):
    """
    Returns a list of all Boldon House orderings of size k.
    """
    return extendMultiple([], [], k)
    

def extendSingle(solution, k):
    length = len(solution)
    if length > 2:
        if (solution[length-1] - solution[length-2]) % k < (solution[length-2] - solution[length-3]) % k:
            return solution
    
    for i in range(0,k):
        if i not in solution:
            solution.append(i)
            result = extendSingle(solution, k)
            if len(result) == k:
                return result
            else:
                solution.remove(i)       

    return solution

def ordering(k):
    """
    Returns a Boldon House ordering of size k.
    """
    return extendSingle([], k)
    

