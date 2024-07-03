import random

# Defining classes

class Room():
    def __init__(self, code, breach, name, description, item, adjacent):
        self.breach = breach
        self.name = name
        self.desc = description
        self.item = item
        self.adj = adjacent
        self.code = code

    def roomfinder(self, keycode):
        match keycode: # Ignore this it's really bad, it's a wall of code. "It's a sin" - Pet Shop Boys
            case 0:
                return ExampleRoom
            case 1:
                return RoomOne
            case 2:
                return RoomTwo
            case 3:
                return RoomThree
            case 4:
                return RoomFour
            case 5:
                return RoomFive
            case 6:
                return RoomSix
            case 7:
                return RoomSeven
            case 8:
                return RoomEight
            case 9:
                return RoomNine
            case 10:
                return RoomTen
            case 11:
                return RoomEleven
            case 12:
                return RoomTwelve
            case 13:
                return RoomThirteen
            case 14:
                return RoomFourteen
            case 15:
                return RoomFifteen
            case 16:
                return RoomSixteen
            case 17:
                return RoomSeventeen
            case 18:
                return RoomEighteen
            case 19:
                return RoomNineteen
            case 20:
                return RoomTwenty
            case _:
                print('failed to identify room')
                return None

class Character():
    def __init__(self, position, description):
        self.pos = position
        self.desc = description
       
class Player(Character):
    def __init__(self, position, inventory, description, alive):
        Character.__init__(self, position, description)
        self.inv = inventory
        self.alive = alive

    def pickup(self, monster): # This is to pickup items for a room
        x = ExampleRoom.roomfinder(self.pos)
        if x.item == None:
            print('You look around, but there doesn\'t appear to be anything here. You\'re wasting time.')
        else:
            if x.item == 'DeBris':
                if 'Cheese touch' in self.inv:
                    print('Looking down, you spot something on the floor... Oh no... not again...')
            if x.item == 'Energy cell':
                print('Out of the corner of your eye, you spot a faint glow from behind a vent, and notice an energy cell.\nYou try and pry the vent cover open, but it resists your tugs. With one huge heave and the scream of warping metal, you tear it off.\nYou\'ve got it, but a roar from the depths of the ship lets you know that your victory hasn\'t gone unnoticed.')
                monster.dest = self.pos
                monster.awake = True
            if x.item == 'Override key':
                print('You crane your neck to see over the shelf, and spy what looks like the override key for the escape pods, judging by the label.\nYou jump to pick it up, but while you\'re grabbing it, you knock a paint can over, starting a cascade.\nYou hear running footsteps start to get closer to you. You might want to get out of here.')
                monster.dest = self.pos
                monster.awake = True
            print('Picked up', x.item)
            self.inv.add(x.item)
            x.item = None
     
    def move(self, to): # This is to move to another room
        if int(to) in ExampleRoom.roomfinder(self.pos).adj:
            self.pos = int(to) # Rooms have a number code
            moved = True
        else:
            moved = False
    
    def triggercheck(self, monster, sec1, sec2):
        if ExampleRoom.roomfinder(self.pos).breach == True:
            print('As soon as the door opens, you are sucked through it into the next room, and your body is lifelessly thrown into space throught the gaping hole in the hull.\nLuckily, you don\'t have to experience the air being pulled from your lungs as your blood boils and your vital organs freeze one by one.\nYou are dead.')
            self.alive = False
        if monster.pos == self.pos:
            print('A noise overhead and a drop of liquid on your scalp makes you look up. You barely get to start moving your head before a hideous monster grabs you.\nYou spend your last moments wondering how you taste.\nYou are dead.')
            self.alive = False
        if sec1.pos == self.pos:
            print('A security robot is hurtling towards you! Sparks are flying from exposed wires in its armour, it seems to be malfunctioning.\n"THREAT DETECTED" you hear, as it barrels towards you. You close your eyes, preparing for the worst, and you feel a pressure on your stomach as your thoughts go fuzzy and you pass out.\nYou wake up somewhere new, surprised to be alive and relatively unharmed.')

    def invcheck(self): # This is to check what items the player has and show them
        if 'Mouldy cheese' in self.inv:
            print('You reach into your pocket and feel something gross. You quickly withdraw your hand, but the disgusting piece of mouldy, rotted cheese sticks to your fingers. You shake it off. Ew. Now your hand smells like cheese.\nCheese touch acquired.')
            self.inv.remove('Mouldy cheese')
            self.inv.add('Cheese touch')
        print('You reach into your pocket and rummage around. You see what you pulled out:')
        for item in self.inv:
            print(item)

class Monster(Character):
    def __init__(self, position, destination, awake, description):
        Character.__init__(self, position, description)
        self.dest = destination
        self.awake = awake

    def move(self): # Pathfinding! (Nested if statements meh but it's efficient since the path is so simple) Resetting destination after reaching it doesn't work right now.
        if self.pos == self.dest:
                self.dest = None
        if self.dest == None:
            self.dest = random.randint(1, 20)
        if self.dest in (ExampleRoom.roomfinder(self.pos)).adj: # If destination is one room away, go there
            self.pos = self.dest
        else:
            nextmove3, nextmove4, nextmove5 = None, None, None
            for x in (ExampleRoom.roomfinder(self.pos)).adj:
                for y in (ExampleRoom.roomfinder(x)).adj: # If destination is adjacent to adjacent room, go to that near room
                    if self.dest == y: 
                        self.pos = x
                        return
                    else:
                        for z in (ExampleRoom.roomfinder(y)).adj:
                            if self.dest == z:
                                nextmove3 = x
                                break
                            else:
                                for a in (ExampleRoom.roomfinder(z)).adj:
                                    if nextmove3 != None:
                                        break
                                    if self.dest == a:
                                        nextmove4 = x
                                        break
                                    else:
                                        for b in (ExampleRoom.roomfinder(a)).adj:
                                            if nextmove4 != None:
                                                break
                                            if self.dest == b:
                                                nextmove5 = x
                                                break
            if nextmove3 != None:
                self.pos = nextmove3
            elif nextmove4 != None:
                self.pos = nextmove4
            else:
                self.pos = nextmove5

class SecBot(Character):
    def __init__(self, position, destination, description):
        Character.__init__(self, position, description)
        self.dest = destination

    def move(self):
        y = 3
        for x in ExampleRoom.roomfinder(self.pos).adj:
            self.pos = x
            if random.randint(1, y) == 1:
                break
            y = y - 1


# Debugging Example Objects

ExampleCharacter = Character(0, 'Example desc')
ExampleMonster = Monster(1, None, True, 'Example desc')
ExampleSecBot = SecBot(0, 13, 'Example desc')
ExampleRoom = Room(0, False, 'Example room', 'Example desc', 'Cheese touch', {1, 2, 3}) # CHEESE TOUCH
ExamplePlayer = Player(0, set({}), 'Example desc', True)

# Game Objects

RoomOne = Room(1, False, 'Cafeteria', 'Description placeholder', None, {2, 5, 8})
RoomTwo = Room(2, False, 'Ruined room', 'Description placeholder', None, {1, 3, 10})
RoomThree = Room(3, False, 'Pointless pipe corridor', 'Seemingly pointless backway full of pipes leaking steam', None, {2, 4, 12})
RoomFour = Room(4, False, 'Living quarters', 'Description placeholder', None, {3, 5, 14})
RoomFive = Room(5, False, 'Idea room', 'Description placeholder', None, {1, 4, 6})
RoomSix = Room(6,  False, 'Airlock', 'Description placeholder', None, {5, 7, 15})
RoomSeven = Room(7, False, 'Barracks', 'Description placeholder', None, {6, 8, 17})
RoomEight = Room(8, False, 'Procrastination room', 'Description placeholder', None, {1, 7, 9})
RoomNine = Room(9, False, 'Caboose', 'Description placeholder', None, {8, 10, 18})
RoomTen = Room(10, False, '', 'Description placeholder', None, {2, 9, 11})
RoomEleven = Room(11, False, 'Storage', 'Description placeholder', None, {10, 12, 19})
RoomTwelve = Room(12, False, 'Office', 'Description placeholder', None, {3, 11, 13})
RoomThirteen = Room(13, False, 'Escape pod bay', 'Description placeholder', None, {12, 14, 20})
RoomFourteen = Room(14, False, 'Cheese factory', 'Description placeholder', 'DeBrie', {4, 13, 15})
RoomFifteen = Room(15, False, 'Grand hallway', 'Description placeholder', None, {6, 14, 16})
RoomSixteen = Room(16, False, 'Server room', 'Description placeholder', None, {15, 17, 20})
RoomSeventeen = Room(17, False, 'Office', 'Description placeholder', None, {7, 16, 18})
RoomEighteen = Room(18, False, 'Medical bay', 'Description placeholder', None, {9, 17, 19})
RoomNineteen = Room(19, False, 'Conference room', 'Description placeholder', None, {11, 18, 20})
RoomTwenty = Room(20, False, 'Bridge', 'You have found your way to the bridge, the central command centre of the ship. A vast and sterile room, once bustling with activity, now swaddles your footsteps with deafening silence.', None, {13, 16, 19})

def forcemonstermove(): # Test and debug
    ExampleMonster.move()
    print('Destination is: ' + str(ExampleMonster.dest))
    print('Position is: ' + str(ExampleMonster.pos))

moved = True

# Main

def main():
    playername = input('Enter name: ')
    takenrooms = set({13})
    realplayer = Player(random.randint(1, 20), set({'Mouldy cheese'}), 'This is you, '+playername, True) # Creating player
    takenrooms.add(realplayer.pos)
    variable = random.randint(1, 20) 
    while variable in takenrooms: # Making random variables to place enemies and hazards but not on top of the player
        variable = random.randint(1, 20)
    realmonster = Monster(variable, None, False, 'This is the monster') # Creating monster
    takenrooms.add(variable)
    while variable in takenrooms:
        variable = random.randint(1, 20)
    securityrobotone = SecBot(variable, random.randint(1, 10), 'This is the first security robot') # Creating robots
    takenrooms.add(variable)
    while variable in takenrooms:
        variable = random.randint(1, 20)
    securityrobottwo = SecBot(variable, random.randint(11, 20), 'This is the second security robot')
    takenrooms.add(variable)
    while variable in takenrooms:
        variable = random.randint(1, 20)
    ExampleRoom.roomfinder(variable).breach = True # Creating hull breaches
    takenrooms.add(variable)
    while variable in takenrooms:
        variable = random.randint(1, 20)
    ExampleRoom.roomfinder(variable).breach = True
    takenrooms.add(variable)
    while variable in takenrooms:
        variable = random.randint(1, 20)
    ExampleRoom.roomfinder(variable).item = 'Override key' # Creating items
    takenrooms.add(variable)
    while variable in takenrooms:
        variable = random.randint(1, 20)
    ExampleRoom.roomfinder(variable).item = 'Energy cell'
    print('A ruined spacecraft, drifting through the dark, illuminated by fires behind glass, and riddled with holes.\nInside, a survivor blinks their eyes open, and pushes against the wall, slowly making their way up to standing.\nThis is you. And you have to escape.')
    print('"I have to get to the escape pods! Hopefully they aren\'t destroyed. Let\'s see which rooms I can move to..."')
    while True:
        print('Current position: '+str(realplayer.pos()))
        for x in ExampleRoom.roomfinder(realplayer.pos).adj:
            if ExampleRoom.roomfinder(x).breach == True:
                adjbreach = True
        if adjbreach == True:
            print('"I feel a chill and hear a rush of air."')
            adjbreach = False
        if securityrobotone.pos in ExampleRoom.roomfinder(realplayer.pos).adj:
            print('"I hear sparks and whirring motors."')
        elif securityrobottwo.pos in ExampleRoom.roomfinder(realplayer.pos).adj:
            print('"I hear sparks and whirring motors."')
        if realmonster in ExampleRoom.roomfinder(realplayer.pos).adj:
            print('"I hear distant footsteps from the vents."')
            if random.randint(1,2) == 1:
                print('The footsteps stop suddenly, and you can hear a low growl.')
                realmonster.dest = realplayer.pos
        print('"I see signs on the walls, I think I can get to these rooms:')
        for x in ExampleRoom.roomfinder(realplayer.pos).adj:
            print(str(x))
        if ExampleRoom.roomfinder(realplayer.pos).item == 'Energy cell':
            print('"Is that something in the vent..?"')
        if ExampleRoom.roomfinder(realplayer.pos).item == 'Override key':
            print('"Something is glinting up on that shelf."')
        print('What will you do? [tip: type "help"]')
        inpt = input('')
        match inpt.lower():
            case 'help':
                print('commands list') # Finish this please
                input('Press enter to continue ')
                continue
            case 'move':
                x = input('Where? ') # Working on this
                if x == 'help':
                    print('commands list') # Finish this please
                    input('Press enter to continue ')
                    continue
                else:
                    try:
                        int(x)
                    except:
                        print('Invalid input')
                        continue
                    realplayer.move(x)
                    if moved == False:
                        print('"I can\'t get to that room from here."')
                        continue
            case 'inventory':
                realplayer.invcheck()
            case 'wait':
                print('"I don\'t feel safe to move. I\'ll wait"')
            case 'pickup':
                realplayer.pickup(realmonster)
        # Make monster move etc
        
        realmonster.move()
                





print('breakpoint')