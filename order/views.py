from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response

class OrderAPIView(APIView):
    # template_name = "api/login.html"
    #    @method_decorator(login_required(login_url='/login'))
    @method_decorator(login_required(login_url='login'))
    def get(self, request, pk=None, format=None):
        user = self.request.user
        print(user)
        if pk:
            data = Order.objects.get(id=pk)
            serializer = OrderSerializer(data)
        else:
            data = Order.objects.all()
            serializer = OrderSerializer(data,many=True)

        return Response(serializer.data)

    #   @method_decorator(login_required(login_url='/login'))
    @method_decorator(login_required(login_url='login'))
    def post(self, request, format=None):
        data = request.data
        serializer = OrderSerializer(data=data)

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
        todo_to_update = Order.objects.get(pk=pk)
        serializer = OrderSerializer(instance=todo_to_update,data=request.data, partial=True)

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
        todo_to_delete =  Order.objects.get(pk=pk)

        todo_to_delete.delete()

        return Response({
            'message': 'Todo Deleted Successfully'
        })
