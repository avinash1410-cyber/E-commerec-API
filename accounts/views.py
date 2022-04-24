from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout





def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"accounts/login.html",{
                "message":"Invalid Credentials"
            })
    return render(request,"accounts/login.html")




def logout_page(request):
    logout(request)
    return render(request,'accounts/login.html',{
        'message':"Logged out"
    })



class CustomerAPIView(APIView):
    def get(self, request, pk=None, format=None):
        if pk:
            data = Customer.objects.get(id=pk)
            serializer = CustomerSerializer(data)
        else:
            data = Customer.objects.all()
            serializer = CustomerSerializer(data,many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = CustomerSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Todo Created Successfully',
            'data': serializer.data
        }
        return response

    # @method_decorator(login_required(login_url='/login'))
    @login_required
    def put(self, request, pk=None, format=None):
        todo_to_update = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(instance=todo_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Todo Updated Successfully',
            'data': serializer.data
        }
        return response

  #  @method_decorator(login_required(login_url='/login'))
    @login_required
    def delete(self, request, pk, format=None):
        todo_to_delete =  Customer.objects.get(pk=pk)

        todo_to_delete.delete()

        return Response({
            'message': 'Todo Deleted Successfully'
        })