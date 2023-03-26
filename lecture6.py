# Есть класс Animal c одним методом voice().
# 1. Создать от него три класса наследника и для каждого сделать свою реализацию метода voice().
# 2. Создать по одному экземпляру всех наследников и вызвать для каждого переопределенный метод voice().

class Animal:
    def voice(self):
        pass


class Dog(Animal):
    def voice(self):
        return 'Gav'


class Cat(Animal):
    def voice(self):
        return 'Miaw'


class Cow(Animal):
    def voice(self):
        return 'Mu-u-u'


dog = Dog()
cat = Cat()
cow = Cow()

print('Dog voice : ' + dog.voice())
print('Cat voice : ' + cat.voice())
print('Cow voice : ' + cow.voice())
