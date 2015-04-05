import shelve

class FileManager(object):
    def __init__(self, filePath):
        self.filePath = filePath

    def savedGames(self):
        data = shelve.open(self.filePath)
        saves = data.keys()
        data.close()
        return saves
        

    def saveGame(self, state, name):
        data = shelve.open(self.filePath)
        try:
            data[name] =  state 
        except ValueError:
            print("random stuff")
        data.close()

    def loadGame(self, save):
        data = shelve.open(self.filePath)
        try:
            return data[save]
        except ValueError:
            print("random stuff")        
        data.close()