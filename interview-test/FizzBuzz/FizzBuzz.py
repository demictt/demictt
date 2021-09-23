
def FizzBuzz(rg):
    for fizzbuzz in range(rg+1):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("FizzBuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("Fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("Buzz")
            continue
        print(FizzBuzz)

FizzBuzz(n)

def QuickerFizzBuzz(rg):
    for i in range(1,rg+1): 
        print("Fizz"*(i%3<1)+"Buzz"*(i%5<1) or i)

QuickerFizzBuzz(n)
