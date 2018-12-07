from django.urls import path
from org_app import views

app_name = 'org_app'

urlpatterns = [
    path('',views.DepartmentListView.as_view(),name='list'),
    path('<int:pk>',views.DepartmentDetailView.as_view(),name='detail'),
    path('create/',views.DepartmentCreateView.as_view(),name='create'),
    path('update/<int:pk>',views.DepartmentUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.DepartmentDeleteView.as_view(),name='delete')
]
