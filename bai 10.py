a = float (input())
b = float(input())
c= float (input())
d = float(input())
if ( a == b and c == d ) or ( a == c and b == d ) or ( a == d and b ==c ):
    print("Yes")
else:
    print("No")
