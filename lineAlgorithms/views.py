from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import AdditionForm
import plotly.express as px
import pandas as pd
# Create your views here.

def home(request):
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

    
    return render(request, 'home.html', context
                 )


def brensenham(request):
    return render(request, template_name="brensenham.html")

def DDA(request):
    return render(request, template_name="DDA.html")
