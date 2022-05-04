import matplotlib.pyplot as plt


class PLOT:

    def __init__(self, function: str, min: int, max: int) -> None:
        self.valide_function = function
        self.min = min
        self.max = max

    def __generate_x_step(self):
        """ uses the minimum number and the maximum number of x and generate an apropriate step
        """
        return int((self.max - self.min) / 100)

    def plot(self):
        """ generate x numbers an plot the function
        """
        x = []
        y = []
        step = self.__generate_x_step()
        for i in range(self.min,self.max,step) :
            val = None
            try :
                val = eval(self.valide_function,{"__builtins__": None},{"x" : i})
            except : 
                continue
            y.append(val)
            x.append(i)
        plt.plot(x,y)
        plt.show()