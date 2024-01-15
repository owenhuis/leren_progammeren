from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
# for start in range(10):
#     robotArm.grab()
#     for i in range(5):
#         robotArm.moveRight()
#     robotArm.drop()
#     if start == 1 or start == 3 or start == 4 or start == 6 or start == 7 or start == 8:
#         robotArm.moveLeft()
#     if start < 9:
#         for i in range(4):
#             robotArm.moveLeft()
for start in range(1,5):
    print(f'start: {start}')
    for x in range(start, 0 ,-1):
        print(f'x {x}')
        robotArm.grab()
        for rechts in range(5):
            robotArm.moveRight()
        robotArm.drop()
        if x != 1:
            robotArm.moveLeft()
        for links in range(4):
            robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()