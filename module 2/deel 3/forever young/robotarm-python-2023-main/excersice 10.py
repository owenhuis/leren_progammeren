from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

rechts = 9
links = 8
# Jouw python instructies zet je vanaf hier:
for start in range(5):
    print(start)
    robotArm.grab()
    for left in range(rechts):
        robotArm.moveRight()
    robotArm.drop()
    if start == 4:
        break
    for right in range(links):
        robotArm.moveLeft()
    rechts -= 2
    links -= 2
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()