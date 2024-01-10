from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
for start in range(10):
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    if start == 1 or start == 3 or start == 4 or start == 6 or start == 7 or start == 8:
        robotArm.moveLeft()
    elif start == 9:
        break
    for i in range(4):
        robotArm.moveLeft()
    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()