from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import AdditionForm, RadiusForm
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
# Create your views here.

def DDA(request):
    result = None
    
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
        if step == 0:
            return (0, 0)
        else:
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
        return (xp, yp)
    if request.method == 'POST':
        form = AdditionForm(request.POST)
        if form.is_valid():
            x1 = form.cleaned_data['number1']
            x2 = form.cleaned_data['number2']
            y1 = form.cleaned_data['number3']
            y2 = form.cleaned_data['number4']


            result = DDA(x1, x2, y1, y2)
    else:
        form = AdditionForm()
   
    if result is not None and len(result) >= 2:
        data = {
          'x': result[0],
          'y': result[1]
            }
        df = pd.DataFrame(data)

        fig = px.line(
            df,
            x= 'x',
            y= 'y',
            title='DDA',
            labels={'x':'x-axis', 'y':'y-axis'},
            )

        fig.update_layout(
               title={
                   'font_size':22,
                   'xanchor': 'center',
                   'x': 0.5
                   },
               plot_bgcolor='lightblue',
               paper_bgcolor='lightblue'
                )
        chart = fig.to_html()

        context = {
        'resultx': result[0],
        'resulty': result[1],
        'form':form,
        'chart':chart,
    }
    else:
        context = {
        'resultx': None,
        'resulty': None,
        'form': form,
                }

    
    return render(request, 'DDA.html', context
                 )


def bresenham(request):
    result = None
    def bresenham_line(x1, y1, x2, y2):
    # Initialize variables
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        slope_error = dy - dx
        x, y = x1, y1
        coordinatesX = []
        coordinatesY = []

        coordinates = [(x, y)]

    # Determine the direction of the line
        x_inc = 1 if x1 < x2 else -1
        y_inc = 1 if y1 < y2 else -1

    # Main loop to generate coordinates
        for _ in range(dx):
            x += x_inc
            if slope_error >= 0:
                y += y_inc
                slope_error -= dx
            slope_error += dy
            coordinatesX.append(x)
            coordinatesY.append(y)
            coordinates.append((x, y))

        return coordinatesX, coordinatesY, coordinates
    if request.method == 'POST':
        form = AdditionForm(request.POST)
        if form.is_valid():
            x1 = form.cleaned_data['number1']
            y1 = form.cleaned_data['number2']
            x2 = form.cleaned_data['number3']
            y2 = form.cleaned_data['number4']


            result = bresenham_line(x1, x2, y1, y2)
    else:
        form = AdditionForm()
    if result is not None and len(result) >= 2:
        data = {
          'x': result[0],
          'y': result[1]
            }
        df = pd.DataFrame(data)

        fig = px.line(
            df,
            x= 'x',
            y= 'y',
            title='Bresenham',
            labels={'x':'x-axis', 'y':'y-axis'},
            )

        fig.update_layout(
               title={
                   'font_size':22,
                   'xanchor': 'center',
                   'x': 0.5
                   },
               plot_bgcolor='lightblue',
               paper_bgcolor='lightblue'
                )
        chart = fig.to_html()

        context = {
        'resultx': result[0],
        'resulty': result[1],
        #'coordinates':result[2],
        'form':form,
        'chart':chart,
    }
    else:
        context = {
            'resultx': None,
            'resulty': None,
            'form': form,


                }

    return render(request, "bresenham.html", context)


def midpoint_circle(request):
    ''''function draw_circle(radius):
    x = radius
    y = 0
    p = 1 - radius  // Initial decision parameter

    points = [(x, y)]  // Store the points of the circle

    while x > y:
        y = y + 1

        // Mid-point is inside or on the perimeter of the circle
        if p <= 0:
            p = p + 2 * y + 1
        else:  // Mid-point is outside the perimeter of the circle
            x = x - 1
            p = p + 2 * (y - x) + 1

        // All the perimeter points have already been recorded
        if x < y:
            break

        points.append((x, y))
        points.append((-x, y))
        points.append((x, -y))
        points.append((-x, -y))

        // If the generated point is on the line y = x, then
        // the perimeter points have already been recorded
        if x != y:
            points.append((y, x))
            points.append((-y, x))
            points.append((y, -x))
            points.append((-y, -x))

    return points
'''
    result = None 
    def draw_circle(radius):
        coordinatesX = []
        coordinatesY = []

        x = radius
        y = 0
        p = 1 - radius  # Initial decision parameter

        points = [(x, y)]  # Store the points of the circle

        while x > y:
            y += 1

            # Mid-point is inside or on the perimeter of the circle
            if p <= 0:
                p = p + 2 * y + 1
            else:  # Mid-point is outside the perimeter of the circle
                x -= 1
                p = p + 2 * (y - x) + 1

            # All the perimeter points have already been printed
            if x < y:
                break

            points.extend([
                (x, y), (-x, y), (x, -y), (-x, -y),
            ])

            # If the generated point is on the line y = x, then
            # the perimeter points have already been printed
            if x != y:
                points.extend([
                    (y, x), (-y, x), (y, -x), (-y, -x),
                ])
        for x, y in points:
            coordinatesX.append(x)
            coordinatesY.append(y)
        return coordinatesX, coordinatesY, points

    if request.method == 'POST':
        form = RadiusForm(request.POST)
        if form.is_valid():
            radius = form.cleaned_data['number1']
           

            result = draw_circle(radius)
    else:
        form = RadiusForm()
    if result is not None and len(result) >= 2:
        # data = {
        #   'x': result[0],
        #   'y': result[1]
        #     }
        # df = pd.DataFrame(data)

        # fig = px.line(
        #     df,
        #     x= 'x',
        #     y= 'y',
        #     title='Midpoint Circle',
        #     labels={'x':'x-axis', 'y':'y-axis'},
        #     )

        # fig.update_layout(
        #        title={
        #            'font_size':22,
        #            'xanchor': 'center',
        #            'x': 0.5
        #            },
        #        plot_bgcolor='lightblue',
        #        paper_bgcolor='lightblue'
        #         )
        # create nodes
        nodes = []
        for i in range(len(result[2])):
            nodes.append(go.Scatter(
                x=[result[2][i][0]],
                y=[result[2][i][1]],
                mode='markers',
                marker=dict(
                    size=10,
                        color='blue'
                ),
                name='nodes'
            ))
        # # create lines
        # lines = []
        # for i in range(len(result[2])):
        #     lines.append(go.Scatter(
        #         x=[0, result[2][i][0]],
        #         y=[0, result[2][i][1]],
        #         mode='lines',
        #         name='lines'
        #     ))
        ## create circles
        # circles = []
        # for i in range(len(result[2])):
        #     circles.append(go.Scatter(
        #         x=result[0],
        #         y=result[1],
        #         mode='lines',
        #         name='circles'
        #     ))
        # create figure
        fig = go.Figure(data=nodes )
        fig.update_layout(
            title='Midpoint Circle',
            xaxis=dict(
                range=[-radius - 1, radius + 1],
                zeroline=False,
                showgrid=False,
                showticklabels=False,
            ),
            yaxis=dict(
                range=[-radius - 1, radius + 1],
                zeroline=False,
                showgrid=False,
                showticklabels=False,
            ),
            plot_bgcolor='lightblue',
            paper_bgcolor='lightblue'
        )

        chart = fig.to_html()

        context = {
        'resultx': result[0],
        'resulty': result[1],
        #'coordinates':result[2],
        'form':form,
        'chart':chart,
    }
    else:
        context = {
            'resultx': None,
            'resulty': None,
            'form': form,


                }

    return render(request, "midpoint.html", context)

from geoip2 import GeoIP2
from django.shortcuts import render

def get_location_from_ip(request):
    ip_address = request.META.get('REMOTE_ADDR')
    geo_reader = GeoIP2()
    response = geo_reader.city(ip_address)

    city = response.get('city', {}).get('names', {}).get('en')
    country = response.get('country', {}).get('names', {}).get('en')

    context = {
        'city': city,
        'country': country,
    }

    return render(request, 'location.html', context)


