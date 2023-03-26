# Необходимо дополнить "Практическое задание №6" таким образом, чтобы в конце программы мы вызвали статический метод
# родительского класса Animal, который вывел бы нам количество всех созданных экземпляров.
# Если мы создали трех наследников в предыдущем задании, то наш метод должен вывести на экран число 3.

class Animal:
    numAnimals = 0

    def __init__(self):
        Animal.numAnimals += 1

    def printNumAnimals():
        print('Number of animals : ' + str(Animal.numAnimals))

    printNumAnimals = staticmethod(printNumAnimals)

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
Animal.printNumAnimals()
