from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()
for i in range(6):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'white':
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    elif color == 'red':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()