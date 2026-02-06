from django.urls import path
from .views import EmployeeListCreate, EmployeeDetail

urlpatterns = [
    path('', EmployeeListCreate.as_view()),
    path('<int:pk>/', EmployeeDetail.as_view()),
]
