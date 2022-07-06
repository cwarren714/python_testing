def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        elif num == 0:
            return 'please enter a non-zero number'
        else:
            return 'please enter a number'
    except ValueError as err:
        return err
