last_output = True 
last_round = -1;
points = 0;
def nextOutput():
    global last_output

    if last_round == -1:
        last_output = True;
        return last_output 
    elif last_round < 3:
        last_output = not last_output
        return last_output
    elif last_round > 2:
        return last_output 
    
def addPoints(i):
    global points;
    global last_round;
    points = points+i;
    last_round = i;
