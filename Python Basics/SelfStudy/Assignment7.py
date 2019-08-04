#Interface with scroll and click abstract methods
from abc import abstractmethod, ABC

class TouchScreenLaptop(ABC):

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

#HP and Dell Class inherit TouchScreenLaptop and having method scroll [print] only
class HP(TouchScreenLaptop):
    def scroll(self):
        print("HP Laptop is Scrolling")

class Dell(TouchScreenLaptop):
    def scroll(self):
        print("HP Laptop is Scrolling")

#HPNotebook by HP by invoking object
class HPNotebook(HP):
    def click(self):
        print("HPNotebook is Clicking")
#DELLNotebook by Dell by invoking object
class DellNotebook(Dell):
    def click(self):
        print("DellNotebook is Clicking")

H1 = HPNotebook()
D1 = DellNotebook()

H1.click()
H1.scroll()

D1.click()
D1.scroll()

