#!/usr/bin/python3
'''HBNBCommand - console for the airbnb clone'''
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, inp):
        '''Quit command to exit the program'''
        return True

    do_EOF = do_quit

HBNBCommand().cmdloop()
