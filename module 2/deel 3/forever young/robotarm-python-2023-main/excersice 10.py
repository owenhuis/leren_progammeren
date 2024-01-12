from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

rechts = 9

# Jouw python instructies zet je vanaf hier:
for start in range(5):
    robotArm.grab()
    for right in range(rechts):
        robotArm.moveRight()
    robotArm.drop()
    rechts -= 1
    if start < 4:
        for left in range(rechts):
            robotArm.moveLeft()
    rechts -= 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()