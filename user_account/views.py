from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .models import User
from .permissions import IsAccountOwner
from .serializers import LoginTokenSerializer, UserSerializer

class Register(generics.CreateAPIView):
    """Create a new user"""
    model = User
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )
    queryset = User.objects.all()


class Login(ObtainAuthToken):
    """Authenticate a user and return a token along with user_id"""
    serializer_class = LoginTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id
        })
        
        
class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/Update details of a specific user.
    Delete account
    Must be called by account owner
    """
    model = User
    permission_classes = (permissions.IsAuthenticated, IsAccountOwner, )
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"