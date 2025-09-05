from django.contrib import admin
from django.urls import path, include
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("mualliflar/", muallif_list, name="muallif_list"),
    path("muallif/<int:pk>/", muallif_detail, name="muallif_detail"),
    path("kitoblar/", kitob_list, name="kitob_list"),
    path("kitob/<int:pk>/", kitob_detail, name="kitob_detail"),
    path("recordlar/", record_list, name="record_list"),
    path("record/<int:pk>/", record_detail, name="record_detail"),
    path("tirik_mualliflar/", tirik_mualliflar, name="tirik_mualliflar"),
    path("top3_kitob/", top3_kitob, name="top3_kitob"),
    path("top3_muallif/", top3_muallif, name="top3_muallif"),
    path("songi3_record/", oxirgi3_record, name="oxirgi3_record"),
    path("badiiy_kitoblar/", badiiy_kitoblar, name="badiiy_kitoblar"),
    path("bitiruvchi_recordlar/", bitiruvchi_recordlar, name="bitiruvchi_recordlar"),
    path("kam_kitobli_mualliflari/", kam_kitobli_muallif_kitoblar, name="kam_kitobli_muallif_kitoblar"),
]
