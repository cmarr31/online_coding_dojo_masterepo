# try this either as a .py file or in the python shell
import turtle
# the distance we want the pointer to travel each time
# window = turtle.Screen()
# ella = turtle.Turtle()
# dist = 100
for x in range(0,6):
	window = turtle.Screen()
	ella = turtle.Turtle()
	dist = 100
    print "x", x
    for y in range(1,5):
        print "y", y
        # turn the pointer 90 degrees to the right
        ella.right(90)
        # advance according to set distance
        ella.forward(dist)
    # add to set distance
    dist += 20
