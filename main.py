class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x


class Comcrete(metaclass=Meta):
    pass


obj = Comcrete()
print(obj.attr)

print(obj.__class__)
print(type(obj))
print(type(Comcrete))
print(type(Meta))
# print(Meta.attr) # error

print('--------------')
for t in int, float, dict, list, tuple:
    print(type(t))

print(type(type))

print('--------------')

def decorator(cls):
    class NewClass(cls):
        attr = 100
    return NewClass
...
@decorator
class X:
    pass

y = X()
print(y.attr)
# print(NewClass) # error

print('---------- or simply use inheritance ------')

class Base:
    attr = 100

class X(Base):
    pass

xx = X()

print(Base.attr)
print(xx.attr)
