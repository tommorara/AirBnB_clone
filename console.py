#!/usr/bin/python3

"""Console module for the AirBnB clone project."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB command interpreter."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program upon receiving EOF (End Of File)"""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass

    def do_help(self, arg):
        """List commands with 'help' or get detailed help using 'help cmd'."""
        super().do_help(arg)


# Add additional command methods here


if __name__ == '__main__':
    HBNBCommand().cmdloop()
