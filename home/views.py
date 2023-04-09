from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin')
def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})
