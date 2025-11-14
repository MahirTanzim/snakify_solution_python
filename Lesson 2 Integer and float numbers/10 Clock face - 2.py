a = float(input())

# Hour hand angle 'a' lets us find minutes:
#   in 1 hour -> minute handle does a full 360deg rotation 
#                hour handle rotate 30deg
#   so in a hour minute handle's rotation = 360/30*a = 12*a

# Use modulo 360 to keep angle within a full circle.

print((12*a)%360)