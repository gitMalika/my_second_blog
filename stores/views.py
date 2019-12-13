from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def stores_render(request):
    return render(request, 'stores.html')