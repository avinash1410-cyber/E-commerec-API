from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from scipy.constants import slug
# from sklearn.gaussian_process.kernels import Product

from .models import Products
from .serializers import ProductSerializer
from rest_framework.response import Response

from category.models import Category



class CategoryView(APIView):
    def get(self, request, slug=None):
        category = Category.objects.all()
        products = Products.objects.filter(category__slug = slug)
        data=products
        serializer = ProductSerializer(data,many=True)
        return Response(serializer.data)


class ProductAPIView(APIView):
    # template_name = "api/login.html"
    #    @method_decorator(login_required(login_url='/login'))
    def get(self, request, pk=None, format=None):
        if pk:
            data = Products.objects.get(id=pk)
            serializer = ProductSerializer(data)
        else:
            data = Products.objects.all()
            serializer = ProductSerializer(data,many=True)

        return Response(serializer.data)

    #   @method_decorator(login_required(login_url='/login'))
    @method_decorator(login_required)
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
    @method_decorator(login_required)
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
    @method_decorator(login_required)
    def delete(self, request, pk, format=None):
        todo_to_delete =  Products.objects.get(pk=pk)

        todo_to_delete.delete()

        return Response({
            'message': 'Todo Deleted Successfully'
        })





# Create your views here.
# class OrderView(LoginRequiredMixin,
#     mixins.CreateModelMixin,
#                       generics.GenericAPIView):
#     queryset=Order.objects.all()
#     serializers_class=OrderSerializers
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         print("order post")
#         return self.create(request, *args, **kwargs)


# class OrderItemView(LoginRequiredMixin,
#                     mixins.RetrieveModelMixin,
#                     generics.GenericAPIView):
#     queryset=OrderItem.objects.all()
#     serializers_class=OrderItemSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field="pk"
#     def retrieve(self, request, *args, **kwargs):
#         print("in order retrieve")
#         return self.create(request, *args, **kwargs)
