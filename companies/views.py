from .serializers import Stockserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Stocks

@api_view(['GET'])
def apiurlsoverview(request):
    api_urls={
        'Stocklist-':'/stock-list/',
        'Stockdetail-': '/stock-detail/<str:pk>/',
        'Stockcreate-': '/stock-create/',
        'Stockupdate-': '/stock-update/<str:pk>/',
        'Stockdelete-': '/stock-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def stocklist(request):
    stocks = Stocks.objects.all()
    serializer = Stockserializers(stocks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def stockdetail(request,pk):
    stock = Stocks.objects.get(id=pk)
    serializer = Stockserializers(stock,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def stockcreate(request):
    serializer = Stockserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def stockupdate(request,pk):
    stock = Stocks.objects.get(id=pk)
    serializer = Stockserializers(instance=stock,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def stockdelete(request,pk):
    stock = Stocks.objects.get(id=pk)
    stock.delete()
    return Response('Stock deleted successfully')