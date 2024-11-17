from django.urls import path
from . import views


urlpatterns = [
    path('inflows/list/', views.InflowListView.as_view(), name='inflow_list'),
    path('inflows/create/', views.InflowCreateView.as_view(), name='inflow_create'),
    path('inflows/<int:pk>/detail/', views.InflowDetailView.as_view(), name='inflow_detail'),

    path('https://relfsrecife.pythonanywhere.com/api/v1/inflows/', views.InflowCreateListAPIView.as_view(), name='inflow-create-list-api-view'),
    path('https://relfsrecife.pythonanywhere.com/api/v1/inflows/<int:pk>/', views.InflowRetrieveAPIView.as_view(), name='inflow-detail-api-view'),
]
