from math import factorial

def bionomial(x,n,p):
    factional_part = factorial(n)/(factorial(x)*factorial(n-x))
    result = factional_part*p**x*(1-p)**(n-x)
    return result


if __name__ == "__main__":
    a,b = map(float, input().split())
    p = a/(a+b)
    n = 6
    answer = 0
    
    for x in range(3,7):
        answer+= bionomial(x,n,p)

    print(round(answer,3))