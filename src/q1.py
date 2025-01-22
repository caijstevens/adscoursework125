# q1(a)

def compute_winner(history_A, history_B):
    htotal_A = hcount(history_A)
    htotal_B = hcount(history_B)
    if htotal_A == htotal_B:
        return("D")
    elif htotal_A > htotal_B:
        return("A")
    else:
        return("B")    

def hcount(history):
    best_htotal = 0
    current_htotal =0
    for i in range(0, len(history)):
        if str(history[i]) == "H":
            current_htotal = current_htotal + 1
            if current_htotal > best_htotal:
                best_htotal = current_htotal
                
        elif str(history[i]) == "T":
            if current_htotal > best_htotal:
                best_htotal = current_htotal
            current_htotal = 0
            
    return best_htotal



# q1(b)

def encode(history):
    encoded_history = ""
    i = 0
    current_letter = history[0]
    current_count = 1
    while i < len(history):
        current_letter = str(history[i])
        if (i == len(history) - 1):
            if history[i] == history[i-1]:
                encoded_history = (encoded_history + current_letter + "" + str(current_count))
            else:
                encoded_history = (encoded_history + current_letter + "1")
            return(encoded_history)
        else:
            next_letter = str(history[i+1])
            if next_letter == current_letter:
                current_count = current_count + 1
            else:
                encoded_history = (encoded_history + current_letter + "" + str(current_count))
                current_count = 1
        i = i + 1
    return(encoded_history)



# q1(c)

def decode(compressed_history):
    uncompressed = ""
    i = 0
    while i < len(compressed_history):
        character = str(compressed_history[i])
        repeat = int(compressed_history[i+1])
        for count in range(0, repeat):
            uncompressed = str(uncompressed + character)
        i = i + 2
    return(uncompressed)

# q1(d)

def compute_winner_compressed(compressed_history_A, compressed_history_B):
    high_A = 0
    high_B = 0
    for i in range(0, len(compressed_history_A)):
        if compressed_history_A[i] == "H":
            if int(compressed_history_A[i+1]) > high_A:
                high_A = int(compressed_history_A[i+1])
    for j in range(0, len(compressed_history_B)):
        if compressed_history_B[j] == "H":
            if int(compressed_history_B[j+1]) > high_B:
                high_B = int(compressed_history_B[j+1])
    if high_A == high_B:
        return("D")
    elif high_A > high_B:
        return("A")
    else:
        return("B")
