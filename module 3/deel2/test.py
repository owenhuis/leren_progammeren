def flick_switch(lst):
    result = []
    flick_switch = True
    
    for item in lst:
        if item == 'flick':
            flick_switch = not flick_switch
        result.append(flick_switch)
    
    return result
