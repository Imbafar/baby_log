from django.conf import settings
from itertools import groupby
# from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .models import Record
from .forms import RecordForm


def extract_date(entity):
    return entity.pub_date.date()

def index(request):
    record_list = Record.objects.all()
    paginator = Paginator(record_list, settings.POSTS_FOR_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'records/index.html', context)


def record_create(request):
    form = RecordForm(request.POST or None)
    if form.is_valid():
        record = form.save(commit=False)
        record.author = request.user
        record.save()
        return redirect('logs:index')
    return render(request, 'records/create_record.html', {'form': form})

def index2(request):
    record_list = Record.objects.all()
    paginator = Paginator(record_list, settings.POSTS_FOR_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    list_of_lists = [list(g) for _, g in groupby(page_obj, key=extract_date)]
    
    for date in list_of_lists:
        summ = 0
        for item in date:
            summ += item.text
        print(item.pub_date.day, summ)
    context = {
        'list_of_lists': list_of_lists,
    }
    return render(request, 'records/index2.html', context)