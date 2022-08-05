from django.conf import settings

# from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import WeightForm

from .models import Weight


def extract_date(entity):
    return entity.pub_date.date()


def index(request):
    weight_obj = Weight.objects.all()
    paginator = Paginator(weight_obj, settings.POSTS_FOR_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "weight/index.html", context)


def weight_create(request):
    form = WeightForm(request.POST or None)
    if form.is_valid():
        record = form.save(commit=False)
        record.author = request.user
        record.save()
        return redirect("weight:index")
    return render(request, "weight/create_weight.html", {"form": form})


def weight_edit(request, weight_id):
    weight = get_object_or_404(Weight, id=weight_id)
    if request.user != weight.author:
        return redirect("weight:index", weight_id)

    form = WeightForm(request.POST or None, instance=weight)
    if form.is_valid():
        form.save()
        return redirect("weight:index")
    context = {"form": form, "weight": weight, "is_edit": True}
    return render(request, "weight/create_weight.html", context)


def weight_delete(request, weight_id):
    get_object_or_404(Weight, id=weight_id)
    obj = Weight.objects.filter(id=weight_id)
    obj.delete()
    return redirect("weight:index")
