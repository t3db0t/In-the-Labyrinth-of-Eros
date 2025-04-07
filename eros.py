import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

class Room:
    "Stores data for individual rooms"
    
    description = 'Default Room Description'
    #cont = {'line':''}
    destinations = {}

    def __init__(self, roomNumber):
        self.roomNumber = roomNumber

    def enter(self):
        if(self.roomNumber not in visited):
            visited.append(self.roomNumber)
        
        print(f"You've entered Room No. {self.roomNumber}")
        if(self.roomNumber == easterEggRoom):
            print("It is pitch black. You are likely to be eaten by a grue.")
        #print(self.description)
        #print("\n", self.cont['line'], "\n")
            
        print(f"\n{bcolors.OKGREEN}{self.line}{bcolors.ENDC}\n")

        if((self.roomNumber == 12 and 13 in visited) or (self.roomNumber == 13 and 12 in visited)):
            theEnd()
            #print("The End.")
        else:
            self.printDestinations()
            self.prompt()

    def printDestinations(self):
        print("Destinations:")
        for which in self.destinations:
            print(which, end=' ')
        print()
    
    def prompt(self):
        goodToGo = 0
        while(not goodToGo):
            result = input('--> ')
            result = result.upper().split(' ')
            if(result[0] == 'GO' and result[1] in self.destinations):
                if(self.destinations[result[1]] in visited):
                   print("You were already in that room... try another destination.")
                   print("If you definitely absolutely want to go that way, try 'force.'")
                   continue
                else:
                   goodToGo = 1
                   self.goToRoom(self.destinations[result[1]])
            elif(result[0] == 'FORCE' and result[1] in self.destinations):
                goodToGo = 1
                self.goToRoom(self.destinations[result[1]])
            elif(result[0] == 'QUIT'):
                print("Quitter!")
                break
            elif(result[0] == 'LOOK'):
                self.printDestinations()
                continue
            else:
                print("Command unknown. Try 'go' with a destination!")
                continue
                #self.prompt()

    def goToRoom(self, where):
        #print("Going to Room #", where)
        rooms[where].enter()

def theEnd():
    print("The End.")
    print("\nYou visited these rooms:")
    print(visited)
    print(f"The easter egg was in Room No. {easterEggRoom}")

rooms = []
visited = []

easterEggRoom = random.randint(0, 13)

for i in range(14):
    rooms.append(Room(i))

rooms[13].destinations = {'W':12}
rooms[12].destinations = {'E':13}
rooms[11].destinations = {'W':9, 'S':10}
rooms[10].destinations = {'SW':12, 'SE':13, 'NW':9, 'NE':11, 'LADDER':4}
rooms[9].destinations  = {'E':11, 'S':10}
rooms[8].destinations  = {'SW':9, 'DOWN':10, 'SE':11}
rooms[7].destinations  = {'SW':12, 'SE':13, 'NW':5, 'NE':6, 'LADDER':8}
rooms[6].destinations  = {'S':7, 'W':5}
rooms[5].destinations  = {'S':7, 'E':6}
rooms[4].destinations  = {'SW':5, 'SE':6, 'DOWN':7}
rooms[3].destinations  = {'S':2, 'W':1}
rooms[2].destinations  = {'SW':4, 'SE':8, 'NW':1, 'NE':3}
rooms[1].destinations  = {'E':3, 'S':2}
rooms[0].destinations  = {'SW':1, 'S':2, 'SE':3}

rooms[0].line  = "When we had opened all the doors"
rooms[1].line  = "When we had broken every window"
rooms[2].line  = "The vesper-bells had rattled like the floors"
rooms[3].line  = "And the dust had settled on the lintel"
rooms[4].line  = "When we first met the image of the other"
rooms[5].line  = "And the mirrors danced so brightly"
rooms[6].line  = "The crows had fled the gables nightly"
rooms[7].line  = "And the love between the seedling was the mother of the moon"
rooms[8].line  = "The house had crumbled from the rust"
rooms[9].line  = "And the silence grew in anger"
rooms[10].line = "As the host redoubled with a clangor"
rooms[11].line = "And our trust had all the force of a typhoon"
rooms[12].line = "And in the Labyrinth of Eros, a time became a turning"
rooms[13].line = "For the blankness in the sky was a fire, and a yearning"

rooms[0].enter()
