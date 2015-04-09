import shelve
import unittest

class FileManager(object):
    def __init__(self, filePath):
        """
        Given the filepath for the shelve storage
        """
        self.filePath = filePath
        self.data = None

    def savedGames(self):
        """
        savedGames(filepath)
        
        Reads the shelve dictionary at the filepath given. 
        Returns the dictionary keys
        
        """
        try:
            self.data = shelve.open(self.filePath)
            saves = self.data.keys()
            self.data.close()
            return saves            
            
        except:
            print("An error has occured")
            
    def clearSaves(self):
        self.data = shelve.open(self.filePath)
        self.data.clear()
        

    def saveGame(self, state, name):
        """
        saveGame(state, name)
        
        Given the state and name for save will shelve
        the state with the key of the save name.
        """
        self.data = shelve.open(self.filePath)
        try:
            self.data[name] =  state 
        except ValueError:
            print("An error has occured")
        self.data.close()

    def loadGame(self, save):
        """
        loadGame(save)
        Given the 
        >>> loadGame("save 5")
        "KeyError"
        """
        self.data = shelve.open(self.filePath)
        try:
            return self.data[save]
        except KeyError:
            return "KeyError"     
        self.data.close()
    
    def delSave(self, save):
        self.data = shelve.open(self.filePath)
        try:
            del self.data[save]
            return 0
        except KeyError:
            return "KeyError"            
        
        
#class unitTestCase(unittest.TestCase):
    #def setUp(self):
        #self.filepath = "ZIMPsave.db"
        #self.fileMan = FileManager("ZIMPsave.db")
        
    #def test_saveGame(self):
        #self.fileMan.saveGame("data 1", "Test 1")
        #self.fileMan.saveGame("data 2", "Test 2")
        #data = self.fileMan.savedGames()
        #self.assertEquals(data[1], "Test 1")   
        
        
    #def test_loadGame(self):
        #self.fileMan.saveGame("data 1", "Test 1")
        #self.fileMan.saveGame("data 2", "Test 2")        
        #data = self.fileMan.loadGame("Test 1")
        #self.assertEquals(data, "data 1")
        
    #def test_delSave(self):
        #self.fileMan.saveGame("data 1", "Test 1")
        #self.fileMan.saveGame("data 2", "Test 2")        
        #self.fileMan.delSave("Test 1")
        #data = self.fileMan.savedGames()      
        #self.assertEquals(data[0], "Test 2")
        
        
    #def test_clearSaves(self):
        #self.fileMan.saveGame("data 1", "Test 1")
        #self.fileMan.saveGame("data 2", "Test 2")         
        #self.fileMan.clearSaves()
        #data = self.fileMan.savedGames()
        #self.assertEquals(data, [])
        
        



#unittest.main()
