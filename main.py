class Tesla:

    def __init__(self, model: str, color: str, autopilot: bool = False):
        """
        Initializes all inputs
        :param model: str
        :param color: str
        :param autopilot: str

        returns private initialized variables
        """
        self._is_locked = False
        self.__model = model
        self.__battery_charge = 99.9
        self.__color = color
        self.__is_locked = True
        self.__seats_count = 5
        self.__autopilot = autopilot

    @property
    def color(self) -> str:
        return self.__color

    def welcome(self) -> str:
        raise NotImplementedError

    def autopilot(self, obsticle: str) -> str:
        if self.__autopilot:
            return f"Tesla model S avoids {obsticle}"
        return "Autopilot is not available"

    @property
    def seats_count(self) -> int:
        """
        Returns the count of seats of a car
        """
        return self.__seats_count

    @seats_count.setter
    def seats_count(self, count: int):
        if count < 2:
            print("Seats count cannot be lower than 2!")
        else:
            self.__seats_count = count

    def lock(self):
        """Locks a car
        """
        self._is_locked = True

    def unlock(self):
        """Unlocks a car"""

    def open_doors(self) -> str:
        if not self.__is_locked:
            return "Doors opens sideways"
        return "Car is locked!"

    def check_battery_level(self) -> str:
        return f"Battery charge level is {self.__battery_charge}%"

    def charge_battery(self):
        self.__battery_charge = 100
        self.check_battery_level()

    def drive(self, travel_range: float) -> str:
        battery_discharge_percent = travel_range * self.__efficiency
        if self.__battery_charge - battery_discharge_percent >= 0:
            self.__battery_charge -= battery_discharge_percent
        else:
            print("Battery charge level is too low!")
        return self.check_battery_level()


tesla = Tesla("S", "red")
assert tesla.color == "red"
assert tesla.autopilot("tree") == "Autopilot is not available"
