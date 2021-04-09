from simple_benchmark import benchmark
from recursia_3 import fact_rec
from recursiv_hvost_4 import fact_line_iter_proc
import matplotlib.pyplot as plt

def factorial(n):
   if n == 0 or n == 1:
       return 1
   else:
       prod = 1
       for i in range(1, n + 1):
           prod *= i
       return prod




funcs = [fact_rec, fact_line_iter_proc, factorial]

arguments = {}
for i in range(30):
    arguments['i'+str(i)] = i

print(arguments)
argument_name = 'size of number'
aliases = {fact_rec: 'Простая рекурсия', fact_line_iter_proc: 'Хвостовая рекурсия',factorial: "использование цикла" }
b = benchmark(funcs,arguments , argument_name, function_aliases=aliases)
b.plot()

plt.show(b)