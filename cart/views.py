from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from .models import Cart
from .serializers import CartSerializer
from rest_framework.response import Response


class CartAPIView(APIView):
    # template_name = "api/login.html"
    #    @method_decorator(login_required(login_url='/login'))
    @method_decorator(login_required(login_url='login'))
    def get(self, request, pk=None, format=None):
        if pk:
            data = Cart.objects.get(id=pk)
            serializer = CartSerializer(data,many=True)
        else:
            data = Cart.objects.all()
            serializer = CartSerializer(data)

        return Response(serializer.data)

    #   @method_decorator(login_required(login_url='/login'))
    @method_decorator(login_required(login_url='login'))
    def post(self, request, format=None):
        data = request.data
        serializer = CartSerializer(data=data)

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
        todo_to_update = Cart.objects.get(pk=pk)
        serializer = CartSerializer(instance=todo_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Todo Updated Successfully',
            'data': serializer.data
        }
        return response


#   #  @method_decorator(login_required(login_url='/login'))
    @method_decorator(login_required(login_url='login'))
    def delete(self, request, pk, format=None):
        todo_to_delete =  Cart.objects.get(pk=pk)

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











