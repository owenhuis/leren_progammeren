reeks = [1]
drie_op_een_rij = False

start = 1 

while drie_op_een_rij == False:
    nieuwe_reeks = []
    count = 1 
    for i in range(1, len(reeks)):
        if reeks[i] == reeks[i - 1]:
            count += 1
        else:
            nieuwe_reeks.append(count)
            nieuwe_reeks.append(reeks[i - 1])
            count = 1
    nieuwe_reeks.append(count) 
    nieuwe_reeks.append(reeks[-1]) 
    reeks = nieuwe_reeks
    for y in reeks:
        print(y, end='')
    print()

    for laatste_check in range(len(reeks)):
        if reeks[laatste_check] == 3 and reeks[laatste_check + 1] == 3:
            drie_op_een_rij = True
