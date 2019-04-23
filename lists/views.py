from django.shortcuts import redirect, render
from lists.models import Item
from django.http import HttpResponse

def home_page(request):
  if request.method == 'POST':
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/')
  return render(request, 'home.html')
