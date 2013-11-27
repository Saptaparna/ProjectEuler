def fib(n):
	if n==0: return 0;
	if n==1: return 1;
        return fib(n-1) + fib(n-2);
sum = 0;
for n in range(0, 1000):
    a = fib(n);
    if(a%2==0): sum += a;
    if(a>=4000000): 
               print sum;
	       exit()
