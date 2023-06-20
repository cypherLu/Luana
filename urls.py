from django.urls import path
from . import views

urlpatterns=[
    path('', views.kilig, name='kilig'),
    path('fanfic/<int:id>', views.fanficView, name="fanfic-view"),
    path('newfanfic/', views.newFanfic, name='new-fanfic'),
    path('edit/<int:id>', views.editfanfic, name='edit-fanfic'),
    path('delete/<int:id>', views.deletefanfic, name='delete-fanfic'),
]