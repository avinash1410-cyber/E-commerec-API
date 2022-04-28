from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from product.models import Products
from rest_framework.response import Response
from product.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_products_by_date(request):
    if request.method == "GET":
        data = Products.objects.all()
        if data == None:
            return HttpResponse("NONE")
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)
    else:
        return HttpResponse("Wrong REquest")


@api_view(['GET','POST'])
def search(request):
    if request.method=="POST":
        q= request.POST['q']
        data=Products.objects.filter(name__icontains=q)
        if data ==None:
            return HttpResponse("NONE")
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)
    else:
        return render(request,'search.html')



#@api_view(['GET','POST'])
#@staticmethod
def get_products_by_artist(request):
    pass


#@staticmethod




#@property
def get_products_by_id(ids):
    pass