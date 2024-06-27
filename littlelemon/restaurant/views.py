from django.shortcuts import render
from rest_framework import generics
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
  permission_classes = [IsAuthenticated]
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer