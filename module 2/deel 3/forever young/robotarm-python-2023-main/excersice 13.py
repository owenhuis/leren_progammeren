from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)


# Jouw python instructies zet je vanaf hier:
for start in range(1,7):
    print(start)
    pakken = robotArm.grab()
    if pakken == False:
        break
    for i in range(start):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(start):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()