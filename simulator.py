import getopt , sys
import importlib
import random

miscommunication_rate = 1
num_games = 300
steal_points = 5
cooperate_points = 3
fight_points = 1

def runSimulation(p1, p2):
    p1_choices = []
    p2_choices = []

    for i in range(0, num_games):
        p1_choice = p1.nextOutput();
        p2_choice = p2.nextOutput();

        if(random.randint(0,99) < miscommunication_rate):
            p1_choice = not p1_choice
        if(random.randint(0,99) < miscommunication_rate):
            p2_choice = not p2_choice

        p1_choices.append(p1_choice)
        p2_choices.append(p2_choice)

        if p1_choice and p2_choice:
            p1.addPoints(cooperate_points)
            p2.addPoints(cooperate_points)

        elif p1_choice and not p2_choice:
            p2.addPoints(steal_points)
            p1.addPoints(0)

        elif p2_choice and not p1_choice:
            p1.addPoints(steal_points)
            p2.addPoints(0)

        else:
            p1.addPoints(fight_points)
            p2.addPoints(fight_points)

    print(p1_choices)
    print(p2_choices)
    print("Simulation finished! P1: " + str(p1.points)+ " P2: "+str(p2.points))

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    print("Starting simulation!")
    p1 = importlib.import_module(args[0].split('.')[0])
    p2 = importlib.import_module(args[1].split('.')[0])

    runSimulation(p1, p2);



if __name__ =='__main__':
    main();
    
