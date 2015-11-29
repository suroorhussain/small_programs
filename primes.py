def primes(n) :
    num = []
    primes = [1]
    for i in range(2,n+1) :
        num.append(i)
    print num
    while len(num) != 0  :
        primes.append(num.pop(0))
        print primes


primes(10)
    
