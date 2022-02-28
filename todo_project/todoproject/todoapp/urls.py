
from django.urls import path
from . import views
app_name = 'todoapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('tlhome/',views.TaskList.as_view(),name='tlhome'),
    path('tldetail/<int:pk>/',views.TaskDetailView.as_view(),name='tldetail'),
    path('tlupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='tlupdate'),
    path('tldelete/<int:pk>/',views.TaskDeleteView.as_view(),name='tldelete'),

]