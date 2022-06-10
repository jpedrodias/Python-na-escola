# '''frange''' 

'''pyhton
def frange(start, stop=None, step=1):
  '''float range - usage: for i in frange(1, 2, 0.1): print(i)'''
  if stop is None:
    start, stop = 0., float(start)
  while start <= stop-step:
    yield start
    start = round(start + step, 12)
#End function frange
'''
