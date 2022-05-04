from typing import Tuple

def isFunction(inpu_function: str) -> bool:
    """ check if the user function is a valide function
    """
    valide_sympols = ["x", "X"]
    valide_operators = ["+", "-", "*", "/", "^"]

    if(len(inpu_function) == 0):
        return False
    if((len(inpu_function) == 1) and (inpu_function[0] in valide_sympols)):
        return True

    # remove any white spaces
    function = inpu_function.replace(" ", "")

    # remove any parentheses
    function = function.replace("(", "")
    function = function.replace(")", "")

    # get the smallest units
    for op in valide_operators:
        function = function.replace(op, ":")
    print(function)
    units = function.split(":")
    print(units)
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
        function = inpu_function.replace("^","**")
        i = 1
        val = eval(function,{"__builtins__": None},{"x" : i})
        print(val)
    except : 
        valide = False

    return valide

def valide_min_max(min : str,max : str) -> Tuple[bool,list] :
    """ function to check the entered minimum and maximum
    """
    erros = []
    if(int(min) <= 0) :
        erros.append("Invalide Minimum Value")
    if(int(max) <= 0) :
        erros.append("Invalide Maximum Value")
    if(int(min) <= int(max)) :
        erros.append("Minimum value should be smaller than the maximum value")
    if(len(erros) == 0) :
        return (True,[])
    else : 
        return (False,erros)

