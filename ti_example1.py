# filename: ti_example1.py
from ti_plot_helper import setup_plt, Point, Rect
from ti_plot_helper import red, green, blue, black

setup_plt()
A = Point(0, 0)
B = Point(5, 5)
r = Rect(A, B)

A.draw(red) 
B.draw(blue)
r.draw(green)
