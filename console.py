#!/usr/bin/python3
""" Console class """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Handle console monitor class
    Args:
        cmd: cmd class inheritance
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of file command to exit the program"""
        print('')
        return True

    def emptyline(self):
        """Do nothing when user input is empty"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
