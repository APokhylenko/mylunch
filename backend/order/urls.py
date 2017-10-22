from django.conf.urls import url
from rest_framework import routers
from .views import UserViewSet, ProductViewSet
# UserProfileChangeAPIView

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
# router.register(r'^update/(?P<username>[\w-]+)$', UserProfileChangeAPIView, 'update-user')

urlpatterns = router.urls
