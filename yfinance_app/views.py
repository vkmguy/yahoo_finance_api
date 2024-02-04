import yfinance as yf
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import DataFrameSerializer


def fetch_historical_data(data):
    historical_data = data[['Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']].reset_index()
    historical_data.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']
    return historical_data


class MaxHistoricalDataAPIView(APIView):
    def get(self, request, symbol):
        data = yf.Ticker(symbol).history(period="max")
        result = fetch_historical_data(data)
        serializer = DataFrameSerializer(result, many=True)
        return Response(DataFrameSerializer.flatten_dataframe(serializer.instance))


class DateRangeHistoricalDataAPIView(APIView):
    def get(self, request, symbol, start_date, end_date):
        data = yf.Ticker(symbol).history(start=start_date, end=end_date)
        result = fetch_historical_data(data)
        serializer = DataFrameSerializer(result, many=True)
        return Response(DataFrameSerializer.flatten_dataframe(serializer.instance))
