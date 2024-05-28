def score(dice):
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for die in dice:
        counts[die] += 1
    score = 0

    for value, count in counts.items():
        if count >= 3:
            if value == 1:
                score += 1000
            else:
                score += value * 100
            count -= 3
        
        if value == 1:
            score += count * 100
        elif value == 5:
            score += count * 50
    return score
