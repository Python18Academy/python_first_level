def fact_line_iter_proc(n):
   return fact_iter(1, 1, n)

def fact_iter(prod, counter, n):
   if counter > n:
       return prod
   else:
       return fact_iter(counter * prod, counter + 1, n)

print(fact_line_iter_proc(100))#выдаст все те же 120