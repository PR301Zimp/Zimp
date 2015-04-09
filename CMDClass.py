import cmd

class CMD(cmd.Cmd):
    """Simple command processor example."""

    def __init__(self, game):
        cmd.Cmd.__init__(self)
        self.prompt = "Command: "
        self.game = game
        
    def do_fight(self):
        pass
    
    def do_run(self):
        pass
    
    def do_move(self, arg):
        if (arg == "N" or arg == "S" or arg == "W" or arg == "E"):
            self.game.movePlayer(arg)
        else:
            print("Not recognised direction please use N, S, E ,W")

    def help_move(self):
        print("syntax: move [direction]",)
        print("-- Moves player if possible")        
    
    def do_clearSaves(self, arg):
        self.game.clearSaves()
    
    def help_clearSaves(self):
        print("syntax: clearSaves",)
        print("-- Clears all saved games from storage")         
    def do_delSave(self, arg):
        self.game.delSave(arg)
        
    def help_delSave(self):
        print("syntax: delSave [save name]",)
        print("-- Deletes specific saved game")         
    
    def do_saveFiles(self, arg):
        print(self.game.viewSavedGames())
        
    def help_saveFiles(self):
        print("syntax: saveFiles",)
        print("-- Returns a list of all saves currently in shelve storage")         
    
    def do_save(self, arg):
        self.game.saveGame(arg)
        print ("Saved Game: " + arg)
    
    def help_save(self):
        print("syntax: save [save name]",)
        print("-- Saves game data in shelve")    
    
    def do_load(self, arg):
        self.game.loadGame(arg)
    
    def help_load(self):
        print("syntax: load [save name]",)
        print("-- Loads data from old game")


    def do_quit(self, line):
        """Quits you out of Quitter."""
        print("Quitting...")
##        return 1
        return True

