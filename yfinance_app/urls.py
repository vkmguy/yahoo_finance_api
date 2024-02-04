from django.urls import path
from .views import MaxHistoricalDataAPIView, DateRangeHistoricalDataAPIView


urlpatterns = [
    path('historical-data/<str:symbol>/', MaxHistoricalDataAPIView.as_view(), name='historical-data'),
    path('historical-data/<str:symbol>/date-range/<str:start_date>/<str:end_date>/', DateRangeHistoricalDataAPIView.as_view(), name='date-range-historical-data'),
]