"""
a = 0
b =1
series = []

while  a<10:
     series.append(a)
     a=b
    # series.append(b)
     b = b+a
print(series)     
#    0 1 1 2 3 5 8
"""

def fib(n):
     a,b = 0,1
     list = []
     while a< n:
          list.append(a)
          a,b = b, a+b
     print(list)

fib(20)

#multi-dimensional array
rows = range(1,4)
cols = range(1,3)

for col in cols:
     for row in rows :
          print(row,col)
          
cells = [(row,col) for row in rows for col in cols]
for cell in cells:
     print(cell)
