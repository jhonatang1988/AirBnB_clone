#!/usr/bin/python3
'''HBNBCommand - console for the airbnb clone'''
import cmd
from models.base_model import BaseModel
from models import storage
import os.path
import json


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    __file_path = 'file.json'

    def do_quit(self, inp):
        '''Quit command to exit the program'''
        return True

    do_EOF = do_quit

    def do_create(self, inp):
        '''create a new instance of a model'''
        if len(inp) == 0:
            print("** class name missing **")
        elif inp == 'BaseModel':
            new = BaseModel()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, inp):
        if len(inp) == 0:
            print("** class name missing **")
        else:
            a_list = inp.split()
            if a_list[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif len(a_list) == 1:
                print("** instance id missing **")
            elif a_list[0] == 'BaseModel' and len(a_list) == 2:
                if os.path.isfile(self.__file_path):
                    with open(self.__file_path,
                              encoding='utf-8', mode='r') as f:
                        a_string = f.read()
                        a_dict = json.loads(a_string)
                        if 'BaseModel.' + a_list[1] in a_dict:
                            print(BaseModel(**(a_dict['BaseModel.' +
                                                      a_list[1]])))
                        else:
                            print("** no instance found **")

    def do_destroy(self, inp):
        if len(inp) == 0:
            print("** class name missing **")
        else:
            a_list = inp.split()
            if a_list[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif len(a_list) == 1:
                print("** instance id missing **")
            elif a_list[0] == 'BaseModel' and len(a_list) == 2:
                if os.path.isfile(self.__file_path):
                    with open(self.__file_path,
                              encoding='utf-8', mode='r') as f:
                        a_string = f.read()
                        a_dict = json.loads(a_string)
                        if 'BaseModel.' + a_list[1] in a_dict:
                            del a_dict['BaseModel.' + a_list[1]]
                        else:
                            print("** no instance found **")
                    with open(self.__file_path,
                              encoding='utf-8', mode='w') as f:
                        f.write(json.dumps(a_dict))

HBNBCommand().cmdloop()
