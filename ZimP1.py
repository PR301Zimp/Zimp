DOOR = OPEN = True
BLOCKED = HEDGE = False
NO_MESSAGE = ''

def deleteAll():
    pass
def displayAll():
    pass

class Tile(object):
    def __init__(self, name, north, east, south, west, message):
        self.Name = name
        self.North = north
        self.East = east
        self.South = south
        self.West = west
        self.Message = message

class IndoorTile(Tile):
    pass

class OutdoorTile(Tile):
    pass

class Player(object):
    def __init__(self, item1 = None, item2 = None, x = 0, y = 0, health = 6, totem=False):
        self.item1 = None
        self.item2 = None
        self.x = 0
        self.y = 0
        self.health = 6
        self.totem = False

    def getLoc(self):
        return self.x,self.y


class Item(object):
    def __init__(self, name, damage, message, uses):
        self.name = name
        self.damage = damage
        self.message = message
        self.uses = uses

class ActionCard(object):
    def __init__(self, item, msgNine, msgTen, msgEleven):
        self.item = item
        self.msgNine = msgNine
        self.msgTen = msgTen
        self.msgEleven = msgEleven

class Game(object):
    def __init__(self, title, time):
        self.allIndoorTiles = {}
        self.allOutDoorTiles = {}
        self.time = 9.00
        self.actionCards = []
        self.actionCardsCurrent = []
        self.map = {}


    def resetPlayer(self, name, attack, health):
        pass

    def addTile(self,  type, name, north, east, south, west, message):
        if(type == IndoorTile):
            inDoorTemp = IndoorTile(name, north, east, south, west, message)
            self.allIndoorTiles[name] = inDoorTemp
        elif(type == OutdoorTile):
            outDoorTemp = OutdoorTile(name, north, east, south, west, message)
            self.allIndoorTiles[name] = outDoorTemp

    def setStartTile(self,  name ):
        pass
    def setTileAside(self,  name):
        pass
    def addItem(self,  name , damage, message, uses):
        pass
    def addMessage(self, message, timeWasted):
        pass

def main():
    deleteAll()
    game = Game( 'Zombie on my Screen', '21:00' )
    game.resetPlayer( 'Innocent Victim', 1, 6 )
    # indoors
    game.addTile( IndoorTile, 'Bathroom', DOOR, BLOCKED, BLOCKED, BLOCKED, NO_MESSAGE )
    game.addTile( IndoorTile, 'Kitchen', DOOR, DOOR, BLOCKED, DOOR, '+1 health if end move here' )
    game.addTile( IndoorTile, 'Storage', DOOR, BLOCKED, BLOCKED, BLOCKED, 'may search for an item here' )
    game.addTile( IndoorTile, 'Evil Temple', BLOCKED, DOOR, BLOCKED, DOOR, 'can search for the totem here')
    game.addTile( IndoorTile, 'Family Room', DOOR, DOOR, BLOCKED, DOOR, NO_MESSAGE )
    game.addTile( IndoorTile, 'Dining Room', DOOR, DOOR, DOOR, DOOR, NO_MESSAGE )
    game.addTile( IndoorTile, 'Bedroom', DOOR, BLOCKED, BLOCKED, DOOR, NO_MESSAGE )
    game.addTile( IndoorTile, 'Foyer', DOOR, BLOCKED, BLOCKED, BLOCKED, NO_MESSAGE )
    #outdoors
    game.addTile( OutdoorTile, 'Garden', HEDGE, OPEN, OPEN, OPEN, '+1 Health of end turn here' )
    game.addTile( OutdoorTile, 'Sitting Area', HEDGE, OPEN, OPEN, OPEN, NO_MESSAGE )
    game.addTile( OutdoorTile, 'Yard01', HEDGE, OPEN, OPEN, OPEN, NO_MESSAGE )
    game.addTile( OutdoorTile, 'Graveyard', HEDGE, OPEN, OPEN, HEDGE, 'Can bury the totem here' )
    game.addTile( OutdoorTile, 'Garage', HEDGE, HEDGE, OPEN, OPEN, NO_MESSAGE )
    game.addTile( OutdoorTile, 'Patio', DOOR, OPEN, OPEN, HEDGE, NO_MESSAGE )
    game.addTile( OutdoorTile, 'Yard02', HEDGE, OPEN, OPEN, OPEN, NO_MESSAGE )
    game.addTile( OutdoorTile, 'Yard03', HEDGE, OPEN, OPEN, OPEN, NO_MESSAGE )

    game.setStartTile( 'Foyer' )
    game.setTileAside( 'Patio' )

    game.addItem( 'Oil' , None, "not sure", 1)
    game.addItem( 'Gasoline', None, "not sure", 1)
    game.addItem( 'Board with Nails', 2, "not sure", -1)
    game.addItem( 'Machete', 3, "not sure", -1)
    game.addItem( 'Grisly Femur', 2, "not sure", -1)
    game.addItem( 'Golf Club', 2, "not sure", -1)
    game.addItem( 'Chainsaw', 2, "not sure", -1)
    game.addItem( 'Can of Soda', None, "not sure", 1)
    game.addItem( 'Candle', None, "not sure", 1)

    game.addMessage( 'You try hard not to wet yourself', 0 )
    game.addMessage( 'You sense your impending doom',  -1 )
    game.addMessage( 'Something icky in your mouth', -1 )
    game.addMessage( 'A bat poops in your eye', -1 )
    game.addMessage( 'Your sould is not wanted here', -1 )
    game.addMessage( 'Slip on nasty goo', -1 )
    game.addMessage( 'The smell of blood is in the air', 0 )
    game.addMessage( 'you hear terrible screams', 0 )
    game.addMessage( 'Candy bar in your pocket', +1 )
    game.addMessage( 'Your body shivers involuntarily', 0 )
    game.addMessage( 'You feel a spark of hope', +1 )

    displayAll()



if __name__ == '__main__':
    main()
