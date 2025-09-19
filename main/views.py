from django.shortcuts import render
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect
from .models import *
from .forms import *

def home(request):
    return render(request, "home.html")


def muallif_list(request):
    q = request.GET.get("q")
    mualliflar = Muallif.objects.all()

    if request.method == 'POST':
        form = MuallifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('muallif_list')

    context = {
        'mualliflar': mualliflar,
        'form': MuallifForm,
    }
    return render(request, 'muallif_list.html', context)

    if q:
        mualliflar = mualliflar.filter(ism__icontains=q)


    return render(request, "muallif_list.html", {"mualliflar": mualliflar})


def muallif_update(request, pk):
    muallif = get_object_or_404(Muallif, id=pk)
    if request.method == "POST":
        muallif.ism = request.POST.get("ism")
        muallif.jins = request.POST.get("jins")
        muallif.tugilgan_sana = request.POST.get("tugilgan_sana")
        muallif.kitob_soni = request.POST.get("kitob_soni")
        muallif.tirik = True if request.POST.get("tirik") == "on" else False
        muallif.save()
        return redirect("/muallif/")

    context = {"muallif_list": muallif}
    return render(request, "muallif_update.html", context)


def muallif_detail(request, pk):
    muallif = get_object_or_404(Muallif, pk=pk)
    kitoblar = Kitob.objects.filter(muallif=muallif)
    return render(request, "muallif_detail.html", {"muallif": muallif, "kitoblar": kitoblar})


def kitob_list(request):

    mualliflar = Muallif.objects.all()
    kitoblar = Kitob.objects.select_related("muallif").all()

    if request.method == 'POST':
        form = KitobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kitob_list')

    context = {
        'mualliflar': mualliflar,
        'kitoblar': kitoblar,
        'form': KitobForm,}
    return render(request, "kitob_list.html", context)

def kitob_update(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)
    mualliflar = Muallif.objects.all()

    if request.method == "POST":
        kitob.nom = request.POST.get("nom")
        kitob.janr = request.POST.get("janr")
        kitob.sahifa = request.POST.get("sahifa")
        muallif_id = request.POST.get("muallif")
        kitob.muallif = get_object_or_404(Muallif, id=pk)
        kitob.save()
        return redirect("/kitob_list/")

    context = {
        "kitob": kitob,
        "mualliflar": mualliflar
    }
    return render(request, "kitob_update.html", context)


def kitob_detail(request, pk):
    kitob = get_object_or_404(Kitob, pk=pk)
    return render(request, "kitob_detail.html", {"kitob": kitob})

def record_list(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("record_list")
    kitoblar = Kitob.objects.all()
    talabalar = Talaba.objects.all()
    adminlar = Admin.objects.all()

    context = {
        "kitoblar": kitoblar,
        "talabalar": talabalar,
        "adminlar": adminlar,
        'form': RecordForm }
    return render(request, "record_list.html", context )

    q = request.GET.get("q")
    recordlar = Record.objects.select_related("kitob", "talaba", "admin").all()
    if q:
        recordlar = recordlar.filter(talaba__ism__icontains=q)
    return render(request, "record_list.html", {"recordlar": recordlar})



def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)
    return render(request, "record_detail.html", {"record": record})



def muallif_delete(request, pk):
    muallif = get_object_or_404(Muallif, pk=pk)
    if request.method == "POST":
        muallif.delete()
        return redirect("muallif_list")
    return render(request, "muallif_confirm_delete.html", {"muallif": muallif})

def record_delete(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "POST":
        record.delete()
        return redirect("record_list")
    return render(request, "record_confirm_delete.html", {"record": record})

def student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/student/")
    students = Talaba.objects.all()

    search = request.GET.get('search')
    if search:
        students = students.filter(ism__contains=search)

    ordering = request.GET.get('ordering')
    if ordering:
        students = students.order_by(ordering)

    kurs = request.GET.get('kurs')
    if kurs:
        students = students.filter(kurs=kurs)


    context = {
        'students': students,
        'search': search,
        'ordering': ordering,
        'kurs': kurs,
        'form': StudentForm
    }
    return render(request, 'student.html', context)

def admin_list(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/admin_list/")
    adminlar = Admin.objects.all()
    context = {'form': AdminForm, 'adminlar': adminlar}

    return render(request, "admin_list.html", context)

def student_update(request,student_id):
    student = get_object_or_404(Talaba, id=student_id)
    if request.method == "POST":
        return redirect("/student/")

    context = {"student": student}
    return render(request, "student_update.html", context)


