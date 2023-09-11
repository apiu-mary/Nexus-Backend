from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from customer.models import Customer
from .serializer import CustomerSerializer
from django.http import Http404


# Create your views here.
class CustomerListView(APIView):
    def get(self, request):  
        try:
            customer = Customer.objects.all()
            serializer = CustomerSerializer(customer, many=True)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}),
    
    def post(self,request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


class CustomerDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            customer = Customer.objects.get(id=id)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            raise Http404("Customer not found")
    
    
    def put(self, request, id, format=None):
        try:
            customer = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            raise Http404("Customer not found")

        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, id, format = None):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response("customer deleted", status=status.HTTP_204_NO_CONTENT)
     