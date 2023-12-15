zin = 'laat mij programmeren want ik loop achter net zoals de hele klas'
def add_length(zin):
    woorden_lijst = []
    losse_woorden = zin.split()
    woorden_lijst.append(losse_woorden)
    for index in woorden_lijst:
        print(index)
    return woorden_lijst

result = add_length('laat mij programmeren want ik loop achter net zoals de hele klas')

print(result)