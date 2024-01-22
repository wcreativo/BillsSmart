# serializers.py
from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if email is None or password is None:
            raise serializers.ValidationError("Email and password are required fields.")

        user = authenticate(
            request=self.context.get("request"), email=email, password=password
        )

        if user is None:
            raise serializers.ValidationError("Invalid email or password.")

        data["user"] = user
        return data
