from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=150, write_only=True)
    
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "password2",
            "first_name",
            "last_name",
            "date_joined"
        )
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate_password2(self, value):
        password = self.initial_data.get('password')
        if password and value and password != value:
            raise serializers.ValidationError("Passwords mismatched")
        return value
    
    def create(self, validated_data):
        validated_data.pop('password2')
        instance = User.objects.create(
            **validated_data
        )
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class LoginTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
