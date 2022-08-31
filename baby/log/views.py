from django.conf import settings
from itertools import groupby

# from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .models import Record
from .forms import RecordForm


def extract_date(entity):
    return entity.pub_date.date()


def record_create(request):
    form = RecordForm(request.POST or None)
    if form.is_valid():
        record = form.save(commit=False)
        record.author = request.user
        record.save()
        return redirect("logs:index")
    return render(request, "records/create_record.html", {"form": form})


def index(request):
    record_list = Record.objects.all()
    paginator = Paginator(record_list, settings.POSTS_FOR_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    list_of_lists = [list(g) for _, g in groupby(page_obj, key=extract_date)]
    list_of_total = []
    list_of_kasha = []
    for date in list_of_lists:
        total = 0
        total_kasha = 0
        for item in date:
            if not item.kasha:
                total += item.text
            else:
                total_kasha += item.text
        list_of_total.append(total)
        list_of_kasha.append(total_kasha)
    # todo: make lists with list comprehensions
    list_of_lists = zip(list_of_lists, list_of_total, list_of_kasha)
    context = {
        "list_of_lists": list_of_lists,
    }
    return render(request, "records/index.html", context)


def record_detail(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    form = RecordForm()
    context = {
        "record": record,
        "form": form,
    }
    return render(request, "records/record_detail.html", context)


def record_edit(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    if request.user != record.author:
        return redirect("logs:record_detail", record_id)

    form = RecordForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect("logs:index")
    context = {"form": form, "post": record, "is_edit": True}
    return render(request, "records/create_record.html", context)


def record_delete(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    obj = Record.objects.filter(id=record_id)
    obj.delete()
    return redirect("logs:index")
