from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

rood = 9
door = 9
# Jouw python instructies zet je vanaf hier:
for start in range(9):
    print(start)
  
    print(rood)

    robotArm.grab()
    color = robotArm.scan()
    print(color)
    if color == 'red':
        for i in range(rood):
            robotArm.moveRight()
        robotArm.drop()
        if start == 8:
            break
        for i in range(door):
                robotArm.moveLeft()
    elif color != 'red':
        robotArm.drop()
    if start == 8:
        break
    robotArm.moveRight()
    rood -= 1
    door -=1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()