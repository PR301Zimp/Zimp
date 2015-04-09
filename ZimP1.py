from zimpDataInit import *
from FileManager import *
import random

DOOR = OPEN = True
BLOCKED = HEDGE = False
NO_MESSAGE = ''
START_TIME = '21:00'
GAME_NAME = 'Zombie on my Screen'
FILE_NAME = "ZIMPsave.db"

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
        
    def rotateTile(self, direction):
        pass
    
    def breakOut(self):
        pass
        

class IndoorTile(Tile):
    pass

class OutdoorTile(Tile):
    pass

class Player(object):
    def __init__(self, name = "New Player", item1 = None, item2 = None, x = 0, y = 0, health = 6, totem=False):
        self.name = name
        self.item1 = item1
        self.item2 = item2
        self.x = x
        self.y = y
        self.health = health
        self.totem = totem

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
        self.allItems = {}
        self.player = Player()
        self.turn = None 
        
    def saveGame(self, name):
        fileManager = FileManager(FILE_NAME)
        fileManager.saveGame([self.allIndoorTiles, self.allOutDoorTiles, self.time, self.actionCards, self.actionCardsCurrent, self.map, self.allItems, self.player, self.turn], name)
    
    def loadGame(self, saveName):
        """
        >>> loadGame("save 5")
        False
        """
        fileManager = FileManager(FILE_NAME)
        data = fileManager.loadGame(saveName)
        if (data == "KeyError"):
            #print "Save does not Exist"
            return False
        else:
            self.allIndoorTiles = data[0]
            self.allOutDoorTiles = data[1]
            self.time = data[2]
            self.actionCards = data[3]
            self.actionCardsCurrent = data[4]
            self.map = data[5]
            self.allItems = data[6]
            self.player = data[7]
            self.turn = data[8] 
            return True
        
    def clearSaves(self):
         fileManager = FileManager(FILE_NAME)
         fileManager.clearSaves()
        
    
    def viewSavedGames(self):
        fileManager = FileManager(FILE_NAME)
        data = fileManager.savedGames()
        return data
    
    def delSave(self, saveName):
        fileManager = FileManager(FILE_NAME)
        data = fileManager.delSave(saveName)        

    def resetPlayer(self, name = 'Innocent Victim',  health = 6):
        self.player = Player(name=name, health=health)

    def addTile(self,  type, name, north, east, south, west, message):
        if(type == IndoorTile):
            self.allIndoorTiles[name] = IndoorTile(name, north, east, south, west, message)
        elif(type == OutdoorTile):
            self.allOutDoorTiles[name] = OutdoorTile(name, north, east, south, west, message)

    def setStartTile(self,  name ):
        pass
    def setTileAside(self,  name):
        pass
    def addItem(self,  name , damage, message, uses):
        self.allItems[name] = Item(name, damage, message, uses)
    def addMessage(self, message, timeWasted):
        pass
    def addActionCard(self, item, msgNine, msgTen, msgEleven):
        self.actionCards.append(ActionCard(item, msgNine, msgTen, msgEleven))
        
    def shuffleCards(self):
        cards = self.actionCards
        cards.pop(random.randrange(0,9+1))
        cards.pop(random.randrange(0,8+1))
        self.actionCardsCurrent = cards
        
        
    def drawCard(self):
        pass
    
    def addCard(self):
        pass
    
    def newGame(self):
        pass
    
    def movePlayer(self):
        pass
    
    def waitHeal(self):
        pass
    
    def runAway(self):
        pass
    
    def searchTotem(self):
        pass
    
    def buryTotem(self):
        pass
    


def main():
    deleteAll()
    game = Game( GAME_NAME, START_TIME )
    game.resetPlayer( 'Innocent Victim', 6 )
    
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
    game.addItem( 'Machette', 3, "not sure", -1)
    game.addItem( 'Grisly Femur', 2, "not sure", -1)
    game.addItem( 'Golf Club', 2, "not sure", -1)
    game.addItem( 'Chainsaw', 2, "not sure", -1)
    game.addItem( 'Can of Soda', None, "not sure", 1)
    game.addItem( 'Candle', None, "not sure", 1)
    
    game.addActionCard(game.allItems['Oil'], ( 'You try hard not to wet yourself', 0 ), 'item', 6)
    game.addActionCard(game.allItems['Gasoline'], 4, ( 'You sense your impending doom',  -1 ), 'item')
    game.addActionCard(game.allItems['Board with Nails'], 'item', 4, ( 'Something icky in your mouth', -1 ))
    game.addActionCard(game.allItems['Machette'], 4, ( 'A bat poops in your eye', -1 ), 6)
    game.addActionCard(game.allItems['Grisly Femur'], 'item', 5, ( 'Your sould is not wanted here', -1 ))
    game.addActionCard(game.allItems['Golf Club'], ( 'Slip on nasty goo', -1 ), 4, ( 'The smell of blood is in the air', 0 ))  
    game.addActionCard(game.allItems['Chainsaw'], 3, ( 'you hear terrible screams', 0 ), 5)
    game.addActionCard(game.allItems['Can of Soda'], ( 'Candy bar in your pocket', +1 ), 'item', 4)
    game.addActionCard(game.allItems['Candle'], ( 'Your body shivers involuntarily', 0 ), ( 'You feel a spark of hope', +1 ), 4)
    
    
    game.shuffleCards()
    #print(game.player.name)
    #game.resetPlayer("Scott", 9)
    #game.saveGame("Save 2|")
    #print game.viewSavedGames()
    #print(game.player.name)
    #game.resetPlayer()
    #print(game.player.name)
    #print game.loadGame("save 5")
    #print(game.player.name)
    #game.delSave("Save 2|")
    #print game.viewSavedGames()
    #game.clearSaves()
    #print game.viewSavedGames()

if __name__ == '__main__':
    main()
