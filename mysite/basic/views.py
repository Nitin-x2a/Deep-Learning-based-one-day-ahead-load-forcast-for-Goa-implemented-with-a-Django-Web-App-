from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from basic.backend import update, view_fetch_dates, run, forecast_fetch_dates, test_fetch_dates, fest_fetch_dates
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Update(LoginRequiredMixin, TemplateView):
    template_name = 'update.html'
    login_url = '/user_login/'
    redirect = 'update'

class Browse(TemplateView):
    template_name = 'view_data_menu.html'

class Results(TemplateView):
    template_name = 'results.html'

class Index(TemplateView):
    template_name = 'index.html'


@login_required
def upload_megawatts(request):

    template = 'update_megawatts.html'

    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'The file should be of .csv type')

    update.update_megawatts(csv_file)

    return redirect('home')

@login_required
def upload_festival(request):

    template = 'update_festival.html'

    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'The file should be of .csv type')

    update.update_festival(csv_file)

    return redirect('home')

def browse_megawatts(request):

    template = 'datetimepicker.html'

    start_limit = view_fetch_dates.start_limit()
    end_limit = view_fetch_dates.end_limit()
    format = 'YYYY-MM-DD HH:mm'

    if request.method == "GET":
        context = {'start_limit': json.dumps(start_limit), 'end_limit': json.dumps(end_limit), 'format': json.dumps(format) }
        return render(request, template, context)

    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    run.run_model(2, start_date, end_date)

    return redirect('results')

def browse_festival(request):

    template = 'datetimepicker.html'

    start_limit = fest_fetch_dates.start_limit()
    end_limit = fest_fetch_dates.end_limit()
    format = 'YYYY-MM-DD'


    if request.method == "GET":
        context = {'start_limit': json.dumps(start_limit), 'end_limit': json.dumps(end_limit), 'format': json.dumps(format) }
        return render(request, template, context)

    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    run.run_model(4, start_date, end_date)

    return redirect('results')

def forecast(request):

    template = 'datetimepicker.html'

    start_limit = forecast_fetch_dates.start_limit()
    end_limit = forecast_fetch_dates.end_limit()
    format = 'YYYY-MM-DD HH:mm'

    if request.method == "GET":
        context = {'start_limit': json.dumps(start_limit), 'end_limit': json.dumps(end_limit), 'format': json.dumps(format) }
        return render(request, template, context)

    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    run.run_model(1, start_date, end_date)

    return redirect('results')

def test(request):

    template = 'datetimepicker.html'

    start_limit = test_fetch_dates.start_limit()
    end_limit = test_fetch_dates.end_limit()
    format = 'YYYY-MM-DD HH:mm'

    if request.method == "GET":
        context = {'start_limit': json.dumps(start_limit), 'end_limit': json.dumps(end_limit), 'format': json.dumps(format) }
        return render(request, template, context)

    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    run.run_model(3, start_date, end_date)

    return redirect('results')


def log_in(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')

        else:
            return render(request, 'cred_req.html', {'warn': 'Incorrect details. Try again!'})

    else:
        return render(request, 'cred_req.html', {})

def log_out(request):

    logout(request)
    return redirect('home')
