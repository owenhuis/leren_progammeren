from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')


# Jouw python instructies zet je vanaf hier:
for i in range(8):
    robotArm.moveRight()
for start in range(9):
    print(start)      
    robotArm.grab()
    color = robotArm.scan()
    if color == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    if start < 8:
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()