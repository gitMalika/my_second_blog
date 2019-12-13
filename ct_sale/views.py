from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def ct_render(request):
    return render(request, 'ct_sale.html')
