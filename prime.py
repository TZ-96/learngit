def prime(n):
    x = 2;
    while x<n:
        if n%x == 0:
	        return 1;
        x = x+1
    return 0
a = 10000;
b = 1;
while b<a:
    y=prime(b);
    if y == 0:
	    print(b);
    b = b+1
