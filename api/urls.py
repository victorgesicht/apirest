from django.urls import path 
from . import views


urlpatterns=[
    path('list/', views.todoListCreate.as_view(), name='list'),
    path('listdestroy/<int:pk>', views.todoListCreateRetrieveDestroy.as_view(), name='list_destroy'),

]