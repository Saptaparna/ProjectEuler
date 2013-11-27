def fib(n):
        if n==0: return 0;
        if n==1: return 1;
        return fib(n-1) + fib(n-2);
sum = 0;
array = []
#for n in range(1, 50):
    #a = fib(n);
    #print a
    #array.append(a)
array2 = []
for i in range(31, 10000, 5):
  array2.append(i)
print array2
print array2[994]

array3 = []
for j in range(7, 1001):
  array3.append(j)
print len(array3)
