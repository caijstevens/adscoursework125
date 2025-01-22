

def hash_quadratic(d):
    """Inserts keys from the list d into a hash table and
    returns the HashTable which contains the state of the 
    hash table after these insertions.

    Use just one HashTable instance inside this function.
    
    Use quadratic probing (see question for details) to resolve 
    collisions.
    """

    h = HashTable(17)
   
    for current_key in d:
        attempt = 0
        while attempt < 17:
            pos_check = ((((current_key * 3) + 5) % 17) + (attempt ** 2)) % 17
            
            if h.lookup(pos_check) == '-':
                h.add(pos_check, current_key)
                break
            attempt = attempt + 1

 
    return(h)



def hash_double(d):
    """Inserts keys from the list d into a hash table and
    returns the HashTable which contains the state of the 
    hash table after these insertions.

    Use just one HashTable instance inside this function.
    
    Use double hashing (see question for details) to resolve
    collisions.
    """
    h = HashTable(17)
   
    for current_key in d:
        attempt = 0
        while attempt < 17:
            pos_check = ((((current_key * 3) + 5) % 17) + attempt * (13 - (current_key % 13))) % 17
            
            if h.lookup(pos_check) == '-':
                h.add(pos_check, current_key)
                break
            attempt = attempt + 1

    
    return(h)


