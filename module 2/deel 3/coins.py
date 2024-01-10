# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #input betalen
paid = int(float(input('Paid amount: ')) * 100) #input gegeven
change = paid - toPay #change berekenen

if change > 0: # start if
  coinValue = 500 #de hoogste value coin voor in een latere berekening
  
  while change > 0 and coinValue > 0: #start while loop
    nrCoins = change // coinValue #berekening change hoeveelhijd
    
    if nrCoins > 0: #start voor een berekening en print met een ifp
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # je print de hoeveelheid dat terug moet worden gegeven en de coin grootte
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # input hoeveel munten je terug geeeft
      change -= nrCoinsReturned * coinValue #berekening om de change hoeveelhijd om laag te halen en om daarna als er nog change over is dat er dan opnieuw de loop wordt gedaan
    

# comment on code below: als de coinvalue een bepaalde grote heeft wordt het een kleinere grote
    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # als de change groter is dan 0 dan wordt er aan gegeven dan print er welke change je mist anders print er done
  print('Change not returned: ', change / 100,' cents')
elif change <= 0:
  print('done')