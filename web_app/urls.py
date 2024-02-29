from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name=''),
    path('register',views.register, name='register'),
    path('login',views.my_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('dashboard',views.dashboard,name="dashboard"),
    path('create-record',views.create_record,name="create-record"),
    path('update-record/<int:id>',views.update_record,name='update-record'),
    path('view-record/<int:id>',views.view_single_record,name='view-record'),
    path('delete-record/<int:id>',views.delete_record,name= 'delete-record'),
]