import math

# ask the user for the coordinates

x_coord1 = float(input("enter x1:"))
x_coord2 = float(input("enter x2:"))
y_coord1 = float(input("enter y1:"))
y_coord2 = float(input("enter y2:"))

point_x = x_coord2 - x_coord1
point_y = y_coord2 - y_coord1

# compute the distance using pow() and sqrt()

point_xy = pow(point_x, 2) + pow(point_y, 2)

distance = math.sqrt(point_xy)

# shows the result

print("the distance between the points is", distance)

