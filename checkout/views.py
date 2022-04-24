from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from .models import Check
from .serializers import CheckSerializer
from rest_framework.response import Response


class CheckAPIView(APIView):
    # template_name = "api/login.html"
    #    @method_decorator(login_required(login_url='/login'))
    @method_decorator(login_required)
    def get(self, request, pk=None, format=None):
        if pk:
            data = Check.objects.get(id=pk)
            serializer = CheckSerializer(data)
        else:
            data = Check.objects.all()
            serializer = CheckSerializer(data,many=True)

        return Response(serializer.data)

    #   @method_decorator(login_required(login_url='/login'))
    @method_decorator(login_required)
    def post(self, request, format=None):
        data = request.data
        serializer = CheckSerializer(data=data)

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
        todo_to_update = Check.objects.get(pk=pk)
        serializer = CheckSerializer(instance=todo_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Todo Updated Successfully',
            'data': serializer.data
        }
        return response


#   #  @method_decorator(login_required(login_url='/login'))
    @method_decorator(login_required)
    def delete(self, request, pk, format=None):
        todo_to_delete =  Check.objects.get(pk=pk)

        todo_to_delete.delete()

        return Response({
            'message': 'Todo Deleted Successfully'
        })