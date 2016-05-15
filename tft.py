last_round = -1;
points = 0;
def nextOutput():
    if last_round == 1 or last_round == 0:
        return False
    elif last_round == 5 or last_round == 3:
        return True
    else:
        return True
    
def addPoints(i):
    global points;
    global last_round;
    points = points+i;
    last_round = i;
