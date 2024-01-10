# start_getal = 50
# hoeveelheid = 50
# toevoegen = 51

# print(hoeveelheid)
# while hoeveelheid < 1000:
#     print(f'{start_getal} + {toevoegen} = {hoeveelheid}')
#     hoeveelheid = hoeveelheid + toevoegen
#     toevoegen += 1
#     if hoeveelheid >= 1000:
#         print('nu heb je meer dan of duizend getallen')
#         break


total_sum = 0
current_number = 50
iteration = 1

while total_sum <= 1000:
    total_sum += current_number
    print(f"{iteration}. {'+'.join(map(str, range(50, current_number+1)))} = {total_sum}")
    
    current_number += 1
    iteration += 1
