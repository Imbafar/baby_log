from django.conf import settings

# from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SleepTimeForm

from .models import SLeepTime


def extract_date(entity):
    return entity.pub_date.date()


def index(request):
    sleeptime_obj = SLeepTime.objects.all()
    paginator = Paginator(sleeptime_obj, settings.POSTS_FOR_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "weight/index.html", context)
