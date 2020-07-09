x=int(input("enter the base"))
y=int(input("enter the exponent"))

def power(base,exponent):
    if(exponent==0):
        return 1
    else:
        return base*power(base,exponent-1)
print(x,"to the power",y,"= ",power(x,y))
