def stock_availability(inventory, command, *args):
    if command == 'sell':

        if len(args) == 0:
            inventory = inventory[1::]

        elif isinstance(args[0], int):
            inventory = inventory[int(args[0])::]

        elif len(args) > 0:
            for el in args:
                if el in inventory:
                    inventory = list(filter(lambda a: a != el, inventory))

    elif command == 'delivery':
        inventory.extend(args)

    return inventory