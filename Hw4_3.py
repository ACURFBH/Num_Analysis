# HW 4 question 3
import matplotlib.pyplot as plt

# for the problem
a = 1000# river width
dt = 1# step size of my choice
v_0 = 10# initial current speed as stated by the problem
v_b = (5 , 10, 15)# the values of the boat speed for each part of the problem

# define a method for speed of the water current, this is always positive
def w(x):
    return 4 * v_0 * (x/a) * (1-(x/a))

# method used to take the square root to help with the method to solve the problem
def squareRoot(number):
    return number**0.5

# Solve the problem for v_b = 5
x = a
y = 0
xVal = [x]# collection of the x coordinates
yVal = [y]# collection of the y coordinates
print("generating points")
# generate coordinate values into the 2 lists
while 0 < x:
    # dy is the change in the y direction dependent on the water current and the translated direction the boat is moving
    dy = dt * (( -v_b[0] * (y/squareRoot((x**2)+(y**2)))) + w(x) )
    # dx is relative to the movement of the boat in the y direction and the boat speed by the pythagorean theorem
    dx = dt * ( -v_b[0] * (x/squareRoot((x**2)+(y**2))) )
    #print("x=", x, "y=", y)
    # y and x change by their step size
    y += dy
    x += dx
    # include the x and y values into the data
    yVal.append(y)
    xVal.append(x)
# plot the graph of all the values generated
print("plotting graph in red")
plt.plot(xVal, yVal, color = "red")

# Solve the problem for v_b = 10
x = a
y = 0
xVal = [x]# collection of the x coordinates
yVal = [y]# collection of the y coordinates
print("generating points")
# generate coordinate values into the 2 lists
while 0 < x:
    # dy is the change in the y direction dependent on the water current and the translated direction the boat is moving
    dy = dt * (( -v_b[1] * (y/squareRoot((x**2)+(y**2)))) + w(x) )
    # dx is relative to the movement of the boat in the y direction and the boat speed by the pythagorean theorem
    dx = dt * ( -v_b[1] * (x/squareRoot((x**2)+(y**2))) )
    #print("x=", x, "y=", y)
    # y and x change by their step size
    y += dy
    x += dx
    # include the x and y values into the data
    yVal.append(y)
    xVal.append(x)
# plot the graph of all the values generated
print("plotting graph in green")
plt.plot(xVal, yVal, color = "green")

# Solve the problem for v_b = 15
x = a
y = 0
xVal = [x]# collection of the x coordinates
yVal = [y]# collection of the y coordinates
print("generating points")
# generate coordinate values into the 2 lists
while 0 < x:
    # dy is the change in the y direction dependent on the water current and the translated direction the boat is moving
    dy = dt * (( -v_b[2] * (y/squareRoot((x**2)+(y**2)))) + w(x) )
    # dx is relative to the movement of the boat in the y direction and the boat speed by the pythagorean theorem
    dx = dt * ( -v_b[2] * (x/squareRoot((x**2)+(y**2))) )
    #print("x=", x, "y=", y)
    # y and x change by their step size
    y += dy
    x += dx
    # include the x and y values into the data
    yVal.append(y)
    xVal.append(x)
# plot the graph of all the values generated
print("plotting graph in blue")
plt.plot(xVal, yVal, color = "blue")

# show graph
plt.show()