from numerize import numerize

class Calculator:
    def __init__(self, current_diamond: int, current_crystal: int, goal: str) -> None:
        self.diamond = current_diamond
        self.crystal = current_crystal
        self.goal = goal
        self.days = 0
        self.price = 0
        self.iterator(goal)

    def __repr__(self) -> str:
        return f"remaining diamond: {self.diamond}\nremaining crystal: {self.crystal}\ndays needed: {self.days}\ncost: {numerize.numerize(self.price)}"

    @property
    def diamond(self) -> int:
        return self.__diamond
    
    @diamond.setter
    def diamond(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        self.__diamond = value

    @property
    def crystal(self) -> int:
        return self.__crystal
    
    @crystal.setter
    def crystal(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        self.__crystal = value

    @property
    def price(self) -> int:
        return self.__price
    
    @price.setter
    def price(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        self.__price = value

    @property
    def days(self) -> int:
        return self.__days
    
    @days.setter
    def days(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        self.__days = value

    def iterator(self, goal) -> None:
        def calculate():
            self.add_daily_box()
            self.days += 1
            if self.days % 30 == 0:
                self.add_monthly_box()
                
        #could use some match case and kwarg
        if goal == "collector":
            target: int = 3780 - 465 
            # 3780 is the price for 1 if user utilizing the 50% daily discount
            # 465 is the free token given to player after doing certain quest
            while self.crystal < target:
                calculate()

        elif goal == "zodiac":
            target: int = 1260
            # 1260 is the price assigned if user spins on launch day
            while self.crystal < target:
                calculate()

        self.crystal -= target

    def add_weekly(self):
        self.diamond += 220
        self.crystal += 70
        self.price += 32_000

    def add_daily_box(self):
        if self.diamond < 10:
            self.add_weekly()
        val = 1.4 * 10
        self.crystal += int(val)
        self.diamond -= 10

    def add_monthly_box(self):
        if self.diamond < 80:
            self.add_weekly()
        val = 1.8
        self.crystal += int(val * 80)
        self.diamond -= 80


if __name__ == "__main__":
    pass
