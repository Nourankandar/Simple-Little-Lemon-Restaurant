from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'bookings', views.BookingViewSet)
router.register(r'menu', views.MenuViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]