
class Horse: # Класс описывающий лошадь
    x_distance = 0 # пройденный путь
    _sound = 'Frrr' # звук, который издаёт лошадь
    def run(self, dx): # где dx - изменение дистанции, увеличивает x_distance на dx
        self.x_distance += dx

class Eagle: # Класс описывающий орла
    y_distance = 0 # высота полёта
    sound = 'I train, eat, sleep, and repeat' # звук, который издаёт орёл(отсылка)
    def fly(self, dy): # где dy - изменение дистанции, увеличивает y_distance на dy
        self.y_distance += dy

class Pegasus(Horse, Eagle): # класс описывающий пегаса

    def __init__(self):
        self.sound = super()._sound
        self.sound = super().sound

    def move(self, dx, dy):# где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run и fly соответственно.
        self.run(dx)
        self.fly(dy)

    def get_pos(self): # возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
        pos_pegasus = (self.x_distance, self.y_distance)
        return pos_pegasus

    def voice(self):  # печатает значение унаследованного атрибута sound.
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
