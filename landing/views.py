from django.shortcuts import render, redirect
from .models import RecordType, Record, Messages
from .forms import ContactForm


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


def delete_view(request, id):
    record = Record.objects.get(pk=id)
    if not record:
        return redirect('/')

    record.delete()
    return redirect('/')


def edit_view(request, id):
    record = Record.objects.get(pk=id)
    if not record:
        return redirect('/')

    if request.POST:
        record.text = request.POST.get('text')
        record.phone = request.POST.get('phone')
        record.preferred_timing = request.POST.get('preferred_timing')
        record_type_id = int(request.POST.get('record_type'))
        record.record_type = RecordType.objects.get(pk=record_type_id)
        record.save()
        return redirect('/')

    record_types = RecordType.objects.all()
    return render(request, 'edit.html', { "record": record, "record_types": record_types })


def about_view(request):
    return render(request, 'about.html')


def contacts_view(request):
    form = ContactForm()

    if request.POST:
        new_message = ContactForm(request.POST)

        if new_message.is_valid():
            Messages(
                theme=new_message.cleaned_data["theme"],
                message=new_message.cleaned_data["message"],
                attachment=new_message.cleaned_data["attachment"]
            ).save()

            return redirect('/contacts')

        return render(
            request,
            'contacts.html',
            { "form": form, "error": "Неверно заполнены поля" }
        )

    return render(request, 'contacts.html', { "form": form })
