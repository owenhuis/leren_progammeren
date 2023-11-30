weekdagen = 'maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondaag'

for dag_in_de_week in weekdagen:
    print(dag_in_de_week, end=' ')
print()
for werkdagen in  range(len(weekdagen)):
    print(weekdagen[werkdagen])