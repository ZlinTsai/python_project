from django.shortcuts import render
from django.http import Http404
from .models import MyTable

def my_view(request, id=None):
    records = MyTable.objects.all()
    selected_record = None
    if id:
        selected_record = MyTable.objects.get(id=id)
        print(selected_record)
    return render(request, 'app1/my_template.html', {'records': records, 'selected_record': selected_record})
