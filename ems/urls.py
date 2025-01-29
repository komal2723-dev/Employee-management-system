from django.urls import path
from . import views 

urlpatterns = [
    path('', views.main_page.as_view(), name='home'),
    path('showemp/', views.show_all_emp.as_view(),name="showdata"),
    path('addemp/', views.add_emp.as_view(),name="addemp"),
    path('remove/', views.delete_emp.as_view(),name="delete_emp"),
    path('remove/<int:eid>/', views.delete_emp.as_view(),name="delete_emp"),
    path('update/<int:id>/', views.update_Emp.as_view(),name="update_emp"),
    path('filter_emp/', views.filter_Emp.as_view(),name="getdata"),
]