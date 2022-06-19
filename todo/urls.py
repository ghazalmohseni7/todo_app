from django.urls import path
from . import views

urlpatterns =[
    path('',views.list_todo_items.as_view(),name='list_todo'),
    path('insert_todo/',views.insert_todo_item,name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/',views.delete_todo_item,name='delete_todo_item'),
]