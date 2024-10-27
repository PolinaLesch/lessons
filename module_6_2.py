class Vehicle:
    __COLOR_VARIANTS = ['Red', 'Blue', 'Black', 'Green']
    def __init__(self, owner, __model,  __color, __engine_power,):
        self.owner = str(owner) #владелец транспорта. (владелец может меняться)
        self.__model = str(__model) # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = int(__engine_power) # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color = str(__color) # название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_model(self):
        print(F'Модель: {self.__model}')

    def get_horsepower(self):
        print(F'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(F'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(F'Владелец: {self.owner}\n')

    def set_color(self, new_color):
        # new_color = input('Новый цвет: ')
        reg_colours = [colour.lower() for colour in self.__COLOR_VARIANTS] #проверка относительно регистра
        if new_color.lower() in reg_colours:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}\n')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
