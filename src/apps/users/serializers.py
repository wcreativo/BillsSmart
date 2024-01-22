# serializers.py
from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = User.objects.filter(email=email).first()

            if user and user.check_password(password):
                data["user"] = user
            else:
                raise serializers.ValidationError("Invalid email or password")
        else:
            raise serializers.ValidationError("Email and password are required")

        return data


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    def create(self, validated_data):
        user = User.objects.create(email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user
