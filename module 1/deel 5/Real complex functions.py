#opdracht 1# toets_data has name:score combinations separated by a komma
toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
separator = ','
position= 8 # position of Bram, first position starts with 0

def get_value(toets_data: str, separator: str, position: int) -> str:
    splitted_strings = toets_data.split(separator) # string splits itself into collection of strings
    if 0 <= position< len(splitted_strings):
        value = splitted_strings[position] # read value at position of split_values
        return value
    else:
        value = None
        return value

result = get_value(toets_data, separator, position) 
print(result) # prints: Bram:6

#opdracht 2