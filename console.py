#!/usr/bin/python3
""" Console class """

import cmd
import shlex
import models


class HBNBCommand(cmd.Cmd):
    """ Handle console monitor class
    Args:
        cmd: cmd class inheritance
    """
    prompt = "(hbnb) "

    # Quit commands and  Emptyline
    # ============================================================ #

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

    # Create
    # ============================================================ #

    def do_create(self, arg):
        """ Create an instance and save it """
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        instance = getattr(models, class_name)()
        instance.save()
        print(instance.id)

    # Show instance
    # ============================================================ #

    def do_show(self, arg):
        """ Prints the string rep of an instance """
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        all_objects = models.storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in all_objects:
            print("** no instance found **")
            return

        print(all_objects[key])

    # Destroy
    # ============================================================ #

    def do_destroy(self, arg):
        """ Deletes an instance based on class name + ID """
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        all_objects = models.storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in all_objects:
            print("** no instance found **")
            return

        del all_objects[key]
        models.storage.save()

    # Show all instances
    # ============================================================ #

    def do_all(self, arg):
        """Print all instances from the storage"""
        all_objects = models.storage.all()

        if not arg:
            print([str(instance) for instance in all_objects.values()])
        else:
            args = shlex.split(arg)
            class_name = args[0]

            if class_name not in models.classes:
                print("** class doesn't exist **")
                return

            for instance in all_objects.values():
                if type(instance).__name__ == class_name:
                    print(str(instance))

    # Update instance
    # ============================================================ #

    def do_update(self, arg):
        """Update an instance and save it"""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)

        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        all_objects = models.storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in all_objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribut_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribut_value = args[3]

        setattr(all_objects[key], attribut_name, attribut_value)
        all_objects[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
