# ```math_plus.frange```

```pyhton
def frange(start, stop=None, step=1):
  '''float range - usage: for i in frange(1, 2, 0.1): print(i)'''
  if stop is None:
    start, stop = 0., float(start)
  while start <= stop-step:
    yield start
    start = round(start + step, 12)
#End function frange
```
### usage:
```pyhton
for i in frange(1, 2, 0.1):
  print(i)
```


# ```math_plus.Point```

```pyhton
class Point():
  def __init__(self, x, y):
    self.x, self.y = x, y
  def __sub__(self, other):
    dx = self.x - other.x
    dy = self.y - other.y
    return ((dx**2+dy**2))**0.5
  def __repr__(self):
    values = {'name': self.__qualname__, 'x': self.x, 'y': self.y}
    return '{name}(x={x}, y={y})'.format(**values)
#End class Point 
```