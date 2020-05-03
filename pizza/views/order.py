from pizza.models import Order
from rest_framework import serializers, viewsets
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields='__all__'

# ViewSets define the view behavior.
class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @csrf_exempt
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)