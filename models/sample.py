#!/usr/bin/python3

import cmd

class MyCmd(cmd.Cmd):
    prompt = '>>> '

    def do_greet(self, person):
        """Greet the person"""
        if person:
            print(f"Hello, {person}")
        else:
            print("Hello!")

    def do_quit(self, arg):
        """Quit the program"""
        print("Quitting.")
        return True

if __name__ == '__main__':
    MyCmd().cmdloop()