#  form untuk memanggil mengisi list yg selanjutnya masuk database
from django import forms
from .models import List # impor db list

# mendefinisikan db list di views.py
class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item', 'completed']

