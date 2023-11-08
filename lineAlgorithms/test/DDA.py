import matplotlib.pyplot as plt

def DDA(x1, x2, y1, y2):
   xp = []
   yp = []
   # Get the steps
   dx = x2-x1
   dy = y2-y1

   if dx > dy:
       step = dx
   else:
        step = dy
   # print(step)
   
   # Calculate the y and x increment
   y_inc = dy/step
   x_inc = dx/step

   #create a loop with a range of steps while adding the increment values starting from (x1, y1)
   
   if step < 0:
       inc = -1*step
   else:
        inc = step
   for i in range(inc):
        if step < 0:
            x1 -= x_inc
            y1 -= y_inc
        else:
           x1 += x_inc
           y1 += y_inc

        xp.append(round(x1))
        yp.append(round(y1))
        # print the results and round them to the nearest whole number
        print(round(x1), round(y1))
   # create a scatter plot      
   plt.scatter(xp, yp, label='Data Points', color='b', marker='o')
   
   plt.xlabel('X-axis')
   plt.ylabel('Y-axis')
   plt.title('Scatter Plot Example')

   # Add a legend
   plt.legend()

   # Display the plot
   plt.show()

   

# Get the two points
x1,y1 = (12, 9)

x2,y2 = (17, 14)

DDA(x1, x2, y1, y2)
