class Test:
    a = 'this is a class attribute'
    __a = 'this is a private attribute'
    def __init__(self, pa):
        self.__a = pa

    def test(self):
        print('instance could visit class attribute a:', self.a)

    def test_private(self):
        print('instance could visit private attribute __a:', self.__a)
        print(self._Test__a)

# t = Test()
# print(t.a)
# t.test()

if __name__ == '__main__':
    t1 = Test("test private 1")
    t2 = Test("test private 2")
    t1.test_private()
    t2.test_private()
    try:
        print(Test.__a)
    except AttributeError:
        print('Names anywhere within class statements with '
              'two leading un‐ derscores only (e.g., __X) '
              'are mangled at compile time to include the '
              'enclosing class name as a prefix (e.g., _Class__X).')
    finally:
        print("This is right --", Test._Test__a)