import math
a = 1
b = -2
c = -5

def equation(a,b,c):
  # obliczanie delty
  D = b * b - 4 * a * c 
  print(D)
  if D > 0:
    x1 =(-b-math.sqrt(D))/(2*a)
    x2 =(-b+math.sqrt(D))/(2*a)
    wyniki = (x1 ,x2)
    print(wyniki)
    
  elif D == 0:
    x1 = -b / 2*a
    print(x1)
  else:
    print("Brak rozwiązań - Delta ujemna")
  pass

equation(a,b,c)

print("UDAŁO SIEEEEEEEEEEEEEEEEE!")


