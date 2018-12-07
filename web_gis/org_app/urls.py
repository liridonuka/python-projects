from django.urls import path
from org_app import views

app_name = 'org_app'

urlpatterns = [
    path('',views.DepartmentListView.as_view(),name='list'),
    path('<int:pk>',views.DepartmentDetailView.as_view(),name='detail')
]
