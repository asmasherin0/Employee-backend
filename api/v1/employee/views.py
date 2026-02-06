from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from employee.models import Employee
from .serializers import EmployeeSerializer

class EmployeeListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(EmployeeSerializer(Employee.objects.all(), many=True).data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EmployeeDetail(APIView):
    permission_classes = [IsAuthenticated]


    def put(self, request, pk):
        emp = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        Employee.objects.get(pk=pk).delete()
        return Response({"message": "Deleted"})
