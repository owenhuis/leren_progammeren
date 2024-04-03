def fibonacci_reeks(aantal_snedes):
    snede = [0,1]

    for _ in range(aantal_snedes-2):
        snede.append(snede[-1] + snede[-2])
    
    
    print(', '.join(str(nummer)for nummer in snede))
        

    if len(snede) >= 3:
        gulden_snede = snede[-1] / snede[-2]
        print(f'\n{gulden_snede}')
        

fibonacci_reeks(29)