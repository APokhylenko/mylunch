from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Product
from .serializers import UserSerializer, ProductSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class UserIsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


# class UserProfileChangeAPIView(generics.RetrieveAPIView,
#                                mixins.DestroyModelMixin,
#                                mixins.UpdateModelMixin):
#     permission_classes = (
#         permissions.IsAuthenticated,
#         UserIsOwnerOrReadOnly,
#     )
#     serializer_class = UserSerializer
#     parser_classes = (MultiPartParser, FormParser,)
#
#     def get_object(self):
#         username = self.kwargs["last_name"]
#         obj = get_object_or_404(User, last_name=username)
#         return obj
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

