import random
import os
import time

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
    def __init__(self, position, destination):
        self.pos = position
        self.dest = destination
       
class Player(Character):
    def __init__(self, position, inventory, alive, cellused, keyused, seenpods, escaped, moved, destination):
        Character.__init__(self, position, destination)
        self.inv = inventory
        self.alive = alive
        self.cell = cellused
        self.key = keyused
        self.pods = seenpods
        self.esc = escaped
        self.moved = moved

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
            self.moved = True
        else:
            self.moved = False
    
    def triggercheck(self, monster, sec1, sec2):
        if ExampleRoom.roomfinder(self.pos).breach == True:
            clear()
            print('As soon as the door opens, you are sucked through it into the next room, and your body is lifelessly thrown into space throught the gaping hole in the hull.\nLuckily, you don\'t have to experience the air being pulled from your lungs as your blood boils and your vital organs freeze one by one.\nYou are dead.')
            self.alive = False
            return
        if monster.pos == self.pos:
            clear()
            print('A noise overhead and a drop of liquid on your scalp makes you look up. You barely get to start moving your head before a hideous monster grabs you.\nYou spend your last moments wondering how you taste.\nYou are dead.')
            self.alive = False
        if sec1.pos == self.pos:
            print('A security robot is hurtling towards you! Sparks are flying from exposed wires in its armour, it seems to be malfunctioning.\n"THREAT DETECTED" you hear, as it barrels towards you. You close your eyes, preparing for the worst, and you feel a pressure on your stomach as your thoughts go fuzzy and you pass out.\nYou wake up somewhere new, surprised to be alive and relatively unharmed.')
            self.pos = sec1.dest
        if sec2.pos == self.pos:
            print('A security robot is hurtling towards you! Sparks are flying from exposed wires in its armour, it seems to be malfunctioning.\n"THREAT DETECTED" you hear, as it barrels towards you. You close your eyes, preparing for the worst, and you feel a pressure on your stomach as your thoughts go fuzzy and you pass out.\nYou wake up somewhere new, surprised to be alive and relatively unharmed.')
            self.pos = sec2.dest

    def invcheck(self): # This is to check what items the player has and show them
        if 'Mouldy cheese' in self.inv:
            print('You reach into your pocket and feel something gross. You quickly withdraw your hand, but the disgusting piece of mouldy, rotted cheese sticks to your fingers. You shake it off. Ew. Now your hand smells like cheese.\nCheese touch acquired.')
            self.inv.remove('Mouldy cheese')
            self.inv.add('Cheese touch')
        print('You take some time to reach into your pocket and rummage around. You see what you pulled out:')
        for item in self.inv:
            print(item)

    def escape(self):
        if self.pos == 13:
            if self.pods == False:
                self.pods = True
                print('You rush to get in an escape pod and get the heck out of this ship. But you cannot. The pods are broken.\n"This is fine, this is fine," you try not to panic, "I can fix the pods, if I just find the right materials."\nLooking more closely, you observe that only one escape pod looks like it isn\'t liable to explode on a whim.\nHowever, you can\'t get inside, since the door power is missing its energy cell, and the access keypad is now a hole full of rainbow spaghetti.')
            if 'Energy cell' in self.inv:
                print('You slot your energy cell into its designated slot in the nearby fusebox. The door power comes back on', end='')
                if self.key == True:
                    print('.')
                elif 'Override key' in self.inv:
                    print('.')
                else:
                    print(', but you still can\'t get through a locked door.')
                self.cell = True
                self.inv.remove('Energy cell')
            if 'Override key' in self.inv:
                if self.cell == False:
                    print('You insert the override key into the keyhole at the top of the door, and it turns jankily, but nothing happens. There still isn\'t any power. Damn. You leave the key though')
                elif self.cell == True:
                    print('You insert the override key into the keyhole at the top of the door, and it turns in the lock like butter as the door squeals open.')
                self.key = True
            if self.key and self.cell == True:
                print('This is it. You clamber into the escape pod, yank down the lever, smash the glass, and slam the button behind it. You hear a roar behind you and turn around to see... the Monster.\nIt lunges towards you, and just in time, the pod door slams shut. You are launched away from the ship, to... freedom?\nHopefully, someone finds and resuces you. You comfort yourself with the thought that anything is better than being on that ship.\nAs if on cue, an explosion tears through its hull, ripping it into even more pieces.\nAdrenaline wears off, and you feel tired. You activate the distress beacon, and '+playername+' slowly drifts off... to sleep...')
                self.escaped = True
            else:
                print('"I can\'t do anything more at the moment, I need to find something to let me in there!"')
        else:
            print('"I\'m not at the escape pod bay yet. I need to get there first.')

class Monster(Character):
    def __init__(self, position, destination):
        Character.__init__(self, position, destination)

    def move(self): # Pathfinding! (Nested if statements meh but it's efficient since the path is so simple) Resetting destination after reaching it doesn't work right now.
        if self.pos == self.dest:
                self.dest = None
        if self.dest == None:
            self.dest = random.randint(1, 20)
        if self.dest in (ExampleRoom.roomfinder(self.pos)).adj: # If destination is one room away, go there
            self.pos = self.dest
        else:
            nextmove3, nextmove4, nextmove5 = None, None, None
            monstermoved = False
            for x in (ExampleRoom.roomfinder(self.pos)).adj:
                for y in (ExampleRoom.roomfinder(x)).adj: # If destination is adjacent to adjacent room, go to that near room
                    if self.dest == y: 
                        self.pos = x
                        monstermoved = True
                        break
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
            if monstermoved == True:
                return
            if nextmove3 != None:
                self.pos = nextmove3
            elif nextmove4 != None:
                self.pos = nextmove4
            else:
                self.pos = nextmove5

class SecBot(Character):
    def __init__(self, position, destination):
        Character.__init__(self, position, destination)

    def move(self, player):
        y = 3
        for x in ExampleRoom.roomfinder(self.pos).adj:
            if x == player.pos:
                break
            self.pos = x
            if random.randint(1, y) == 1:
                break
            y = y - 1


# Example room is not redundant although not used for debugging

ExampleRoom = Room(0, False, 'Example room', 'Example desc', 'Cheese touch', {1, 2, 3}) # CHEESE TOUCH

# Game Objects

RoomOne = Room(1, False, 'The cafeteria', 'This is the cafeteria. Half-eaten meals are scattered all over the floor, but there is no sign of life, or even death, that you see.', None, {2, 5, 8})
RoomTwo = Room(2, False, 'A ruined room', 'This room is ruined. Completely destroyed. You have no idea what is was once used for. Probably for the best.', None, {1, 3, 10})
RoomThree = Room(3, False, 'That pointless pipe corridor', 'You\'ve managed to find that seemingly pointless backway full of pipes leaking steam which is such a hallmark of any media.\n  It\'s so cliche you half expect to get jumpscared by a burst of steam.', None, {2, 4, 12})
RoomFour = Room(4, False, 'Living quarters', 'You are now in some living quarters. Looking past a flipped pool table, you wonder why anyone would disembowel a poor defenceless couch like that.', None, {3, 5, 14})
RoomFive = Room(5, False, 'The idea room', 'Ah, this is the ideas room. People brainstorm things here. You have the idea that you better keep moving.', None, {1, 4, 6})
RoomSix = Room(6,  False, 'An airlock', 'You are currently next to a sketchy looking airlock door.', None, {5, 7, 15})
RoomSeven = Room(7, False, 'The barracks', 'These are the barracks, where soldiers are trained... Wonder where they\'ve gone.', None, {6, 8, 17})
RoomEight = Room(8, False, 'The procrastination room', '[Description placeholder]', None, {1, 7, 9})
RoomNine = Room(9, False, 'The caboose', 'Apparently, a caboose is a place on a ship. You learn something new every day.', None, {8, 10, 18})
RoomTen = Room(10, False, 'A public bathroom', 'Ew. This is a bathroom.', None, {2, 9, 11})
RoomEleven = Room(11, False, 'Storage', 'You look around at the contents of this storage room.', None, {10, 12, 19})
RoomTwelve = Room(12, False, 'An office', 'You step into a drab, boring office.', None, {3, 11, 13})
RoomThirteen = Room(13, False, 'The escape pod bay', 'Yes! This is it! The escape pod bay! Now we just need to get out of here! Come on, let\'s go!', None, {12, 14, 20})
RoomFourteen = Room(14, False, 'The Cheese Factory', 'You are in the most famous part of the ship. A grand, looming, ominous industrial factory, the air thick with the sickening stench of melting cheese.\n  Even while the ship falls apart, the cheese factory still stands, making cheese as ever it does.', 'DeBrie', {4, 13, 15})
RoomFifteen = Room(15, False, 'A grand hallway', 'This... is the biggest, most impressive, grandiose hallway you have ever seen. Why? It\'s just a hallway.', None, {6, 14, 16})
RoomSixteen = Room(16, False, 'The server room', 'Welcome to the server room. On your left, you can see the crushed computers. On the right, you\'ll find a row of burning devices.', None, {15, 17, 20})
RoomSeventeen = Room(17, False, 'An office', 'You step into a drab, boring office.', None, {7, 16, 18})
RoomEighteen = Room(18, False, 'The medical bay', 'You pause, momentarily, to consider healing yourself in the medbay. Alas, no time.', None, {9, 17, 19})
RoomNineteen = Room(19, False, 'A conference room', 'This is where important people dressed in suits talk about this, and display powerpoint presentations of green and red arrows. At least, usually.', None, {11, 18, 20})
RoomTwenty = Room(20, False, 'The bridge', 'You have found your way to the bridge, the central command centre of the ship. A vast and sterile room, once bustling with activity, now swaddles your footsteps with deafening silence.', None, {13, 16, 19})

moved = True
print('Loading self tests...')
if os.name == 'nt':
    clear = lambda : os.system('cls')
else:
    clear = lambda : os.system('clear')
playername = input('Enter name: ')
clear()
rooms = [RoomOne, RoomTwo, RoomThree, RoomFour, RoomFive, RoomSix, RoomSeven, RoomEight, RoomNine, RoomTen, RoomEleven, RoomTwelve, RoomThirteen, RoomFourteen, RoomFifteen, RoomSixteen, RoomSeventeen, RoomEighteen, RoomNineteen, RoomTwenty]
# Main

def main():
    for rume in rooms:
        rume.breach = False
        rume.item = None
    RoomFourteen.item = 'DeBrie'
    takenrooms = set({13, 14})
    realplayer = Player(random.randint(1, 20), set({'Mouldy cheese'}), True, False, False, False, False, False, None) # Creating player
    takenrooms.add(realplayer.pos)
    variable = random.randint(1, 20) 
    while variable in takenrooms: # Making random variables to place enemies and hazards but not on top of the player
        variable = random.randint(1, 20)
    realmonster = Monster(variable, None) # Creating monster
    takenrooms.add(variable)
    while variable in takenrooms:
        variable = random.randint(1, 20)
    securityrobotone = SecBot(variable, random.randint(1, 10)) # Creating robots
    takenrooms.add(variable)
    while variable in takenrooms:
        variable = random.randint(1, 20)
    securityrobottwo = SecBot(variable, random.randint(11, 20))
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
    if True: # doing this so I can collapse it, it's the animation thing
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(3)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '----------------------------------------- . . . -----------------------------------------\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(1)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . _____  --^-^-^-^-^--  _____ . . . . . . . . . .  _____  --^-^-^-^-^--  _____  . . .\n'
        '----- ___________   _   ___________ ----- . . . ----- ___________   _   ___________ -----\n'
        '. . . . . . . . .  ---  . . . . . . . . . . . . . . . . . . . . .  ---  . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(1)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . _________ . . . . . . . . . . . . . . . . . . . _________ . . . . . . . .\n'
        '. _____--------           --------_____ . . . . . _____--------           --------_____ .\n'
        '<                 _____                 > . . . <                 _____                 >\n'
        '.  -----  __    --_____--    __  -----  . . . . .  -----  __    --_____--    __  -----  .\n'
        '. . . . . . . -- _______ -- . . . . . . . . . . . . . . . . . -- _______ -- . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(0.5)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . ____ ----------- ____ . . . . . . . . . . . . . ____ ----------- ____ . . . . .\n'
        '. .__ ---                       ---____ . . . . . ____---                       --- __. .\n'
        '<                _-----_                > . . . <                _-----_                >\n'
        '. ---- __        -__o__-        __ ---- . . . . . ---- __        -__o__-        __ ---- .\n'
        '. . . . . .-- ___       ___ --. . . . . . . . . . . . . . .-- ___       ___ --. . . . . .\n'
        '. . . . . . . . . .---. . . . . . . . . . . . . . . . . . . . . . .---. . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(0.5)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . .  _______  . . . . . . . . . . . . . . . . . . .  _______  . . . . . . . .\n'
        '. . . . __------         ------__ . . . . . . . . . . . __------         ------__ . . . .\n'
        '.   _--                           --_   . . . . .   _--                           --_   .\n'
        '._-                                   -_. . . . ._-                                   -_.\n'
        '<                _ --- _                > . . . <                _ --- _                >\n'
        '. -_            \   O   /            _- . . . . . -_            \   O   /            _- .\n'
        '. . . -__         -----         __- . . . . . . . . . -__         -----         __- . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- . . . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(1)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . .  _______  . . . . . . . . . . . . . . . . . . .  _______  . . . . . . . .\n'
        '. . . . __------         ------__ . . . . . . . . . . . __------         ------__ . . . .\n'
        '.   _--                           --_   . . . . .   _--                           --_   .\n'
        '._-                                   -_. . . . ._-                                   -_.\n'
        '<                _ --- _                > . . . <                _ --- _                >\n'
        '. -_            \   O   /            _- . . . . . -_            \   O   /          o _- .\n'
        '. . . -__         -----         __- . . . . . . . . . -__         -----         __- . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- . . . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(2)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . .  _______  . . . . . . . . . . . . . . . . . . .  _______  . . . . . . . .\n'
        '. . . . __------         ------__ . . . . . . . . . . . __------         ------__ . . . .\n'
        '.   _--                           --_   . . . . .   _--                           --_   .\n'
        '._-                                   -_. . . . ._-                                   -_.\n'
        '<                _ --- _                > . . . <                _ --- _                >\n'
        '. -_            \   O   /            _- . . . . . -_            \   O   /          O _- .\n'
        '. . . -__         -----         __- . . . . . . . . . -__         -----         __- . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- . . . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(2)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . .  _______  . . . . . . . . . . . . . . . . . . .  _______  . . . . . . . .\n'
        '. . . . . __---           ---__ . . . . . . . . . . . . . __---           ---__ . . . . .\n'
        '. ____---                       ---____ . . . . . ____---                       ---____ .\n'
        '<                _ --- _                > . . . <                _ --- _                >\n'
        '. -_             -__o__-             _- . . . . . -_             -__o__-          /\ _- .\n'
        '. . . -__                       __- . . . . . . . . . -__                       _(-_) . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- . . . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(2)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . .   ___  -------  ___   . . . . . . . . . . . . .   ___  -------  ___   . . . . .\n'
        '.  ___   ---                 ---   ___  . . . . .  ___   ---                 ---   ___  .\n'
        '<                                       > . . . <                                       >\n'
        '. -_             _-----_             _- . . . . . -_             _-----_          ^  _- .\n'
        '. . . -__        -__o__-        __- . . . . . . . . . -__        -__o__-        /_- \ . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___--|   * | . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . -___- . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(3)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . .   ___  -------  ___   . . . . . . . . . . . . .   ___  -------  ___   . . . . .\n'
        '.  ___   ---                 ---   ___  . . . . .  ___   ---                 ---   ___  .\n'
        '<                                       > . . . <                                       >\n'
        '. -_             _-----_             _- . . . . . -_             _-----_             _- .\n'
        '. . . -__        -__o__-        __- . . . . . . . . . -__        -__o__-         _^   . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- /   \  . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . .  |   * |  .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . -___- . .\n')
        time.sleep(0.1)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . .   ___  -------  ___   . . . . . . . . . . . . .   ___  -------  ___   . . . . .\n'
        '.  ___   ---                 ---   ___  . . . . .  ___   ---                 ---   ___  .\n'
        '<                                       > . . . <                                       >\n'
        '. -_             _-----_             _- . . . . . -_             _-----_             _- .\n'
        '. . . -__        -__o__-        __- . . . . . . . . . -__        -__o__-         _  . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___--   ^   . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . .   /  *\   .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  |     |  .\n')
        time.sleep(0.1)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . .   ___  -------  ___   . . . . . . . . . . . . .   ___  -------  ___   . . . . .\n'
        '.  ___   ---                 ---   ___  . . . . .  ___   ---                 ---   ___  .\n'
        '<                                       > . . . <                                       >\n'
        '. -_             _-----_             _- . . . . . -_             _-----_             _- .\n'
        '. . . -__        -__o__-        __- . . . . . . . . . -__        -__o__-         _  . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- .   . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . .   ^   . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   /  *\   .\n')
        time.sleep(0.1)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . .  _______  . . . . . . . . . . . . . . . . . . .  _______  . . . . . . . .\n'
        '. . . . . __---           ---__ . . . . . . . . . . . . . __---           ---__ . . . . .\n'
        '. ____---                       ---____ . . . . . ____---                       ---____ .\n'
        '<                _ --- _                > . . . <                _ --- _                >\n'
        '. -_             -__o__-             _- . . . . . -_             -__o__-             _- .\n'
        '. . . -__                       __- . . . . . . . . . -__                       __- . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- . . . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . .   . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   ^   . .\n')
        time.sleep(0.1)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . .  _______  . . . . . . . . . . . . . . . . . . .  _______  . . . . . . . .\n'
        '. . . . . __---           ---__ . . . . . . . . . . . . . __---           ---__ . . . . .\n'
        '. ____---                       ---____ . . . . . ____---                       ---____ .\n'
        '<                _ --- _                > . . . <                _ --- _                >\n'
        '. -_             -__o__-             _- . . . . . -_             -__o__-             _- .\n'
        '. . . -__                       __- . . . . . . . . . -__                       __- . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- . . . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   . . .\n')
        time.sleep(0.1)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . .  _______  . . . . . . . . . . . . . . . . . . .  _______  . . . . . . . .\n'
        '. . . . . __---           ---__ . . . . . . . . . . . . . __---           ---__ . . . . .\n'
        '. ____---                       ---____ . . . . . ____---                       ---____ .\n'
        '<                _ --- _                > . . . <                _ --- _                >\n'
        '. -_             -__o__-             _- . . . . . -_             -__o__-             _- .\n'
        '. . . -__                       __- . . . . . . . . . -__                       __- . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- . . . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(3)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . .  _______  . . . . . . . . . . . . . . . . . . .  _______  . . . . . . . .\n'
        '. . . . . __---           ---__ . . . . . . . . . . . . . __---           ---__ . . . . .\n'
        '. ____---                       ---____ . . . . . ____---                       ---____ .\n'
        '<                                       > . . . <                                       >\n'
        '. -_             _ --- _             _- . . . . . -_             _ --- _             _- .\n'
        '. . . -__        -__o__-        __- . . . . . . . . . -__        -__o__-        __- . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- . . . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(1)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . ____------____  . . . . . . . . . . . . . . . . ____------____  . . . . . .\n'
        '. ____----                     ----____ . . . . . ____----                     ----____ .\n'
        '<                                       > . . . <                                       >\n'
        '. -_             _ --- _             _- . . . . . -_             _ --- _             _- .\n'
        '. . . -__        -__o__-        __- . . . . . . . . . -__        -__o__-        __- . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- . . . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(0.5)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. _______---------     ---------_______ . . . . . _______---------     ---------_______ .\n'
        '<                                       > . . . <                                       >\n'
        '. -_             _ --- _             _- . . . . . -_             _ --- _             _- .\n'
        '. . . -__        -__o__-        __- . . . . . . . . . -__        -__o__-        __- . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- . . . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(0.5)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. _____ . . . . . . . . . . . . . _____ . . . . . _____ . . . . . . . . . . . . . _____ .\n'
        '<         -----___________ -----        > . . . <         -----___________ -----        >\n'
        '. -_             _ --- _             _- . . . . . -_             _ --- _             _- .\n'
        '. . . -__        -__o__-        __- . . . . . . . . . -__        -__o__-        __- . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- . . . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(2)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. _______---------     ---------_______ . . . . . _______---------     ---------_______ .\n'
        '<                                       > . . . <                                       >\n'
        '. -_             _ --- _             _- . . . . . -_             _ --- _             _- .\n'
        '. . . -__        -__o__-        __- . . . . . . . . . -__        -__o__-        __- . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- . . . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(1)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . ____------____  . . . . . . . . . . . . . . . . ____------____  . . . . . .\n'
        '. ____----                     ----____ . . . . . ____----                     ----____ .\n'
        '<                _ --- _                > . . . <                _ --- _                >\n'
        '. -_            \   O   /            _- . . . . . -_            \   O   /            _- .\n'
        '. . . -__         -----         __- . . . . . . . . . -__         -----         __- . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- . . . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(2)
        clear()
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n'
        '. . . . . . . .  _______  . . . . . . . . . . . . . . . . . . .  _______  . . . . . . . .\n'
        '. . . . __------         ------__ . . . . . . . . . . . __------         ------__ . . . .\n'
        '.   _--                           --_   . . . . .   _--                           --_   .\n'
        '._-                ___                -_. . . . ._-                ___                -_.\n'
        '<               /   O   \               > . . . <               /   O   \               >\n'
        '. -_            \ _____ /            _- . . . . . -_            \ _____ /            _- .\n'
        '. . . -__                       __- . . . . . . . . . -__                       __- . . .\n'
        '. . . . . --___           ___-- . . . . . . . . . . . . . --___           ___-- . . . . .\n'
        '. . . . . . . . . ----- . . . . . . . . . . . . . . . . . . . . . ----- . . . . . . . . .\n'
        '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
        time.sleep(5)
    print('A ruined spacecraft, drifting through the dark, illuminated by fires behind glass, and riddled with holes.\nInside, a survivor blinks their eyes open, and pushes against the wall, slowly making their way up to standing.\nTheir name is '+playername+'. This is you. And you have to escape.')
    print('"I have to get to the escape pods! Hopefully they aren\'t destroyed. Let\'s see which rooms I can move to..."\n[Tip: type "help"]')
    while True:
        print('Current position: '+ str(realplayer.pos))
        print('  '+ExampleRoom.roomfinder(realplayer.pos).name)
        print('  '+ExampleRoom.roomfinder(realplayer.pos).desc+'\n')
        adjbreach = False
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
        if realmonster.pos in ExampleRoom.roomfinder(realplayer.pos).adj:
            print('"I hear distant footsteps from the vents."')
            if realmonster.dest == realplayer.pos:
                print('The footsteps stop suddenly, and you can hear a low growl.')
            elif random.randint(1,2) == 1:
                print('The footsteps stop suddenly, and you can hear a low growl.')
                realmonster.dest = realplayer.pos
        print('\n"I see signs on the walls, I think I can get to these rooms:"')
        for x in ExampleRoom.roomfinder(realplayer.pos).adj:
            print(str(x))
        if ExampleRoom.roomfinder(realplayer.pos).item == 'Energy cell':
            print('\n"Is that something in the vent..?"')
        if ExampleRoom.roomfinder(realplayer.pos).item == 'Override key':
            print('\n"Something is glinting up on that shelf."')
        print('\nWhat will you do?')
        inpt = input('')
        match inpt.lower().strip():
            case 'help':
                print('help - shows this list.\nmove - asks you where to move, in the next line type which room you wish to move to.\ninventory - check your inventory. takes time.\nwait - take a little rest.\npickup - look for and pick up items. takes time.\nescape - get in an escape pod and save yourself again.') # Finish this please
                input('Press enter to continue ')
                clear()
                continue
            case 'move':
                x = input('Where? ') 
                if x == 'help':
                    print('help - shows this list.\nmove - asks you where to move, in the next line type which room you wish to move to.\ninventory - check your inventory. takes time.\nwait - take a little rest.\npickup - look for and pick up items. takes time.\nescape - get in an escape pod and save yourself again.') # Finish this please
                    input('Press enter to continue ')
                    clear()
                    continue
                else:
                    try:
                        int(x)
                    except:
                        print('Invalid input')
                        input('Press enter ')
                        clear()
                        continue
                    realplayer.move(x)
                    if realplayer.moved == False:
                        print('"I can\'t get to that room from here."')
                        input('Press enter ')
                        clear()
                        continue
            case 'inventory':
                realplayer.invcheck()
            case 'wait':
                print('"I don\'t feel safe to move. I\'ll wait."')
            case 'pickup':
                realplayer.pickup(realmonster)
            case 'escape':
                realplayer.escape()
                if realplayer.esc == True:
                    time.sleep(20)
                    break
                elif realplayer.esc == False:
                    time.sleep(5)
                    continue
            case _:
                print('Input not understood.\n[Tip: type "help"]')
                input('Press enter ')
                clear()
                continue
        realplayer.triggercheck(realmonster, securityrobotone, securityrobottwo) # This checks if you are dead or the bots get you
        realmonster.move()
        securityrobotone.move(realplayer)
        securityrobottwo.move(realplayer)
        realplayer.triggercheck(realmonster, securityrobotone, securityrobottwo)
        if realplayer.alive == False:
            time.sleep(10)
            break
        input('Press enter ')
        clear()
    clear()
    time.sleep(3)
    print('...drifting through blackness...')
    time.sleep(3)
    clear()
    time.sleep(3)
    return

while True:
    main()