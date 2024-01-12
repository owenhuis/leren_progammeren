from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)

bewegen = 1
# Jouw python instructies zet je vanaf hier:
for start in range(10):
    pakken = robotArm.grab()
    if pakken == False:
        break
    for i in range(bewegen):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(bewegen):
        robotArm.moveLeft()
    bewegen += 1 # 1 of 2 moet nog testen
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()