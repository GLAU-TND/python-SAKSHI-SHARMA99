class MyException(Exception):
    pass
def XYZ(a,b):
    if(a+b)<150:
        raise MyException("custom Exception Occured")
    else:
        print(a+b)
a=int(input())
b=int(input())
XYZ(a,b)

