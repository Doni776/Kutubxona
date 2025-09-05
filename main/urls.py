from django.urls import path
from . import views

urlpatterns = [
    path("mualliflar/", views.muallif_list, name="muallif_list"),
    path("muallif/<int:pk>/", views.muallif_detail, name="muallif_detail"),
    path("kitoblar/", views.kitob_list, name="kitob_list"),
    path("kitob/<int:pk>/", views.kitob_detail, name="kitob_detail"),
    path("recordlar/", views.record_list, name="record_list"),
    path("record/<int:pk>/", views.record_detail, name="record_detail"),
    path("tirik_mualliflar/", views.tirik_mualliflar, name="tirik_mualliflar"),
    path("top3_kitob/", views.top3_kitob, name="top3_kitob"),
    path("top3_muallif/", views.top3_muallif, name="top3_muallif"),
    path("oxirgi3_record/", views.oxirgi3_record, name="oxirgi3_record"),
    path("badiiy_kitoblar/", views.badiiy_kitoblar, name="badiiy_kitoblar"),
    path("bitiruvchi_recordlar/", views.bitiruvchi_recordlar, name="bitiruvchi_recordlar"),
]
