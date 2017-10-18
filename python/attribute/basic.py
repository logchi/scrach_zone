import math

print(hasattr(math, 'pi'))

print(getattr(math, 'pi'))

setattr(math, 'pi', 100)
print(math.pi)

delattr(math, 'pi')
try:
    print(math.pi)
except AttributeError:
    print('math module does not have pi attribute anymore!')
