from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="todo"),
    path('del/<str:item_id>', views.remove, name="del"),
]
