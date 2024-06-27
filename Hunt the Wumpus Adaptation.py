import random

# Defining classes

class Room():
    def __init__(self, code, robot, breach, name, description, item, adjacent):
        self.robot = robot
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
    def __init__(self, position, inventory, description):
        Character.__init__(self, position, description)
        self.inv = inventory

    def pickup(self): # This is to pickup items for a room
        x = ExampleRoom.roomfinder(self.pos)
        if x.item == None:
            print('Nothing in inventory')
        else:
            print('Picked up', x.item)
            self.inv.add(x.item)
            x.item = None

            
    def move(self, to): # This is to move to another room
        # Maybe check if valid?
        self.pos = int(to) # Rooms have a number code

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
        for x in ExampleRoom.roomfinder(self.pos).adj:
            self.pos = x

# Debugging Example Objects

ExampleCharacter = Character(0, 'Example desc')
ExampleMonster = Monster(1, None, True, 'Example desc')
ExampleSecBot = SecBot(0, 13, 'Example desc')
ExampleRoom = Room(0, False, False, 'Example room', 'Example desc', 'Cheese touch', {1, 2, 3}) # CHEESE TOUCH
ExamplePlayer = Player(0, set({}), 'Example desc')

# Game Objects

RoomOne = Room(1, False, False, 'Cafeteria', 'Description placeholder', None, {2, 5, 8})
RoomTwo = Room(2, False, False, 'Ruined room', 'Description placeholder', None, {1, 3, 10})
RoomThree = Room(3, False, False, 'Pipe corridor', 'Seemingly pointless backway full of pipes leaking steam', None, {2, 4, 12})
RoomFour = Room(4, False, False, 'Living quarters', 'Description placeholder', None, {3, 5, 14})
RoomFive = Room(5, False, False, 'Idea room', 'Description placeholder', None, {1, 4, 6})
RoomSix = Room(6, False, False, 'Airlock', 'Description placeholder', None, {5, 7, 15})
RoomSeven = Room(7, False, False, 'Barracks', 'Description placeholder', None, {6, 8, 17})
RoomEight = Room(8, False, False, 'Procrastination room', 'Description placeholder', None, {1, 7, 9})
RoomNine = Room(9, False, False, 'Caboose', 'Description placeholder', None, {8, 10, 18})
RoomTen = Room(10, False, False, '', 'Description placeholder', None, {2, 9, 11})
RoomEleven = Room(11, False, False, 'Storage', 'Description placeholder', None, {10, 12, 19})
RoomTwelve = Room(12, False, False, 'Office', 'Description placeholder', None, {3, 11, 13})
RoomThirteen = Room(13, False, False, 'Escape pod bay', 'Description placeholder', None, {12, 14, 20})
RoomFourteen = Room(14, False, False, 'Cheese factory', 'Description placeholder', 'DeBrie', {4, 13, 15})
RoomFifteen = Room(15, False, False, 'Grand hallway', 'Description placeholder', None, {6, 14, 16})
RoomSixteen = Room(16, False, False, 'Server room', 'Description placeholder', None, {15, 17, 20})
RoomSeventeen = Room(17, False, False, 'Office', 'Description placeholder', None, {7, 16, 18})
RoomEighteen = Room(18, False, False, 'Medical bay', 'Description placeholder', None, {9, 17, 19})
RoomNineteen = Room(19, False, False, 'Conference room', 'Description placeholder', None, {11, 18, 20})
RoomTwenty = Room(20, False, False, 'Bridge', 'You have found your way to the bridge, the central command centre of the ship. A vast and sterile room, once bustling with activity, now swaddles your footsteps with deafening silence.', None, [13, 16, 19])

def forcemonstermove(): # Test and debug
    ExampleMonster.move()
    print('Destination is: ' + str(ExampleMonster.dest))
    print('Position is: ' + str(ExampleMonster.pos))

# Main

def main():
    realplayer = Player(random.randint(1, 20), set({}), 'This is you')
    variable = random.randint(1, 20)
    while variable == realplayer.pos:
        variable = random.randint(1, 20)
    
    

print('breakpoint')

