from django.shortcuts import render, redirect
from .models import RecordType, Record


def home_view(request):
    record_types = RecordType.objects.all()
    records = Record.objects.all()

    return render(
        request,
        'index.html',
        {
            "record_types": record_types,
            "records": records
        }
    )


def create_view(request):
    text = request.POST.get('text')
    phone = request.POST.get('phone')
    preferred_timing = request.POST.get('preferred_timing')
    record_type_id = int(request.POST.get('record_type'))

    record_type = RecordType.objects.get(pk=record_type_id)

    Record(
        text=text,
        phone=phone,
        preferred_timing=preferred_timing,
        record_type=record_type
    ).save()

    return redirect('/')


def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')
