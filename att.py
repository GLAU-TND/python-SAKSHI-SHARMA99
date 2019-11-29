try:
    n=int(input())
    a=input()
    b=int(input())
    c=n+b
    l=a+b
    n.append(3)
except ValueError:
    raise ValueError("Here value error occured")
except TypeError:
    raise TypeError("Here Type error occured")
except:
    raise AttributeError("Here attribute error occured")
