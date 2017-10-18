class Empty:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError

x = Empty()
print(x.age)


class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value + 10  # avoid loops, That is, use self.__dict__['name'] = x, not self.name = x;
        else:
            raise AttributeError(attr + ' not allowed')

x = Accesscontrol()
x.age = 40
x.age


class PrivateExc(Exception): pass
class Privacy:
    def __setattr__(self, attrname, value):
            if attrname in self.privates:
                raise PrivateExc(attrname, self)
            else:
                self.__dict__[attrname] = value

class Test1(Privacy):
    privates = ['age']
class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'

if __name__ == '__main__':
    x = Test1()
    y = Test2()

    x.name = 'Bob'
    #y.name = 'Sue'     # Fail's
    print(x.name)
    y.age  = 30
    #x.age  = 40         # Fails
    print(y.age)
