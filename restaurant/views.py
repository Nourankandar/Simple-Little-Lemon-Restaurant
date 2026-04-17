from rest_framework import viewsets
from .models import Booking,MenuItem
from .serializers import BookingSerializer,MenuItemSerializer
from rest_framework.permissions import IsAuthenticated


from django.shortcuts import render
def index(request):
    return render(request, 'index.html', {})



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer