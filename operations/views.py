from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def query(request):
 

    queryone = int(request.GET['inputone'])
    querytwo = int(request.GET.get('inputtwo'))
    op = request.GET.get('op')
    if (op and op == 'sub'):
        answer = queryone - querytwo
        message = '{} - {} = {}'.format(str(queryone), str(querytwo), str(answer))
    else:
        answer = queryone + querytwo
        message = '{} + {} = {}'.format(str(queryone), str(querytwo), str(answer))
    template = 'operations/result.json'
    context = {'message': message}
    return render(request, template, context, content_type="application/json")

@login_required
def addition(request):
    return render(request, 'operations/addition.html')

@login_required
def subtraction(request):
    return render(request, 'operations/subtraction.html')

def home(request):
    return render(request, 'operations/home.html')

def index(request):
    return render(request, 'operations/index.html')
