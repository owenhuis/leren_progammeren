from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
for blub in range(5):
    for i in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    if blub < 4:
        robotArm.moveRight()
        robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()