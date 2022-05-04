import matplotlib.pyplot as plt
import numpy as np

class PLOT:

    def __init__(self, function: str, min: int, max: int) -> None:
        self.valide_function = function
        self.min = min
        self.max = max

    def plot(self) -> None:
        """ generate x numbers an plot the function
        """
        x = np.linspace(self.min, self.max).tolist()
        final_x = []
        y = []
        for i in range(len(x)):
            val = None
            try :
                val = eval(self.valide_function,{"__builtins__": None},{"x" : x[i]})
            except :
                continue
            final_x.append(x[i])
            y.append(val)
        plt.plot(final_x,y)
        plt.show()