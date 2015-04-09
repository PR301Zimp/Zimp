import cmd


class CMD(cmd.Cmd):
    """Simple command processor example."""

    def __init__(self, game):
        cmd.Cmd.__init__(self)
        self.prompt = "Command: "
        self.game = game

    def do_fight(self, arg):
        if (isinstance(self.game.phase, int)):
            self.game.fight(arg)
        else:
            print("Command not avalible")

    def help_fight(self):
        print("syntax: fight",)
        print("-- Elects to fight the zombies")

    def do_retreat(self, arg):
        if (isinstance(self.game.phase, int)):
            self.game.retreat()
        else:
            print("Command not avalible")

    def help_retreat(self):
        print("syntax: retreat",)
        print("-- Elects to retreat to the previous tile away from the" +
              " zombies atthe cost of 1 health")

    def do_heal(self, arg):
        if (self.game.phaseChecker("heal")):
            self.game.waitHeal(arg)
        else:
            print("Command not avalible")

    def help_heal(self):
        print("syntax: heal y/n",)
        print("-- Elects whether to stop and heal 3 points or to carry on")

    def do_selectItem(self, arg):
        if (self.game.phaseChecker("fight")):
            self.game.selectItem(arg)
        else:
            print("Command not avalible")

    def help_selectItem(self, arg):
        print("syntax: selectItem [item number]",)
        print("-- Selects the item to use in battle either 1 or 2")

    def do_itemSearch(self, arg):
        if (self.game.phaseChecker("item")):
            self.game.searchItem(arg)
        else:
            print("Command not avalible")

    def help_itemSearch(self, arg):
        print("syntax: itemSearch",)
        print("-- Searchs for an item on the floor")

    def do_setTile(self, arg):
        if (self.game.phase == "N" or self.game.phase == "S" or
                self.game.phase == "E" or self.game.phase == "W"):
            self.game.setTile()
        else:
            print("Command not avalible")

    def help_setTile(self):
        print("syntax: setTile",)
        print("-- drops specified item if room is requied")

    def do_itemDrop(self, arg):
        self.game.itemDrop(arg)

    def help_itemDrop(self, arg):
        print("syntax: itemDrop [item name]/[no]",)
        print("-- drops specified item if room is requied")

    def do_move(self, arg):
        if(self.game.phase == "move"):
            if (arg == "N" or arg == "S" or arg == "W" or arg == "E"):
                self.game.movePlayer(arg)
            else:
                print("Not recognised direction please use N, S, E ,W")
        else:
            print("Command not avalible")

    def help_move(self):
        print("syntax: move [direction]",)
        print("-- Moves player if possible")

    def do_rotate(self, arg):
        if (self.game.phase == "N" or self.game.phase == "S" or
                self.game.phase == "E" or self.game.phase == "W"):
            self.game.rotateTile(arg)
        else:
            print("Command not avalible")

    def help_rotate(self):
        print("syntax: rotate [clock]/[anti]",)
        print("-- Rotates tile clockwise or anticlockwise")

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
        return True
