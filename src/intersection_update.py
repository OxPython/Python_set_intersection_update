'''
Created on Jul 9, 2014

@author: viejoemer

HowTo keep only the common values between several sets in Python?

¿Cómo mantener únicamente los valores comunes entre varios sets en Python?

intersection_update(other, ...)
set &= other & ...
Update the set, keeping only elements found in it and all others.
'''

#Create a set with values.
s = set([0,1,2,3])
print("set one", s)

s2 = set([1,6])
print("set two", s2)

#Using intersection_update there are the common values.
s.intersection_update(s2)
print("set one intersection_update",s)

s = set([0,1,2,3])
s2 = set([1,6,3])
s3 = set([0,1,2,3])
#Another way is set &= other $ ...
s3 &= s2 & s
print("set one intersection_update",s)
print("set two intersection_update",s)
print("set three intersection_update",s)
#Be careful because, of the element are in more than one set, that element
#is maintained in the result. As you can see.