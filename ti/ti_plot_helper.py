# filename: ti_plot_helper.py
import ti_plotlib as plt

# colors
red = (255, 0, 00)
green = (0, 255, 00)
blue = (0, 0, 255)
black= (0, 0, 0)

def setup_plt(title='TI Plot Helper'):
  plt.window(-2,10,-2,10)
  plt.grid(1,1,"dotted")
  plt.axes("on")
  plt.title(title)

class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __repr__(self):
    values = {'name': self.__qualname__, 'x': self.x, 'y': self.y}
    return '{name}(x={x}, y={y})'.format(**values)
  def draw(self, color=(0, 0, 0), mark='o'):
    plt.color(*color)
    plt.plot(self.x, self.y, mark)    
#End class Ponto

class Rect():
  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2
  def declive(self):
    return (self.p2.y-self.p1.y)/(self.p2.x-self.p1.x)
  def __repr__(self):
    values = {'name': self.__qualname__, 'p1': self.p1, 'p2': self.p2}
    return '{name}(p1={p1}, p2={p2})'.format(**values)
  def draw(self, color=(0, 0, 0)):
    plt.color(*color) 
    plt.line(self.p1.x,self.p1.y,self.p2.x,self.p2.y,"default")
#End class Reta
