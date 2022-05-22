from django.urls import path
from . import views

urlpatterns = [
    path('customerlist/', views.GetCustomerListView.as_view()),
    path('add-customer/', views.AddCustomerView.as_view()),
    path('add-country/', views.AddCountryView.as_view()),
    path('add-position/', views.AddPositionView.as_view()),
    path('update/<int:pk>/', views.UpdateCustomerView.as_view()),
    path('delete/<int:pk>/', views.DeleteCustomerView.as_view()),
    path('delete-positon/<int:pk>/', views.DeleteCountryView.as_view()),
    path('delete-country/<int:pk>/', views.DeletePositionView.as_view()),
    path('send/', views.SendEmailView.as_view()),
    path('countries/', views.GetCountriesView.as_view()),
    path('positions/', views.GetPositionsView.as_view())
]
