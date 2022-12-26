d = {'Phil': 0, 'Alex': 0, 'Gloria': 0, 'Manny': 0, 'Cam': 0, 'Claire': 0}

def find() :
    highest_poll = max(d.values())
    for char in d :
        if d[char] == highest_poll :
            value = char
            break
        
    return value
