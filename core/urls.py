from django.urls import path
from django.contrib import admin
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),

    # Mualliflar
    path("mualliflar/", muallif_list, name="muallif_list"),
    path("muallif/<int:pk>/", muallif_detail, name="muallif_detail"),
    path("muallif/<int:pk>/delete/", muallif_delete, name="muallif_delete"),
    path("muallif/<int:pk>/update/", muallif_update, name="muallif_update"),

    # Kitoblar
    path("kitoblar/", kitob_list, name="kitob_list"),
    path("kitob/<int:pk>/", kitob_detail, name="kitob_detail"),
    path("kitob/<int:pk>/update/", kitob_update, name="kitob_update"),

    # Recordlar
    path("recordlar/", record_list, name="record_list"),
    path("record/<int:pk>/", record_detail, name="record_detail"),
    path("record/<int:pk>/delete/", record_delete, name="record_delete"),


    # Talabalar
    path("student/", student, name="student"),
    path("student/<int:student_id>/update/", student_update, name="student_update"),

    # Adminlar
    path("admin_list/", admin_list, name="admin_list"),
]