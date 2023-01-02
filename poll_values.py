d = {'Alex': 2, 'Cam': 5, 'Claire': 5, 'Gloria': 7, 'Manny': 2, 'Phil': 9}

def find() :
    highest_poll = max(d.values())
    for char in d :
        if d[char] == highest_poll :
            value = char
            break
        
    return value






