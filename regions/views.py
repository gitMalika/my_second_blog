from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def region_render(request):
    return render(request, 'regions.html')