from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def district_render(request):
    return render(request, 'almaty.html')