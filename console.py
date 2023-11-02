#!/usr/bin/python3
""" Console class """

import cmd
import shlex
import models
import json


class HBNBCommand(cmd.Cmd):
    """ Handle console monitor class
    Args:
        cmd: cmd class inheritance
    """
    prompt = "(hbnb) "

    # Quit commands and  Emptyline
    # ============================================================ #

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of file command to exit the program"""
        print('')
        return True

    def emptyline(self):
        """Do nothing when user input is empty"""
        pass

    # Create
    # ============================================================ #

    def do_create(self, line):
        """ Create an instance and save it """
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        instance = getattr(models, class_name)()
        instance.save()
        print(instance.id)

    # Show instance
    # ============================================================ #

    def do_show(self, line):
        """ Prints the string rep of an instance """
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)

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

    def do_destroy(self, line):
        """ Deletes an instance based on class name + ID """
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)

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

    def do_all(self, line):
        """Print all instances from the storage"""
        all_objects = models.storage.all()

        if not line:
            print([str(instance) for instance in all_objects.values()])
        else:
            args = shlex.split(line)
            class_name = args[0]

            if class_name not in models.classes:
                print("** class doesn't exist **")
                return

            for instance in all_objects.values():
                if type(instance).__name__ == class_name:
                    print(str(instance))

    # Update instance
    # ============================================================ #

    def do_update(self, line):
        """Update an instance and save it"""
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)

        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = models.storage.all()

        if key not in all_objects:
            print("** no instance found **")
            return

        for idx in range(2, len(args), 2):
            attribut_name = args[idx]
            attribut_value = args[idx + 1]

            if attribut_name in models.int_attrs:
                setattr(all_objects[key], attribut_name, int(attribut_value))

            elif attribut_name in models.float_attrs:
                setattr(all_objects[key], attribut_name, float(attribut_value))

            else:
                setattr(all_objects[key], attribut_name, attribut_value)

            all_objects[key].save()

    # Count instances in json (all or per class)
    # ============================================================ #

    def do_count(self, line):
        """Count instances"""
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        all_objects = models.storage.all()

        count = 0

        for key in all_objects.keys():
            name = key.split('.')[0]
            if name == class_name:
                count += 1

        print(count)

    # Alternative command syntax
    # ============================================================ #

    def precmd(self, line):
        """handle alt syntax"""
        if not line:
            return line

        if "." not in line:
            return line

        class_and_cmd = line.split("(")[0]
        class_name = class_and_cmd.split(".")[0]

        if class_name not in models.classes:
            return line

        command = class_and_cmd.split(".")[1]
        new_line = f"{command} {class_name}"

        # get all attributs inside ()
        args = line.split("(")[1].replace(")", "").split(",")

        if len(args) > 0:
            instance_id = args[0]
            new_line += f" {instance_id}"

        if len(args) > 1:
            items = ', '.join(item for item in args[1:])

            # if dictionnary in ()
            try:
                items_dict = json.loads(items)
                name = [key for key in items_dict.keys()]
                value = [val for val in items_dict.values()]
                for idx in range(len(items_dict)):
                    new_line += f" {name[idx]} {value[idx]}"
            # else
            except json.decoder.JSONDecodeError:
                attribut_name = args[1]
                attribut_value = args[2]
                new_line += f"{attribut_name}{attribut_value}"

        return new_line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
