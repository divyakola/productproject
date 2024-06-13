from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product
def product_insert(request):
    context = {}

    # create object of form
    form = ProductForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return render(request,'insert_result.html')

    context['form'] = form
    return render(request, "pinput.html", context)

def display(request):
    data=Product.objects.all()
    return render(request,'display.html',{'records':data})