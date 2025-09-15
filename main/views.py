from django.shortcuts import render
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect
from .models import *

def home(request):
    return render(request, "home.html")

# 1
def muallif_list(request):
    q = request.GET.get("q")
    mualliflar = Muallif.objects.all()
    if q:
        mualliflar = mualliflar.filter(ism__icontains=q)
    return render(request, "muallif_list.html", {"mualliflar": mualliflar})


# 2
def muallif_detail(request, pk):
    muallif = get_object_or_404(Muallif, pk=pk)
    kitoblar = Kitob.objects.filter(muallif=muallif)
    return render(request, "muallif_detail.html", {"muallif": muallif, "kitoblar": kitoblar})

# 3
def kitob_list(request):
    if request.method == "POST":
        Kitob.objects.create(
            nomi=request.POST.get("nom"),
            janr=request.POST.get("janr"),
            sahifa=request.POST.get("sahifa"),
            muallif=get_object_or_404(Muallif, id=request.POST.get("muallif_id"))

        )
        return redirect("/kitob_list/")
    mualliflar = Muallif.objects.all()
    kitoblar = Kitob.objects.select_related("muallif").all()
    return render(request, "kitob_list.html", {"kitoblar": kitoblar, "mualliflar": mualliflar,})

# 4
def kitob_detail(request, pk):
    kitob = get_object_or_404(Kitob, pk=pk)
    return render(request, "kitob_detail.html", {"kitob": kitob})

# 5
def record_list(request):
    if request.method == "POST":
        Record.objects.create(
            kitob=get_object_or_404(Kitob, id=request.POST.get("kitob_id")),
            talaba=get_object_or_404(Talaba, id=request.POST.get("talaba_id")),
            admin=get_object_or_404(Admin, id=request.POST.get("admin_id")),
            olingan_sana=request.POST.get("olingan_sana"),
            qaytargan_sana=request.POST.get("qaytargan_sana")
        )
        return redirect("record_list")
    kitoblar = Kitob.objects.all()
    talabalar = Talaba.objects.all()
    adminlar = Admin.objects.all()
    return render(request, "record_list.html", {
        "kitoblar": kitoblar,
        "talabalar": talabalar,
        "adminlar": adminlar
    })

    q = request.GET.get("q")
    recordlar = Record.objects.select_related("kitob", "talaba", "admin").all()
    if q:
        recordlar = recordlar.filter(talaba__ism__icontains=q)
    return render(request, "record_list.html", {"recordlar": recordlar})


# 6
def tirik_mualliflar(request):
    mualliflar = Muallif.objects.filter(tirik=True)
    return render(request, "tirik_mualliflar.html", {"mualliflar": mualliflar})

# 7
def top3_kitob(request):
    kitoblar = Kitob.objects.order_by("-sahifa")[:3]
    return render(request, "top3_kitob.html", {"kitoblar": kitoblar})

# 8
def top3_muallif(request):
    mualliflar = Muallif.objects.annotate(k_count=Count("kitob")).order_by("-k_count")[:3]
    return render(request, "top3_muallif.html", {"mualliflar": mualliflar})

# 9
def oxirgi3_record(request):
    recordlar = Record.objects.order_by("-olingan_sana")[:3]
    return render(request, "songi3_record.html", {"recordlar": recordlar})

# 10
def tirik_muallif_kitoblar(request):
    kitoblar = Kitob.objects.filter(muallif__tirik=True)
    return render(request, "tirik_muallif_kitoblar.html", {"kitoblar": kitoblar})

# 11
def badiiy_kitoblar(request):
    kitoblar = Kitob.objects.filter(janr__iexact="badiiy")
    return render(request, "badiiy_kitoblar.html", {"kitoblar": kitoblar})

# 12
def eng_qari3_muallif(request):
    mualliflar = Muallif.objects.order_by("tugilgan_sana")[:3]
    return render(request, "katta3_muallif.html", {"mualliflar": mualliflar})

# 13
def kam_kitobli_muallif_kitoblar(request):
    mualliflar = Muallif.objects.filter(kitob_soni__lt=10)
    kitoblar = Kitob.objects.filter(muallif__in=mualliflar)
    return render(request, "kam_kitobli_muallif_kitoblar.html", {"kitoblar": kitoblar})

# 14
def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)
    return render(request, "record_detail.html", {"record": record})

# 15
def bitiruvchi_recordlar(request):
    recordlar = Record.objects.filter(talaba__kurs=4)
    return render(request, "bitiruvchi_recordlar.html", {"recordlar": recordlar})

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
        Talaba.objects.create(
            ism=request.POST.get("ism"),
            guruh=request.POST.get("guruh"),
            kurs=request.POST.get("kurs"),
            kitob_soni=request.POST.get("kitob_soni") if request.POST.get("kitob_soni") else 0

            )
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
    }
    return render(request, 'student.html', context)

def admin_list(request):
    if request.method == "POST":
        Admin.objects.create(
            ism=request.POST.get("ism"),
            ish_vaqti=request.POST.get("ish_vaqti"),  # models'dan choices
        )
        return redirect("/admin_list/")

    adminlar = Admin.objects.all()
    return render(request, "admin_list.html", {"adminlar": adminlar})
