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
    kitoblar = Kitob.objects.select_related("muallif").all()
    return render(request, "kitob_list.html", {"kitoblar": kitoblar})

# 4
def kitob_detail(request, pk):
    kitob = get_object_or_404(Kitob, pk=pk)
    return render(request, "kitob_detail.html", {"kitob": kitob})

# 5
def record_list(request):
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
