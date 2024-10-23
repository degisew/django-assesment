from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
from rest_framework import serializers
from social_auth.users.models import CustomUser


class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.ChoiceField(
        choices=[('admin', 'Admin'), ('coach', 'Coach'),
                 ('agent', 'Agent'), ('football_player', 'Football Player')]
    )

    def get_fields(self):
        fields = super().get_fields()

        if 'username' in fields:
            fields.pop('username')

        return fields
    def save(self, request):
        user = super().save(request)

        # Assign role
        user.role = self.validated_data.get('role', 'coach')
        user.save()

        return user


class CustomLoginSerializer(LoginSerializer):
    username = None

    def get_fields(self):
        fields = super().get_fields()

        if 'username' in fields:
            fields.pop('username')
        return fields

    def validate(self, attrs):
        # Use email instead of username for login
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            from django.contrib.auth import authenticate
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                raise serializers.ValidationError("Invalid email or password")
            attrs['user'] = user
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

        return attrs


class CustomUserDetailsSerializer(UserDetailsSerializer):
    role = serializers.CharField(source='get_role_display', read_only=True)

    class Meta(UserDetailsSerializer.Meta):
        model = CustomUser
        fields = UserDetailsSerializer.Meta.fields + ('role',)

