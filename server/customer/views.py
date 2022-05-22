from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .services import send
from .serializers import CountrySerializer, CustomerListSerializer, CustomerSerializer, PositionSerializer
from .models import Country, Customer, Position


# Create your views here.
class GetCustomerListView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializer


class AddCustomerView(CreateAPIView):
    serializer_class = CustomerSerializer


class AddCountryView(CreateAPIView):
    serializer_class = CountrySerializer


class AddPositionView(CreateAPIView):
    serializer_class = PositionSerializer


class UpdateCustomerView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DeleteCustomerView(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DeleteCountryView(DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class DeletePositionView(DestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class SendEmailView(APIView):
    def post(self, request):
        email = request.data['email']
        text = request.data['text']
        header = request.data['header']
        send(text=text, header=header, users_email=(email,))
        return Response(status=200)


class GetCountriesView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class GetPositionsView(ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer