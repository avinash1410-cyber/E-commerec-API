from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from rest_framework.views import APIView
from scipy.constants import slug
# from sklearn.gaussian_process.kernels import Product

from .models import Products
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from category.models import Category
from artist.models import Artist
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

# @api_view
# def trending(request):
#     data=Products.objects.all().order_by('created')
#     if data:
#         serializer = ProductSerializer(data,many=True)
#         return Response(serializer.data)
#     else:
#         return HttpResponse("No any product is trending")
#
#
#
# def artist(request,pk=None):
#     artist=Artist.objects.get(id=pk)
#     data=Products.get_products_by_artist(artist)
#     if data:
#         serializer = ProductSerializer(data,many=True)
#         return HttpResponse(serializer)
#     else:
#         return HttpResponse("No nay artist to shown")
#
# def category(request,pk=None):
#     category = Category.objects.get(id=pk)
#     data = Products.get_all_products_by_categoryid(pk)
#     if data:
#         serializer = ProductSerializer(data, many=True)
#         return HttpResponse(serializer)
#     else:
#         return HttpResponse("No nay category  to shown")






class Home(APIView):
    def get(self,*args,**kwargs):
        data = Products.objects.all()
        serializer = ProductSerializer(data,many=True)
        return Response(serializer.data)


class CategoryView(APIView):
    def get(self, request, slug=None):
        category = Category.objects.all()
        products = Products.objects.filter(category__slug = slug)
        data=products
        serializer = ProductSerializer(data,many=True)
        return Response(serializer.data)


class ProductAPIView(APIView):
    # template_name = "api/login.html"
    @method_decorator(login_required(login_url='login'))
    #@login_required(login_url='login')
    def get(self, request, pk=None, format=None):
        if pk:
            data = Products.objects.get(id=pk)
            serializer = ProductSerializer(data)
        else:
            data = Products.objects.all()
            serializer = ProductSerializer(data,many=True)

        return Response(serializer.data)

    #   @method_decorator(login_required(login_url='/login'))
    @method_decorator(login_required(login_url='login'))
    def post(self, request, format=None):
        data = request.data
        serializer = ProductSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Todo Created Successfully',
            'data': serializer.data
        }
        return response

#  @method_decorator(login_required(login_url='/login'))
    @method_decorator(login_required(login_url='login'))
    def put(self, request, pk=None, format=None):
        todo_to_update = Products.objects.get(pk=pk)
        serializer = ProductSerializer(instance=todo_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Todo Updated Successfully',
            'data': serializer.data
        }
        return response

  #  @method_decorator(login_required(login_url='/login'))
    @method_decorator(login_required(login_url='login'))
    def delete(self, request, pk, format=None):
        todo_to_delete =  Products.objects.get(pk=pk)

        todo_to_delete.delete()

        return Response({
            'message': 'Todo Deleted Successfully'
        })
