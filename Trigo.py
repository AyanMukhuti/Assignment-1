import math
for i in range(0,360,15):
    print(i, "--",round(math.sin(math.radians(i)),4), round(math.cos(math.radians(i)),4))
