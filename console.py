#!/usr/bin/python3
"""
console module
"""

import cmd
from models.base_model import BaseModel
import models
from models import storage

"""
class HBNBCommand
"""

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handle the end of file condition"""
        return True

    def emptyline(self):
        """an empty line"""
        pass

    def do_create(self, arg):
        """ create a new instance"""
        dt = {}
        if not arg or arg == "":
            print("** class name missing **")
        elif arg == 'BaseModel':
            ojb = BaseModel()
            ojb.save()
            print(ojb.id)   
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation
           of an instance based on the class
           name and id
        """
        classes = ['BaseModel', 'User']
        if not arg or arg == " ":
            print("** class name missing **")
        else:
            args = arg.split(' ')
            if args[0] not in classes:
                print("** class doesn't exit **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance
           based on the class name
           and id
        """
        classes = ['BaseModel', 'User']
        if not arg or arg == " ":
            print("** class name is missing **")
        else:
            args = arg.split(' ')
            if args[0] not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("**  instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all():
                    storage.all().pop(key)

    def do_all(self, arg):
        """ Prints all string representation of all
            instances based or not on the class name.
        """
        classes = ['BaseModel', 'User']
        if arg == "":
            lst = []
            for key, val in storage.all().items():
                lst.append(str(val))
                print(lst)
        else:
            args = arg.split(' ')
            if args[0] not in classes:
                print("** class doesn't exit **")
            else:
                lst = []
                for key, val in storage.all().items():
                    if type(val).__name__ == args[0]:
                        lst.append(str(val))
                print(lst)

    def do_update(self, arg):
        """ Updates an instance based on the class
            name and id by adding or updating attribute 
            (save the change into the JSON file) 
        """
        classes = ['BaseModel', 'User']
        if not arg or arg == "":
            print("** class name missing **")
        else:
            args = arg.split(" ")
            key2 = "{}.{}".format(args[0], args[1])
            if args[0] not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** class doesn't exist **")
            elif key2 not in storage.all():
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                if args[3][0] == '"' and args[3][-1] == '"':
                    args[3] = args[3][1:-1]
            for key , val in storage.all().items():
                if  key2 == key:
                    setattr(storage.all()[key], args[2], args[3])
                    storage.all()[key].save()                   

if __name__ == '__main__':
    HBNBCommand().cmdloop()
