import math

def s(x):
    z=math.radians(x)
    print "the sine value of ",x," in radian is:",z,",in degree:",math.degrees(z)
    return

def c(y):
    v=math.cos(y)
    print "the cosine value of ",y," in radian is:",v,",in degree:",math.degrees(v)
    return

a=input("enter number:")
s(a)
c(a)
