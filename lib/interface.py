from numpy import number


def isFunction(function: str) -> bool:
    """ check if the user function is a valide function
    """
    valide_sympols = ["x","X"]
    valide_operators = ["+","-","*","/","^"]

    if(len(function) == 0) : return False
    if((len(function) == 1) and (function[0] in valide_sympols)) : return True

    # remove any white spaces 
    function = function.replace(" ","")

    # get the smallest units
    for op in valide_operators : 
        function = function.replace(op,":")
    units = function.split(":")
    print(units)
    # check each unit in units
    valide = True
    for unit in units : 
        if (unit.isnumeric()) :
            continue
        if (unit in valide_sympols) :
            continue
        if (unit in valide_operators) :
            continue
        valide = False
    return valide

# def valide_minimum(value : number) -> bool :

# print(isFunction("2*x + 2 - 6*x^2"))