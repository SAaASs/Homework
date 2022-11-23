def quick(mass):
   if len(mass) <= 1:
       return mass
   else:
       q = mass[len(mass)//2]
       bigger = []
       equal = []
       smaller = []
       for n in mass:
           if n > q:
               bigger.append(n)
           elif n < q:
               smaller.append(n)
           else:
               equal.append(n)
       return quick(smaller) + equal + quick(bigger)
aa = [9,8,7,6,5,4,3,2,1]
print(quick(aa))
