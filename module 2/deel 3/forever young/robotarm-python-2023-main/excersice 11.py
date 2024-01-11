from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')


# Jouw python instructies zet je vanaf hier:

for start in range(9):
    if start == 0:
        for i in range(8):
            robotArm.moveRight()
    robotArm.grab()
    color = robotArm.scan()
    if color == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    elif color != 'white':
        robotArm.drop()
    if start == 8:
        break
    else:
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()