from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response


class CategoryAPIView(APIView):
    # template_name = "api/login.html"
    #    @method_decorator(login_required(login_url='/login'))
    def get(self, request, pk=None, format=None):
        if pk:
            data = Category.objects.get(id=pk)
            serializer = CategorySerializer(data)
        else:
            data = Category.objects.all()
            serializer = CategorySerializer(data,many=True)

        return Response(serializer.data)

    #   @method_decorator(login_required(login_url='/login'))
    @method_decorator(login_required)
    def post(self, request, format=None):
        data = request.data
        serializer = CategorySerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Todo Created Successfully',
            'data': serializer.data
        }
        return response

# # @method_decorator(login_required(login_url='/login'))
#     def put(self, request, pk=None, format=None):
#         todo_to_update = Category.objects.get(pk=pk)
#         serializer = CategorySerializer(instance=todo_to_update,data=request.data, partial=True)
#
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#
#         response = Response()
#
#         response.data = {
#             'message': 'Todo Updated Successfully',
#             'data': serializer.data
#         }
#
#         return response
#
#   #  @method_decorator(login_required(login_url='/login'))
#     def delete(self, request, pk, format=None):
#         todo_to_delete =  Category.objects.get(pk=pk)
#
#         todo_to_delete.delete()
#
#         return Response({
#             'message': 'Todo Deleted Successfully'
#         })


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
