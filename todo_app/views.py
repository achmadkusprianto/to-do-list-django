from django.shortcuts import render, redirect
from .models import List #import fungsi list dari models.py
from .forms import ListForm #import ListForm dari forms.py
from django.contrib import messages #fungsi django untuk pop up message
from django.http import HttpResponseRedirect

# membuat fungsi untuk setiap halaman aplikasi
def home(request):
    if request.method == 'POST': # apakah ada request post data baru ke to-do-list?
        form = ListForm(request.POST or None) 

        if form.is_valid(): # kalau valid, maka save form dan tampilkan semua item terkini
            form.save() # didefinisikan di forms.py
            all_items = List.objects.all
            messages.success(request, ('Item has been add to the list !'))
            return render(request, 'home.html', {'all_items': all_items})

    else:        
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def about(request):
    context = {'first_name': 'Achmad', 'last_name': 'Kusprianto'}
    return render(request, 'about.html', context)


def delete(request, list_id):
    item = List.objects.get(pk=list_id) # object memanggil id database (item = isian todo list)
    item.delete()
    messages.success(request, ('Item has been deleted !'))
    return redirect('home')


def cross_off(request, list_id):
    item = List.objects.get(pk=list_id) # object memanggil id database
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, list_id):
    item = List.objects.get(pk=list_id) # object memanggil id database
    item.completed = False
    item.save()
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST': # apakah ada request post data baru ke to-do-list?
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item) 

        if form.is_valid(): # kalau valid, maka save form dan tampilkan semua item terkini
            form.save() # didefinisikan di forms.py 
            messages.success(request, ('Item has been edited !'))
            return redirect('home')

    else:        
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})