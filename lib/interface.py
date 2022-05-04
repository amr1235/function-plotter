from typing import Tuple

def isFunction(input_function: str) -> bool:
    """ check if the user function is a valide function
    """
    valide_sympols = ["x", "X"]
    valide_operators = ["+", "-", "*", "/", "^"]

    if(len(input_function) == 0):
        return False
    if((len(input_function) == 1) and (input_function[0] in valide_sympols)):
        return True

    # remove any white spaces
    function = input_function.replace(" ", "")

    # remove any parentheses
    function = function.replace("(", "")
    function = function.replace(")", "")

    # get the smallest units
    for op in valide_operators:
        function = function.replace(op, ":")
    units = function.split(":")

    # check each unit in units
    valide = True
    for unit in units:
        if (unit.isnumeric()):
            continue
        if (unit in valide_sympols):
            continue
        if (unit in valide_operators):
            continue
        valide = False
        break

    function = function.replace("^","**")

    # confirm that the function can be excecuted
    try :
        function = input_function.replace("^","**")
        i = 1
        val = eval(function,{"__builtins__": None},{"x" : i})
        print(val)
    except : 
        valide = False

    return valide

def valide_min_max(min : str,max : str) -> bool :
    """ function to check the entered minimum and maximum
    """
    if(int(min) >= int(max)) : return False
    return True
