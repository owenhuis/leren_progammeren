from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

rood = 9
door = 8
# Jouw python instructies zet je vanaf hier:
for start in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for i in range(rood):
            robotArm.moveRight()
        robotArm.drop()
        if start < 8:
            for i in range(door):
                    robotArm.moveLeft()
    elif color != 'red':
        robotArm.drop()
    if start < 8 and color != 'red':
        robotArm.moveRight()
    rood -= 1
    door -=1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()