
def Factors(n):
    #We create a function that generates the factors of an integer n
    return [i for i in range(1, n + 1) if not n%i]

def HeadsCount(n):
    countHead = 0
    for i in range(1, n +1):
        print(i)
        print(Factors(i))
        if(len(Factors(i)) % 2 == 1):
            countHead = countHead + 1
    return countHead